/* Kidly-Demo: beantwortet die Serveranfragen von Kidly Family, Kidly Team und Kidly Admin
 * im Browser aus einem Mitschnitt mit fiktiven Daten. Nichts wird an einen Server geschickt,
 * Änderungen gelten nur bis zum Neuladen der Seite.
 *
 * Erwartet vorher: window.KIDLY_DEMO_DATEN (aus demo-daten-<app>.js) und
 * window.KIDLY_DEMO_CONFIG = { app, apiPrefix, tokenKey, personKey, basis }.
 */
(function () {
  'use strict';
  var C = window.KIDLY_DEMO_CONFIG, D = window.KIDLY_DEMO_DATEN;
  if (!C || !D || !D.konten || !D.konten.length) return;
  var originalFetch = window.fetch.bind(window);

  // --- Konto wählen (Rollenwechsel über die Demo-Leiste) ---
  var KEY = 'kidly-demo-konto-' + C.app;
  var idx = 0;
  try { idx = Math.min(Number(localStorage.getItem(KEY) || 0), D.konten.length - 1) || 0; } catch (e) {}
  var konto = D.konten[idx];

  // --- Tage auf heute verschieben ---
  var heute = new Date(); heute.setHours(0, 0, 0, 0);
  var aufnahme = new Date(D.aufgenommenAm + 'T00:00:00');
  var tage = Math.round((heute - aufnahme) / 864e5);
  // Uhrzeiten bleiben auch über die Zeitumstellung hinweg gleich (07:00 bleibt 07:00)
  var versatz = tage * 864e5 + (heute.getTimezoneOffset() - new Date(D.aufgenommenAm + 'T12:00:00').getTimezoneOffset()) * 6e4;
  var ISO_ZEIT = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$/, ISO_TAG = /^\d{4}-\d{2}-\d{2}$/;
  var aufnahmeMs = Date.parse(D.aufgenommenAm + 'T12:00:00Z');
  function nah(x) { return Math.abs(Date.parse(x.length === 10 ? x + 'T12:00:00Z' : x) - aufnahmeMs) <= 90 * 864e5; }
  function verschiebe(x) {
    if (typeof x === 'string') {
      // Nur Tage rund um die Aufnahme verschieben (Termine, Einträge) – Geburtstage und Vertragsbeginn bleiben.
      if (ISO_ZEIT.test(x)) return nah(x) ? new Date(Date.parse(x) + versatz).toISOString() : x;
      if (ISO_TAG.test(x)) { if (!nah(x)) return x; var d = new Date(x + 'T12:00:00Z'); d.setUTCDate(d.getUTCDate() + tage); return d.toISOString().slice(0, 10); }
      return x;
    }
    if (Array.isArray(x)) return x.map(verschiebe);
    if (x && typeof x === 'object') { var o = {}; for (var k in x) o[k] = verschiebe(x[k]); return o; }
    return x;
  }
  var store = {};
  Object.keys(konto.get).forEach(function (p) { store[p] = verschiebe(konto.get[p]); });
  var login = verschiebe(konto.login);
  var ich = login.person || {};
  var beispielBild = null;
  (function such(x) { if (beispielBild) return; if (typeof x === 'string' && /^\/uploads\/feed\//.test(x)) beispielBild = x; else if (x && typeof x === 'object') for (var k in x) such(x[k]); })(store);

  // --- automatisch angemeldet ---
  try {
    if (C.tokenKey) { sessionStorage.setItem(C.tokenKey, 'demo-token'); sessionStorage.setItem(C.personKey, JSON.stringify(ich)); }
  } catch (e) {}

  // --- Hilfen ---
  var UUID = /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i;
  function uuid() { return (crypto.randomUUID && crypto.randomUUID()) || ('d' + Date.now() + Math.random()).replace('.', ''); }
  function trenne(pfad) { var i = pfad.indexOf('?'); return i < 0 ? [pfad, ''] : [pfad.slice(0, i), pfad.slice(i + 1)]; }
  function params(q) { var o = {}; new URLSearchParams(q).forEach(function (v, k) { o[k] = v; }); return o; }
  var DATUMS_PARAMS = ['von', 'bis', 'stichtag', 'monat', 'datum'];
  function finde(pfad) {
    if (pfad in store) return pfad;
    var t = trenne(pfad), p = params(t[1]);
    var kandidaten = Object.keys(store).filter(function (k) { return trenne(k)[0] === t[0]; });
    var passend = kandidaten.filter(function (k) {
      var kp = params(trenne(k)[1]);
      return Object.keys(p).every(function (n) { return DATUMS_PARAMS.indexOf(n) >= 0 || kp[n] === p[n]; });
    });
    return passend[0] || null;
  }
  function antwort(daten, status) {
    return Promise.resolve(new Response(daten === undefined ? null : JSON.stringify(daten), { status: status || 200, headers: { 'content-type': 'application/json' } }));
  }
  function jetztFelder(o) {
    ['createdAt', 'erstelltAm', 'gesendetAm', 'updatedAt', 'eingereichtAm', 'zeitpunkt', 'datum'].forEach(function (f) {
      if (f in o && (!o[f] || ISO_ZEIT.test(o[f]))) o[f] = new Date().toISOString();
    });
    return o;
  }
  function alleObjekte(cb) {
    function lauf(x) {
      if (Array.isArray(x)) x.forEach(lauf);
      else if (x && typeof x === 'object') { cb(x); for (var k in x) lauf(x[k]); }
    }
    Object.keys(store).forEach(function (k) { lauf(store[k]); });
  }
  function koerper(init) {
    var b = init && init.body;
    if (!b) return {};
    if (typeof b === 'string') { try { return JSON.parse(b); } catch (e) { return {}; } }
    if (typeof FormData !== 'undefined' && b instanceof FormData) {
      var o = {};
      b.forEach(function (v, k) {
        if (typeof v === 'string') o[k] = v;
        else if (k === 'foto' || k === 'datei' || k === 'logo') o._datei = URL.createObjectURL(v);
      });
      return o;
    }
    return {};
  }

  // --- Schreibzugriffe: in die passenden Listen übernehmen ---
  function schreiben(methode, pfad, body) {
    var t = trenne(pfad)[0];
    // An-/Abmelden
    if (/\/auth\/login$/.test(t)) return login;
    if (/\/push\/token/.test(t)) return { ok: true };
    // Anwesenheit
    var anw = t.match(/\/anwesenheit\/(checkin|checkout)$/);
    if (anw) {
      var zeile = null;
      alleObjekte(function (o) { if (o.kindId === body.kindId && 'status' in o && ('zeitpunktEin' in o)) { zeile = o; } });
      if (zeile) {
        if (anw[1] === 'checkin') { zeile.status = 'ANWESEND'; zeile.zeitpunktEin = new Date().toISOString(); zeile.zeitpunktAus = null; zeile.eingechecktVon = (ich.vorname || '') + ' ' + (ich.nachname || ''); }
        else { zeile.status = 'ABGEHOLT'; zeile.zeitpunktAus = new Date().toISOString(); }
      }
      return zeile || {};
    }
    // Aktion auf ein bestimmtes Objekt (…/<id>/antwort, …/<id>/beenden, …/freigeben)
    var aktion = t.match(/\/([0-9a-f-]{36})\/([a-z-]+)$/i);
    if (methode === 'POST' && aktion) {
      var treffer = null;
      alleObjekte(function (o) { if (o.id === aktion[1]) { Object.assign(o, body); treffer = o; } });
      return treffer || Object.assign({ id: aktion[1] }, body);
    }
    // Ändern / Löschen über die ID am Ende
    var id = (t.match(/\/([0-9a-f-]{36})$/i) || [])[1];
    if ((methode === 'PATCH' || methode === 'PUT') && id) {
      var geaendert = null;
      alleObjekte(function (o) { if (o.id === id) { Object.assign(o, body); geaendert = o; } });
      if (t in store && !Array.isArray(store[t])) Object.assign(store[t], body);
      return geaendert || Object.assign({ id: id }, body);
    }
    if (methode === 'PUT') { store[t] = Object.assign({}, store[t] || {}, body); return store[t]; }
    if (methode === 'DELETE') {
      Object.keys(store).forEach(function (k) {
        if (Array.isArray(store[k])) store[k] = store[k].filter(function (o) { return !(o && o.id === id); });
      });
      return null;
    }
    // Neu anlegen: in jede Liste mit gleichem Pfad, deren Filter zum neuen Eintrag passen
    var neu = null;
    Object.keys(store).forEach(function (k) {
      var kt = trenne(k), liste = store[k];
      if (kt[0] !== t || !Array.isArray(liste)) return;
      var p = params(kt[1]);
      var passt = Object.keys(p).every(function (n) { return DATUMS_PARAMS.indexOf(n) >= 0 || body[n] === undefined || body[n] === p[n]; });
      if (!passt) return;
      if (!neu) {
        var vorlage = liste[0] ? JSON.parse(JSON.stringify(liste[0])) : {};
        neu = jetztFelder(Object.assign(vorlage, body, { id: uuid() }));
        ['absenderId', 'autorId', 'erstelltVonId', 'personId'].forEach(function (f) { if (f in neu && !(f in body)) neu[f] = ich.id; });
        if (neu.absender && typeof neu.absender === 'object') neu.absender = { id: ich.id, vorname: ich.vorname, nachname: ich.nachname, rolle: ich.rolle };
        if (neu.autor && typeof neu.autor === 'object') neu.autor = { vorname: ich.vorname, nachname: ich.nachname };
        // Hochgeladene Fotos bleiben im Browser; angezeigt wird stattdessen ein Beispielbild aus der Demo.
        if (body._datei && beispielBild) { neu.fotoUrl = beispielBild; neu.fotoZurueckgehalten = false; neu.fotoAnonymisiert = false; }
        if ('kinder' in neu && Array.isArray(neu.kinder)) neu.kinder = [];
        delete neu._datei;
      }
      var neuesteZuerst = liste.length > 1 && String(liste[0].createdAt || liste[0].erstelltAm || '') > String(liste[liste.length - 1].createdAt || liste[liste.length - 1].erstelltAm || '');
      if (neuesteZuerst) liste.unshift(neu); else liste.push(neu);
    });
    return neu || jetztFelder(Object.assign({ id: uuid() }, body));
  }

  // --- Live-Verbindung: kleiner socket.io-Ersatz im Browser ---
  // Die Apps bekommen neue Chat-Nachrichten und Anwesenheits-Änderungen über socket.io.
  // In der Demo antwortet dieser Ersatz auf den Verbindungsaufbau und schickt nach eigenen
  // Änderungen dieselben Ereignisse, die sonst der Server schicken würde.
  var EchtesWS = window.WebSocket, sockets = [];
  function FakeSocket(url) {
    var ws = this; ws.url = String(url); ws.readyState = 0; ws.binaryType = 'arraybuffer'; ws.ns = [];
    function an(daten) { if (ws.readyState === 1 && ws.onmessage) ws.onmessage({ data: daten }); }
    ws._an = an;
    setTimeout(function () {
      ws.readyState = 1; sockets.push(ws);
      if (ws.onopen) ws.onopen({});
      an('0{"sid":"demo","upgrades":[],"pingInterval":25000,"pingTimeout":60000,"maxPayload":1000000}');
      ws._ping = setInterval(function () { an('2'); }, 25000);
    }, 30);
    ws.send = function (d) {
      d = String(d);
      var m = d.match(/^40(\/[^,]*)?,?/);
      if (m) { var ns = m[1] || ''; ws.ns.push(ns); setTimeout(function () { an('40' + (ns ? ns + ',' : '') + '{"sid":"demo-' + ns + '"}'); }, 10); }
    };
    ws.close = function () {
      if (ws.readyState === 3) return;
      ws.readyState = 3; clearInterval(ws._ping);
      sockets = sockets.filter(function (x) { return x !== ws; });
      if (ws.onclose) ws.onclose({ code: 1000, reason: '', wasClean: true });
    };
    ws.addEventListener = function () {}; ws.removeEventListener = function () {};
  }
  function ereignis(nsEnde, name, daten) {
    setTimeout(function () {
      sockets.forEach(function (ws) {
        ws.ns.forEach(function (ns) {
          if (ns.slice(-nsEnde.length) === nsEnde) ws._an('42' + ns + ',' + JSON.stringify(daten === undefined ? [name] : [name, daten]));
        });
      });
    }, 60);
  }
  window.WebSocket = function (url, prot) {
    if (/socket\.io/.test(String(url))) return new FakeSocket(url);
    return prot === undefined ? new EchtesWS(url) : new EchtesWS(url, prot);
  };
  ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED'].forEach(function (k, i) { window.WebSocket[k] = i; });
  try { if (navigator.serviceWorker) navigator.serviceWorker.register = function () { return Promise.resolve({}); }; } catch (e) {}

  // --- fetch abfangen ---
  window.fetch = function (eingabe, init) {
    var url = typeof eingabe === 'string' ? eingabe : (eingabe && eingabe.url) || String(eingabe);
    var methode = ((init && init.method) || (eingabe && eingabe.method) || 'GET').toUpperCase();
    var abs = new URL(url, location.href);
    var voll = abs.href;
    if (/\/api\/session$/.test(abs.pathname)) return antwort(methode === 'GET' ? { authenticated: true } : undefined, methode === 'GET' ? 200 : 204);
    var pfad = null;
    if (C.apiPrefix && voll.indexOf(C.apiPrefix) === 0) pfad = voll.slice(C.apiPrefix.length);
    else if (abs.pathname.indexOf('/api/backend-proxy') >= 0) pfad = abs.pathname.slice(abs.pathname.indexOf('/api/backend-proxy') + 18) + abs.search;
    if (pfad === null) return originalFetch(eingabe, init);
    pfad = decodeURIComponent(pfad);
    if (methode === 'GET') {
      if (/\/person\/me$/.test(trenne(pfad)[0]) && !finde(pfad)) return antwort(ich);
      var key = finde(pfad);
      if (key) return antwort(store[key]);
      var letzter = trenne(pfad)[0].split('/').pop();
      return UUID.test(letzter) || /qr-code|bericht|ergebnisse|status/.test(letzter)
        ? antwort({ message: 'In der Demo nicht verfügbar.' }, 404)
        : antwort([]);
    }
    if (/export|datev|bericht|qr-code/.test(pfad)) return antwort({ message: 'In der Demo nicht verfügbar.' }, 400);
    var ergebnis = schreiben(methode, pfad, koerper(init)), t = trenne(pfad)[0];
    if (methode === 'POST' && t === '/nachricht') ereignis('/chat', 'nachricht:new', ergebnis);
    else if (methode === 'POST' && t === '/intern-chat') ereignis('/intern-chat', 'nachricht:new', ergebnis);
    else if (/^\/(anwesenheit|krankmeldung|urlaub|tagesprotokoll)/.test(t)) ereignis('/anwesenheit', 'gruppe:update');
    return antwort(ergebnis, methode === 'POST' ? 201 : 200);
  };

  // --- Demo-Leiste mit Rollenwechsel ---
  // Handy-Apps: schmale Leiste oben, die App rückt darunter. Kidly Admin: kleine Pille unten rechts.
  var oben = C.app !== 'admin';
  function leiste() {
    var bar = document.createElement('div');
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', 'Demo');
    bar.style.cssText = 'position:fixed;z-index:2147483647;display:flex;gap:8px;align-items:center;background:#111827;color:#fff;' +
      'font:600 12px/1.2 system-ui,-apple-system,Segoe UI,sans-serif;' +
      (oben ? 'top:0;left:0;right:0;height:34px;padding:0 8px 0 12px;justify-content:space-between'
            : 'right:12px;bottom:12px;padding:6px 6px 6px 12px;border-radius:999px;box-shadow:0 6px 20px rgba(0,0,0,.25)');
    if (oben) {
      var css = document.createElement('style');
      css.textContent = '#root{position:fixed!important;top:34px!important;left:0;right:0;bottom:0;height:auto!important}';
      document.head.appendChild(css);
    }
    var txt = document.createElement('span');
    txt.textContent = oben && window.innerWidth < 520 ? 'Demo-Modus' : 'Demo mit erfundenen Daten · nichts wird gespeichert';
    txt.style.whiteSpace = 'nowrap';
    txt.style.overflow = 'hidden';
    txt.style.textOverflow = 'ellipsis';
    bar.appendChild(txt);
    var rechts = document.createElement('span');
    rechts.style.cssText = 'display:flex;gap:6px;align-items:center;flex-shrink:0';
    if (D.konten.length > 1) {
      var sel = document.createElement('select');
      sel.setAttribute('aria-label', 'Als wer ansehen?');
      sel.style.cssText = 'font:inherit;border-radius:999px;border:0;padding:4px 8px;background:#2563eb;color:#fff;max-width:150px';
      D.konten.forEach(function (k, i) {
        var o = document.createElement('option'); o.value = String(i);
        var p = k.login.person || {}; o.textContent = (p.vorname || '') + ' ' + (p.nachname || '');
        if (i === idx) o.selected = true; sel.appendChild(o);
      });
      sel.onchange = function () { try { localStorage.setItem(KEY, sel.value); sessionStorage.clear(); } catch (e) {} location.reload(); };
      rechts.appendChild(sel);
    }
    var zur = document.createElement('a');
    zur.href = C.basis + '/';
    zur.textContent = 'Übersicht';
    zur.style.cssText = 'color:#fff;background:#374151;border-radius:999px;padding:4px 10px;text-decoration:none';
    rechts.appendChild(zur);
    bar.appendChild(rechts);
    document.body.appendChild(bar);
  }
  if (document.body) leiste(); else document.addEventListener('DOMContentLoaded', leiste);
})();
