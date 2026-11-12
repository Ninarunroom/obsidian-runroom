/**
 * Spradling · Datos diarios de Google Ads → Google Sheets
 * Runroom · v1 (06/11/2026) · copia adaptada del script de Barraquer
 *
 * Qué hace: cada noche lee de Google Ads el rendimiento por campaña y día, y por
 * campaña, región/provincia y día, y lo escribe en un Google Sheet. De ahí lo lee
 * la tarea diaria de Claude para calcular alertas (CTR, CPC, CPL, CR, VTR, picos
 * de gasto, campañas paradas) y para optimizar por zonas.
 *
 * SOLO LEE datos. No cambia nada en las cuentas de Google Ads.
 *
 * Instalación (5 min):
 *  1. El Sheet "Spradling - Google Ads diario" ya está creado (Drive de Nina) y su URL ya está puesta.
 *  2. En la MCC: Herramientas → Acciones masivas → Scripts → + → Nuevo script. Pega este código.
 *  3. La cuenta de Spradling (350-973-8243) ya está fijada en ACCOUNT_IDS.
 *  4. "Autorizar" y después "Vista previa" para probarlo. Revisa el Sheet.
 *  5. Guarda y programa la frecuencia: Diaria, a las 5:00.
 * También funciona pegado dentro de una sola cuenta (sin MCC).
 */

var CONFIG = {
  SPREADSHEET_URL: 'https://docs.google.com/spreadsheets/d/1sriNDuHvnG8zTRi07J_-yoHd-lB8ciazJWXwMG6Y_nw/edit',
  // Cuentas a leer. Vacío = todas las cuentas de la MCC cuyo nombre contenga ACCOUNT_NAME_CONTAINS.
  // Ejemplo: ['123-456-7890', '234-567-8901']
  ACCOUNT_IDS: ['350-973-8243'],
  ACCOUNT_NAME_CONTAINS: 'spradling',
  // Campaña × día: histórico desde el 1 de enero del año anterior hasta ayer (se reescribe cada noche
  // porque las conversiones llegan con retraso). Zona × día: solo los últimos GEO_DAYS días.
  GEO_DAYS: 90,
  // Pestaña por zona (región y provincia de la ubicación física del usuario).
  GEO: true
};

var H_DIA = ['Fecha', 'Cuenta', 'ID cuenta', 'Campaña', 'ID campaña', 'Estado', 'Tipo',
  'Inversión', 'Impresiones', 'Clics', 'Conversiones', 'Views',
  'CTR', 'CPC', 'CPL', 'CR', 'VTR'];
var H_GEO = ['Fecha', 'Cuenta', 'Campaña', 'ID campaña', 'País', 'Región', 'Provincia',
  'Inversión', 'Impresiones', 'Clics', 'Conversiones', 'CTR', 'CPC', 'CPL', 'CR'];
var H_CAMP = ['Cuenta', 'ID cuenta', 'Campaña', 'ID campaña', 'Estado', 'Tipo', 'Estrategia de puja', 'Presupuesto diario'];

function main() {
  var ss = SpreadsheetApp.openByUrl(CONFIG.SPREADSHEET_URL);
  var dia = [], geo = [], geoMes = [], camp = [], log = [];
  var geoNames = {};
  var cuentas = cuentas_();
  var rango = null;

  for (var i = 0; i < cuentas.length; i++) {
    var acc = cuentas[i];
    if (acc) AdsManagerApp.select(acc);
    var nombre = AdsApp.currentAccount().getName();
    try {
      rango = rango || rango_();
      leerDia_(rango, dia, log);
      leerCampanas_(camp);
      if (CONFIG.GEO) {
        leerGeo_({ desde: rango.geoDesde, hasta: rango.hasta }, geo, geoNames, log, 'segments.date');
        leerGeo_(rango, geoMes, geoNames, log, 'segments.month');
      }
      log.push('OK ' + nombre);
    } catch (e) {
      log.push('ERROR ' + nombre + ': ' + e.message);
    }
  }

  if (CONFIG.GEO) { traducirGeo_(geo, geoNames, log); traducirGeo_(geoMes, geoNames, log); }

  escribir_(ss, 'Diario_Campañas', H_DIA, dia);
  if (CONFIG.GEO) {
    escribir_(ss, 'Diario_Zonas', H_GEO, geo);
    escribir_(ss, 'Mensual_Zonas', ['Mes'].concat(H_GEO.slice(1)), geoMes);
  }
  escribir_(ss, 'Campañas', H_CAMP, camp);
  escribir_(ss, 'Info', ['Clave', 'Valor'], [
    ['Última ejecución', Utilities.formatDate(new Date(), 'Europe/Madrid', 'yyyy-MM-dd HH:mm')],
    ['Desde', rango ? rango.desde : ''],
    ['Hasta', rango ? rango.hasta : ''],
    ['Cuentas', cuentas.length],
    ['Filas campaña-día', dia.length],
    ['Zonas desde', rango ? rango.geoDesde : ''],
    ['Filas zona-día', geo.length],
    ['Filas zona-mes', geoMes.length],
    ['Log', log.join(' | ').slice(0, 45000)]
  ]);
}

// ── Cuentas ────────────────────────────────────────────────────────────────
function cuentas_() {
  if (typeof AdsManagerApp === 'undefined') return [null];
  var sel = AdsManagerApp.accounts();
  if (CONFIG.ACCOUNT_IDS.length) sel = sel.withIds(CONFIG.ACCOUNT_IDS);
  var it = sel.get(), out = [];
  while (it.hasNext()) {
    var a = it.next();
    if (CONFIG.ACCOUNT_IDS.length || a.getName().toLowerCase().indexOf(CONFIG.ACCOUNT_NAME_CONTAINS.toLowerCase()) >= 0) out.push(a);
  }
  return out;
}

function rango_() {
  var tz = AdsApp.currentAccount().getTimeZone();
  var ayer = new Date(Date.now() - 24 * 3600 * 1000);
  var anio = Number(Utilities.formatDate(ayer, tz, 'yyyy')) - 1;
  var geo = new Date(Date.now() - CONFIG.GEO_DAYS * 24 * 3600 * 1000);
  return { desde: anio + '-01-01', hasta: Utilities.formatDate(ayer, tz, 'yyyy-MM-dd'),
    geoDesde: Utilities.formatDate(geo, tz, 'yyyy-MM-dd') };
}

// ── Campaña × día ──────────────────────────────────────────────────────────
function leerDia_(r, out, log) {
  // El nombre del campo de views cambió entre versiones de la API: probamos los dos.
  var variantes = ['metrics.video_trueview_views', 'metrics.video_views', null];
  for (var v = 0; v < variantes.length; v++) {
    var campoViews = variantes[v];
    var q = 'SELECT customer.id, customer.descriptive_name, campaign.id, campaign.name, campaign.status, ' +
      'campaign.advertising_channel_type, segments.date, metrics.cost_micros, metrics.impressions, ' +
      'metrics.clicks, metrics.conversions' + (campoViews ? ', ' + campoViews : '') +
      ' FROM campaign WHERE segments.date BETWEEN "' + r.desde + '" AND "' + r.hasta + '" AND metrics.impressions > 0';
    try {
      var it = AdsApp.search(q), filas = [];
      while (it.hasNext()) {
        var x = it.next(), m = x.metrics || {};
        var views = campoViews ? num_(campoViews === 'metrics.video_views' ? m.videoViews : m.videoTrueviewViews) : 0;
        var inv = num_(m.costMicros) / 1e6, imp = num_(m.impressions), cl = num_(m.clicks), conv = num_(m.conversions);
        filas.push([x.segments.date, x.customer.descriptiveName, x.customer.id, x.campaign.name, String(x.campaign.id),
          x.campaign.status, x.campaign.advertisingChannelType,
          r2_(inv), imp, cl, r2_(conv), views].concat(ratios_(inv, imp, cl, conv, views)));
      }
      Array.prototype.push.apply(out, filas);
      if (!campoViews) log.push('Aviso: sin campo de views');
      return;
    } catch (e) {
      if (v === variantes.length - 1) throw e;
    }
  }
}

// ── Campañas (estado y presupuesto) ────────────────────────────────────────
function leerCampanas_(out) {
  var q = 'SELECT customer.id, customer.descriptive_name, campaign.id, campaign.name, campaign.status, ' +
    'campaign.advertising_channel_type, campaign.bidding_strategy_type, campaign_budget.amount_micros ' +
    'FROM campaign WHERE campaign.status != "REMOVED"';
  var it = AdsApp.search(q);
  while (it.hasNext()) {
    var x = it.next();
    out.push([x.customer.descriptiveName, x.customer.id, x.campaign.name, String(x.campaign.id), x.campaign.status,
      x.campaign.advertisingChannelType, x.campaign.biddingStrategyType,
      x.campaignBudget ? r2_(num_(x.campaignBudget.amountMicros) / 1e6) : '']);
  }
}

// ── Campaña × zona × día (ubicación física del usuario) ────────────────────
function leerGeo_(r, out, names, log, segFecha) {
  // segFecha: 'segments.date' (zona × día) o 'segments.month' (zona × mes).
  var variantes = [
    ['segments.geo_target_region', 'segments.geo_target_province'],
    ['segments.geo_target_region'],
    ['segments.geo_target_most_specific_location']
  ];
  for (var v = 0; v < variantes.length; v++) {
    var seg = variantes[v];
    var q = 'SELECT customer.descriptive_name, campaign.id, campaign.name, ' + segFecha + ', ' +
      'geographic_view.country_criterion_id, ' + seg.join(', ') + ', ' +
      'metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions ' +
      'FROM geographic_view WHERE segments.date BETWEEN "' + r.desde + '" AND "' + r.hasta + '" ' +
      'AND geographic_view.location_type = "LOCATION_OF_PRESENCE" AND metrics.impressions > 0';
    try {
      var it = AdsApp.search(q), filas = [];
      while (it.hasNext()) {
        var x = it.next(), m = x.metrics || {}, s = x.segments || {};
        var pais = x.geographicView && x.geographicView.countryCriterionId ? 'geoTargetConstants/' + x.geographicView.countryCriterionId : '';
        var reg = s.geoTargetRegion || s.geoTargetMostSpecificLocation || '';
        var prov = s.geoTargetProvince || '';
        [pais, reg, prov].forEach(function (k) { if (k) names[k] = ''; });
        var inv = num_(m.costMicros) / 1e6, imp = num_(m.impressions), cl = num_(m.clicks), conv = num_(m.conversions);
        var rat = ratios_(inv, imp, cl, conv, 0);
        filas.push([segFecha === 'segments.month' ? s.month : s.date, x.customer.descriptiveName, x.campaign.name, String(x.campaign.id), pais, reg, prov,
          r2_(inv), imp, cl, r2_(conv), rat[0], rat[1], rat[2], rat[3]]);
      }
      Array.prototype.push.apply(out, filas);
      if (v > 0) log.push('Zonas con variante ' + seg.join('+'));
      return;
    } catch (e) {
      if (v === variantes.length - 1) { log.push('Zonas no disponibles: ' + e.message); return; }
    }
  }
}

function traducirGeo_(rows, names, log) {
  var keys = Object.keys(names);
  for (var i = 0; i < keys.length; i += 300) {
    var lote = keys.slice(i, i + 300).map(function (k) { return '"' + k + '"'; }).join(', ');
    try {
      var it = AdsApp.search('SELECT geo_target_constant.resource_name, geo_target_constant.name FROM geo_target_constant ' +
        'WHERE geo_target_constant.resource_name IN (' + lote + ')');
      while (it.hasNext()) { var g = it.next().geoTargetConstant; names[g.resourceName] = g.name; }
    } catch (e) { log.push('Nombres de zonas: ' + e.message); }
  }
  rows.forEach(function (r) { for (var c = 4; c <= 6; c++) if (r[c]) r[c] = names[r[c]] || r[c]; });
}

// ── Utilidades ─────────────────────────────────────────────────────────────
function ratios_(inv, imp, cl, conv, views) {
  return [
    imp ? r4_(cl / imp) : '',      // CTR
    cl ? r2_(inv / cl) : '',       // CPC
    conv ? r2_(inv / conv) : '',   // CPL
    cl ? r4_(conv / cl) : '',      // CR
    imp && views ? r4_(views / imp) : ''  // VTR
  ];
}
function num_(x) { var n = Number(x); return isNaN(n) ? 0 : n; }
function r2_(n) { return Math.round(n * 100) / 100; }
function r4_(n) { return Math.round(n * 10000) / 10000; }

function escribir_(ss, nombre, cab, filas) {
  var sh = ss.getSheetByName(nombre) || ss.insertSheet(nombre);
  sh.clearContents();
  var datos = [cab].concat(filas);
  var lote = 20000;
  for (var i = 0; i < datos.length; i += lote) {
    var trozo = datos.slice(i, i + lote);
    sh.getRange(i + 1, 1, trozo.length, cab.length).setValues(trozo);
  }
  sh.setFrozenRows(1);
}
