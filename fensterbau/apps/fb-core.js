/* ProFitAR & PassFort – gemeinsamer Kern: Anmeldung, Firma, Projekte, Fotos, Offline-Speicher, Demo.
   Läuft als statische Seite (GitHub Pages); Daten in Supabase (Tabellen fb_*), Dateien im privaten Bucket "fensterbau". */
(() => {
  const SB_URL = 'https://brtdtjqinyhsesiqhkkk.supabase.co';
  const SB_KEY = 'sb_publishable_i5Lf1DJYMBVX0yQOW2_nKQ_bRBbDUD2';
  const FN = SB_URL + '/functions/v1/fb-konto';
  const VERSION = '2026-11-04c';
  const qs = new URLSearchParams(location.search);
  let demo = qs.get('demo') === '1';
  try { if (qs.get('demo') === '0') sessionStorage.removeItem('fb.demo'); else if (demo) sessionStorage.setItem('fb.demo', '1'); else demo = sessionStorage.getItem('fb.demo') === '1'; } catch {}

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const uid = () => (crypto.randomUUID ? crypto.randomUUID() : 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => { const r = Math.random() * 16 | 0; return (c === 'x' ? r : (r & 3 | 8)).toString(16); }));
  const today = () => { const d = new Date(); return new Date(d.getTime() - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
  const fmtDate = s => { if (!s) return '—'; const d = new Date(String(s).length === 10 ? s + 'T12:00:00' : s); return isNaN(d) ? '—' : d.toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit', year: 'numeric' }); };
  const fmtDT = s => { if (!s) return '—'; const d = new Date(s); return isNaN(d) ? '—' : d.toLocaleString('de-DE', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }); };
  const ERR = {
    EINGABE: 'Bitte alle Pflichtfelder ausfüllen.', PASSWORT: 'Das Passwort braucht mindestens 10 Zeichen.', AGB: 'Bitte AGB und Auftragsverarbeitung bestätigen.',
    EMAIL_VERGEBEN: 'Diese E-Mail-Adresse ist schon vergeben. Bitte melde dich an oder nutze eine andere Adresse.', LIMIT: 'Gerade zu viele Anfragen. Bitte später erneut versuchen.',
    TEAMLIMIT: 'Euer Tarif erlaubt keine weiteren Personen. Wechsle den Tarif unter „Abo“.', ABO: 'Eure Testphase bzw. euer Abo ist abgelaufen.', RECHTE: 'Das darf nur der Inhaber.',
    LOGIN: 'Bitte melde dich an.', KEIN_TEAM: 'Dieses Konto gehört zu keinem Betrieb.', BESTAETIGUNG: 'Der eingegebene Firmenname stimmt nicht.', PASS: 'Dieser Fensterpass wurde nicht gefunden.', GELOESCHT: 'Der Betrieb und alle Daten wurden gelöscht.', FEHLER: 'Das hat nicht geklappt. Bitte erneut versuchen.'
  };
  const errText = e => {
    const m = String(e?.code || e?.message || e || '');
    if (ERR[m]) return ERR[m];
    if (/Invalid login credentials/i.test(m)) return 'E-Mail oder Passwort stimmt nicht.';
    if (/Email not confirmed/i.test(m)) return 'Bitte bestätige zuerst deine E-Mail-Adresse (Link in der Willkommens-Mail).';
    if (/Failed to fetch|NetworkError|network/i.test(m)) return 'Keine Verbindung. Deine Eingaben sind auf dem Gerät gespeichert.';
    if (/row-level security|violates row-level/i.test(m)) return 'Speichern nicht möglich – Testphase oder Abo abgelaufen.';
    if (/expired|invalid.*(token|otp)|otp/i.test(m)) return 'Der Link ist abgelaufen oder wurde schon benutzt. Bitte neu anfordern.';
    return m.slice(0, 160) || ERR.FEHLER;
  };
  function toast(msg, ms = 2800) { let t = $('#fbToast'); if (!t) { t = document.createElement('div'); t.id = 'fbToast'; t.className = 'toast'; t.setAttribute('role', 'status'); document.body.append(t); } t.textContent = msg; t.hidden = false; clearTimeout(t._h); t._h = setTimeout(() => { t.hidden = true; }, ms); }
  function sheet(html, onClose) {
    const s = document.createElement('div'); s.className = 'scrim'; s.innerHTML = `<div class="sheet" role="dialog" aria-modal="true">${html}</div>`;
    const close = () => { s.remove(); document.removeEventListener('keydown', key); onClose && onClose(); };
    const key = e => { if (e.key === 'Escape') close(); };
    s.addEventListener('click', e => { if (e.target === s || e.target.closest('[data-close]')) close(); });
    document.addEventListener('keydown', key); document.body.append(s);
    setTimeout(() => s.querySelector('input,select,textarea,button')?.focus(), 30);
    return { el: s.firstElementChild, close };
  }
  const confirmDlg = (text, ok = 'Ja', danger = false) => new Promise(res => {
    const d = sheet(`<p style="font-size:16px">${esc(text)}</p><div class="row" style="margin-top:16px;justify-content:flex-end"><button class="btn ghost" data-close>Abbrechen</button><button class="btn ${danger ? 'danger' : ''}" id="cfOk">${esc(ok)}</button></div>`, () => res(false));
    $('#cfOk', d.el).onclick = () => { res(true); d.el.parentElement.remove(); };
  });

  /* ---------- IndexedDB: Zwischenspeicher, Warteschlange, Dateien ---------- */
  const idb = new Promise((res, rej) => {
    const r = indexedDB.open(demo ? 'fensterbau-demo' : 'fensterbau', 1);
    r.onupgradeneeded = () => { const d = r.result; ['projekte', 'outbox', 'files', 'kv'].forEach(n => d.objectStoreNames.contains(n) || d.createObjectStore(n)); };
    r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
  });
  const tx = async (store, mode, fn) => { const d = await idb; return new Promise((res, rej) => { const t = d.transaction(store, mode); const s = t.objectStore(store); const out = fn(s); t.oncomplete = () => res(out instanceof IDBRequest ? out.result : out); t.onerror = () => rej(t.error); }); };
  const put = (st, k, v) => tx(st, 'readwrite', s => { s.put(v, k); });
  const get = (st, k) => tx(st, 'readonly', s => s.get(k));
  const del = (st, k) => tx(st, 'readwrite', s => { s.delete(k); });
  const all = async st => { const d = await idb; return new Promise((res, rej) => { const out = []; const r = d.transaction(st).objectStore(st).openCursor(); r.onsuccess = () => { const c = r.result; if (c) { out.push([c.key, c.value]); c.continue(); } else res(out); }; r.onerror = () => rej(r.error); }); };

  /* ---------- Supabase ---------- */
  const sb = !demo && window.supabase ? window.supabase.createClient(SB_URL, SB_KEY, { auth: { persistSession: true, autoRefreshToken: true, storageKey: 'fensterbau-auth', detectSessionInUrl: false } }) : null;
  const S = { user: null, firma: null, rolle: null, me: null, demo, online: navigator.onLine };

  async function call(action, body = {}) {
    const h = { 'Content-Type': 'application/json', apikey: SB_KEY };
    const t = sb && (await sb.auth.getSession()).data.session?.access_token; if (t) h.Authorization = 'Bearer ' + t;
    const r = await fetch(FN, { method: 'POST', headers: h, body: JSON.stringify({ action, ...body }) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok || j.error) throw Object.assign(new Error(j.error || 'FEHLER'), { code: j.error || 'FEHLER' });
    return j;
  }

  /* Demo: Beispielbetrieb, alles bleibt im Browser */
  const DEMO_FIRMA = { id: 'demo', name: 'Fensterbau Muster (Demo)', anschrift: 'Musterstraße 1, 12345 Musterstadt', telefon: '01234 56789', email: 'service@example.com', web: '', logo: null, plan: 'team', testphase_bis: new Date(Date.now() + 14 * 864e5).toISOString(), bezahlt_bis: null,
    pruefliste: ['Fenster und Türen auf leichtgängige Funktion geprüft', 'Dichtungen, Beschläge und Entwässerung kontrolliert', 'Anschlüsse innen und außen sauber ausgeführt', 'Baustelle gereinigt, Verpackung entsorgt', 'Kunde in Bedienung und Pflege eingewiesen'],
    pflege: 'Beschläge einmal im Jahr leicht ölen. Dichtungen mit Wasser und mildem Reiniger säubern, danach mit Pflegestift behandeln. Entwässerungsschlitze frei halten. Rahmen nicht mit scheuernden Mitteln reinigen.',
    mwst: 19, angebot_text: 'Vielen Dank für Ihre Anfrage. Gern bieten wir Ihnen folgende Leistungen an. Das Angebot gilt 30 Tage. Maße vorbehaltlich der Prüfung vor Bestellung.', bewertung_link: '', bewertung_tage: 3,
    preise: { typen: { 'Dreh-Kipp-Fenster': { m2: 480, min: 390 }, 'Festverglasung': { m2: 380, min: 290 }, 'Stulpfenster (2-flügelig)': { m2: 520, min: 690 }, 'Balkontür': { m2: 520, min: 790 }, 'Hebe-Schiebetür': { m2: 980, min: 3900 }, 'Haustür': { m2: 0, min: 2900 }, 'Nebeneingangstür': { m2: 0, min: 1400 } }, farbe_prozent: 12, rollladen: 290, sprossen: 60, insekt: 85, fb_innen_m: 45, fb_aussen_m: 55, montage: 120, demontage: 60, glas: { '3-fach mit Sicherheitsglas (VSG)': 45, 'Schallschutz': 60 } } };
  async function demoSeed() {
    if (await get('kv', 'seeded')) return;
    const el = (label, type, w, h, extra = {}) => ({ id: uid(), label, type, widthMm: w, heightMm: h, widthPoints: [w, w, w], heightPoints: [h, h, h], diagonals: [], installGapMm: 15, opening: 'DIN links', coupling: 'Keine', color: 'RAL 7016 Anthrazit', colorHex: '#3b4148', glass: '3-fach Wärmeschutz', profil: 'Kunststoff 82 mm', rollladen: 'kein', anzahl: 1, colorAussen: '', notiz: '', options: { muntins: false }, ...extra });
    const p1 = { id: uid(), firma_id: 'demo', nummer: 'A-2026-014', status: 'aufmass', kunde: { name: 'Familie Beispiel', adresse: 'Lindenweg 4, 12345 Musterstadt', telefon: '0170 0000000', email: '', notiz: 'Altbau, Laibung innen verputzt' },
      aufmass: { datum: today(), elemente: [el('EG Wohnzimmer links', 'Dreh-Kipp-Fenster', 1230, 1410, { widthPoints: [1232, 1230, 1229], heightPoints: [1410, 1412, 1409], diagonals: [1868, 1871] }), el('EG Wohnzimmer rechts', 'Dreh-Kipp-Fenster', 1230, 1410), el('Terrasse', 'Hebe-Schiebetür', 2980, 2180, { coupling: 'Keine', opening: 'Festverglasung' })] },
      abnahme: {}, created_at: new Date(Date.now() - 2 * 864e5).toISOString(), updated_at: new Date(Date.now() - 864e5).toISOString(), version: 1 };
    const p2 = { id: uid(), firma_id: 'demo', nummer: 'A-2026-009', status: 'montage', kunde: { name: 'Herr Muster', adresse: 'Am Hang 12, 12345 Musterstadt', telefon: '', email: '' },
      aufmass: { datum: today(), elemente: [el('Haustür', 'Haustür', 1100, 2150, { color: 'Eiche', colorHex: '#a8794f', opening: 'DIN rechts' })] }, abnahme: {}, created_at: new Date(Date.now() - 9 * 864e5).toISOString(), updated_at: new Date(Date.now() - 3 * 864e5).toISOString(), version: 1 };
    await put('projekte', p1.id, p1); await put('projekte', p2.id, p2);
    await put('kv', 'service', [{ id: uid(), projekt_id: p2.id, name: 'Herr Muster', email: 'kunde@example.com', telefon: '', nachricht: 'Die Haustür schleift unten leicht, wenn es kalt ist.', status: 'neu', zustaendig: null, notiz: '', created_at: new Date(Date.now() - 36e5).toISOString() }]);
    await put('kv', 'termine', [{ id: uid(), firma_id: 'demo', projekt_id: p2.id, art: 'montage', datum: today(), von: '08:00:00', bis: '12:00:00', titel: '', notiz: 'Haustür mit Seitenteil, Altelement entsorgen', monteure: ['demo-user'], erledigt: false }, { id: uid(), firma_id: 'demo', projekt_id: p1.id, art: 'aufmass', datum: today(), von: '14:00:00', bis: '15:00:00', titel: '', notiz: '', monteure: ['demo-user'], erledigt: false }]);
    await put('kv', 'seeded', 1);
  }

  async function init({ require = true } = {}) {
    if (demo) { await demoSeed(); S.user = { id: 'demo-user', email: 'demo@example.com' }; S.me = { name: 'Demo-Nutzer', rolle: 'inhaber' }; S.rolle = 'inhaber'; S.firma = { ...DEMO_FIRMA, ...((await get('kv', 'firma')) || {}) }; return S; }
    const { data } = await sb.auth.getSession();
    S.user = data.session?.user || null;
    if (!S.user) { if (require) { location.replace('./konto.html?zurueck=' + encodeURIComponent(location.pathname.split('/').pop() + location.hash)); throw new Error('redirect'); } return S; }
    try {
      const { data: m, error } = await sb.from('fb_mitglieder').select('firma_id,rolle,name,email,aktiv').eq('user_id', S.user.id).maybeSingle();
      if (error) throw error;
      if (!m || !m.aktiv) { await sb.auth.signOut(); if (require) { location.replace('./konto.html?fehler=KEIN_TEAM'); throw new Error('redirect'); } S.user = null; return S; }
      S.me = m; S.rolle = m.rolle;
      const { data: f, error: fe } = await sb.from('fb_firmen').select('*').eq('id', m.firma_id).single(); if (fe) throw fe;
      S.firma = f; await put('kv', 'me', { me: m, firma: f, user: { id: S.user.id, email: S.user.email } });
    } catch (e) {
      const c = await get('kv', 'me'); // offline: letzter bekannter Stand
      if (c && c.user?.id === S.user.id) { S.me = c.me; S.rolle = c.me.rolle; S.firma = c.firma; } else throw e;
    }
    return S;
  }
  const abo = () => {
    const f = S.firma || {}, now = Date.now(), paid = f.bezahlt_bis && new Date(f.bezahlt_bis).getTime() > now, trial = f.testphase_bis && new Date(f.testphase_bis).getTime() > now;
    const tage = trial ? Math.ceil((new Date(f.testphase_bis).getTime() - now) / 864e5) : 0;
    return { paid, trial, aktiv: paid || trial, tage, bis: paid ? f.bezahlt_bis : f.testphase_bis };
  };
  const canEdit = () => abo().aktiv;
  const canAdmin = () => ['inhaber', 'buero'].includes(S.rolle);

  /* ---------- Projekte ---------- */
  const FIELDS = 'id,firma_id,nummer,kunde,status,aufmass,abnahme,nacharbeit,abgeschlossen_at,pass_token,kunde_mail_at,bewertung_mail_at,created_at,updated_at,version';
  async function listProjekte() {
    if (demo) return (await all('projekte')).map(([, v]) => v).sort((a, b) => (b.updated_at || '').localeCompare(a.updated_at || ''));
    const pending = new Map((await all('outbox')).filter(([, o]) => o.kind === 'projekt').map(([, o]) => [o.row.id, o.row]));
    try {
      const { data, error } = await sb.from('fb_projekte').select(FIELDS).order('updated_at', { ascending: false }).limit(500); if (error) throw error;
      for (const p of data) await put('projekte', p.id, p);
      const ids = new Set(data.map(p => p.id));
      for (const [k] of await all('projekte')) if (!ids.has(k) && !pending.has(k)) await del('projekte', k);
      return [...data.map(p => pending.get(p.id) || p), ...[...pending.values()].filter(p => !ids.has(p.id))];
    } catch { return (await all('projekte')).map(([, v]) => pending.get(v.id) || v).sort((a, b) => (b.updated_at || '').localeCompare(a.updated_at || '')); }
  }
  async function getProjekt(id) {
    const local = await get('projekte', id), ob = await get('outbox', 'p:' + id);
    if (ob) return ob.row;
    if (demo) return local || null;
    try { const { data, error } = await sb.from('fb_projekte').select(FIELDS).eq('id', id).maybeSingle(); if (error) throw error; if (data) await put('projekte', id, data); return data; } catch { return local || null; }
  }
  function neuesProjekt() {
    return { id: uid(), firma_id: S.firma?.id, nummer: '', status: 'aufmass', kunde: { name: '', adresse: '', telefon: '', email: '', notiz: '' }, aufmass: { datum: today(), elemente: [] }, abnahme: {}, nacharbeit: [], abgeschlossen_at: null, pass_token: null, version: 0, _neu: true };
  }
  async function saveProjekt(p) {
    p.updated_at = new Date().toISOString();
    const row = { id: p.id, firma_id: S.firma.id, nummer: p.nummer || '', kunde: p.kunde, status: p.status, aufmass: p.aufmass, abnahme: p.abnahme, nacharbeit: p.nacharbeit || [], abgeschlossen_at: p.abgeschlossen_at || null };
    if (demo) {
      if (row.abgeschlossen_at && !p.pass_token) { p.pass_token = 'demo-' + uid().replace(/-/g, '').slice(0, 20); p.status = 'abgenommen'; }
      p.version = (p.version || 0) + 1; delete p._neu; await put('projekte', p.id, { ...p }); return p;
    }
    await put('projekte', p.id, { ...p });
    await put('outbox', 'p:' + p.id, { kind: 'projekt', row: { ...p, ...row }, at: Date.now() });
    await flush();
    return (await get('projekte', p.id)) || p;
  }
  async function deleteProjekt(id) {
    if (demo) { await del('projekte', id); return; }
    const { error } = await sb.from('fb_projekte').delete().eq('id', id); if (error) throw error;
    await del('projekte', id); await del('outbox', 'p:' + id);
  }

  /* ---------- Dateien (Fotos, Unterschrift) ---------- */
  async function compress(file, max = 1800, q = .82) {
    const url = URL.createObjectURL(file);
    try {
      const img = await new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = url; });
      const s = Math.min(1, max / Math.max(img.naturalWidth, img.naturalHeight)), c = document.createElement('canvas');
      c.width = Math.round(img.naturalWidth * s); c.height = Math.round(img.naturalHeight * s); c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
      return await new Promise(res => c.toBlob(res, 'image/jpeg', q));
    } finally { URL.revokeObjectURL(url); }
  }
  async function saveFile(projektId, blob, ext = 'jpg') {
    const path = `${S.firma.id}/${projektId}/${uid()}.${ext}`;
    await put('files', path, blob);
    if (!demo) { await put('outbox', 'f:' + path, { kind: 'file', path, type: blob.type || 'image/jpeg', at: Date.now() }); flush(); }
    return path;
  }
  const urlCache = new Map();
  async function fileUrl(path) {
    if (!path) return '';
    if (urlCache.has(path)) return urlCache.get(path);
    const b = await get('files', path);
    if (b) { const u = URL.createObjectURL(b); urlCache.set(path, u); return u; }
    if (demo) return '';
    const { data } = await sb.storage.from('fensterbau').createSignedUrl(path, 3600);
    if (data?.signedUrl) { urlCache.set(path, data.signedUrl); setTimeout(() => urlCache.delete(path), 50 * 6e4); return data.signedUrl; }
    return '';
  }
  async function fileBlob(path) {
    const b = await get('files', path); if (b) return b;
    if (demo || !path) return null;
    const { data } = await sb.storage.from('fensterbau').download(path); return data || null;
  }
  async function removeFile(path) {
    await del('files', path); await del('outbox', 'f:' + path);
    if (!demo) await sb.storage.from('fensterbau').remove([path]).catch(() => {});
  }

  /* ---------- Synchronisierung ---------- */
  let flushing = null;
  function setSync(state, text) { const el = $('#fbSync'); if (!el) return; el.className = 'sync ' + state; el.textContent = text; }
  async function flush() {
    if (demo) return setSync('ok', 'Demo');
    if (flushing) return flushing;
    flushing = (async () => {
      const q = (await all('outbox')).sort((a, b) => (a[1].kind === 'file' ? 0 : 1) - (b[1].kind === 'file' ? 0 : 1) || a[1].at - b[1].at);
      if (!q.length) return setSync('ok', 'Gespeichert');
      if (!navigator.onLine) return setSync('warn', `Offline · ${q.length} vorgemerkt`);
      setSync('', 'Speichert …');
      let failed = 0, lastErr = null;
      for (const [k, o] of q) {
        try {
          if (o.kind === 'file') {
            const b = await get('files', o.path);
            if (b) { const { error } = await sb.storage.from('fensterbau').upload(o.path, b, { contentType: o.type, upsert: true }); if (error && !/exists|Duplicate/i.test(error.message)) throw error; }
            await del('outbox', k);
          } else {
            const r = o.row, row = { id: r.id, firma_id: r.firma_id || S.firma.id, nummer: r.nummer || '', kunde: r.kunde, status: r.status, aufmass: r.aufmass, abnahme: r.abnahme, nacharbeit: r.nacharbeit || [], abgeschlossen_at: r.abgeschlossen_at || null };
            const { data, error } = await sb.from('fb_projekte').upsert(row, { onConflict: 'id' }).select(FIELDS).single();
            if (error) throw error;
            const cur = await get('outbox', k);
            if (cur && cur.at === o.at) await del('outbox', k);
            await put('projekte', data.id, data);
            document.dispatchEvent(new CustomEvent('fb:synced', { detail: data }));
          }
        } catch (e) { failed++; lastErr = e; }
      }
      const left = (await all('outbox')).length;
      if (!left) setSync('ok', 'Gespeichert');
      else if (!navigator.onLine || /fetch|network/i.test(String(lastErr?.message))) setSync('warn', `Offline · ${left} vorgemerkt`);
      else { setSync('warn', `${left} nicht gespeichert`); if (failed) toast(errText(lastErr)); }
    })().finally(() => { flushing = null; });
    return flushing;
  }
  window.addEventListener('online', () => flush());
  window.addEventListener('offline', () => flush());
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') flush(); });

  /* ---------- Kopfzeile ---------- */
  const LOGO = {
    profitar: '<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><path d="M15 30V15h15M70 15h15v15M85 70v15H70M30 85H15V70" stroke="var(--accent)" stroke-width="7" stroke-linecap="round"/><rect x="27" y="27" width="46" height="46" rx="4" stroke="#16a34a" stroke-width="5" stroke-dasharray="7 5"/><path d="M50 27v46M27 50h46" stroke="var(--accent)" stroke-width="4"/></svg>',
    passfort: '<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><path d="M50 10l32 12v24c0 22-14 37-32 44C32 83 18 68 18 46V22z" stroke="var(--accent)" stroke-width="7" stroke-linejoin="round"/><path d="M36 50l10 10 19-21" stroke="#16a34a" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    planung: '<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><rect x="14" y="20" width="72" height="66" rx="9" stroke="var(--accent)" stroke-width="7"/><path d="M14 40h72M34 12v16M66 12v16" stroke="var(--accent)" stroke-width="7" stroke-linecap="round"/><path d="M36 62l9 9 18-18" stroke="#16a34a" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    konto: '<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><rect x="14" y="14" width="72" height="72" rx="10" stroke="var(--accent)" stroke-width="7"/><path d="M50 14v72M14 50h72" stroke="var(--accent)" stroke-width="5"/></svg>'
  };
  function header(app, title, sub) {
    document.documentElement.dataset.app = app;
    const name = { profitar: 'ProFit<span>AR</span>', passfort: 'Pass<span>Fort</span>', konto: 'Fensterbau <span>Konto</span>', planung: 'Montage<span>planung</span>' }[app];
    const el = document.createElement('header'); el.className = 'top';
    el.innerHTML = `<div class="top-in"><a class="brand" href="./${app}.html${location.search.includes('demo=1') ? '?demo=1' : ''}">${LOGO[app]}<div><b>${name}</b><small>${esc(sub || S.firma?.name || title || '')}</small></div></a>
      <div class="grow"></div>
      ${S.user ? `<nav class="switch" aria-label="Apps"><a href="./profitar.html" ${app === 'profitar' ? 'aria-current="page"' : ''}>Aufmaß</a><a href="./passfort.html" ${app === 'passfort' ? 'aria-current="page"' : ''}>Abnahme</a><a href="./planung.html" ${app === 'planung' ? 'aria-current="page"' : ''}>Planung</a><a href="./konto.html" ${app === 'konto' ? 'aria-current="page"' : ''} title="Firma, Team, Abo">Konto</a></nav>
      <span id="fbSync" class="sync" aria-live="polite">…</span>` : ''}</div>`;
    document.body.prepend(el);
    if (S.user) {
      const a = abo(), b = document.createElement('div'); b.className = 'banner';
      if (demo) b.innerHTML = `<div class="info">Demo: Beispieldaten, alles bleibt nur in diesem Browser. <a href="./konto.html?demo=0#registrieren">14 Tage kostenlos testen</a></div>`;
      else if (!a.aktiv) b.innerHTML = `<div class="crit">Testphase bzw. Abo ist abgelaufen – ihr könnt alles ansehen und exportieren, aber nichts mehr ändern. ${S.rolle === 'inhaber' ? '<a href="./konto.html#abo">Tarif wählen</a>' : 'Bitte den Inhaber informieren.'}</div>`;
      else if (a.trial && !a.paid && a.tage <= 5) b.innerHTML = `<div>Testphase endet in ${a.tage} Tag${a.tage === 1 ? '' : 'en'}. ${S.rolle === 'inhaber' ? '<a href="./konto.html#abo">Tarif wählen</a>' : ''}</div>`;
      if (b.innerHTML) el.after(b);
      flush();
    }
    const f = document.createElement('footer'); f.className = 'foot';
    f.innerHTML = `<span>ProFitAR & PassFort · NovaWorks</span><a href="../../impressum.html">Impressum</a><a href="../../datenschutz.html#fensterbau">Datenschutz</a><a href="./agb.html">AGB</a><a href="./avv.html">Auftragsverarbeitung</a>`;
    document.body.append(f);
  }

  /* ---------- PDF (jsPDF mit Noto Sans für Umlaute) ---------- */
  let fontData = null;
  async function pdf(opts) {
    await new Promise(r => { const t = () => window.jspdf ? r() : setTimeout(t, 50); t(); });
    const { jsPDF } = window.jspdf; const doc = new jsPDF(opts || { unit: 'mm', format: 'a4' });
    try {
      fontData ||= Promise.all(['400Regular', '700Bold'].map(w => fetch(`./vendor/notosans-${w}.ttf`).then(r => r.arrayBuffer()).then(b => { let s = ''; const u = new Uint8Array(b); for (let i = 0; i < u.length; i += 32768) s += String.fromCharCode.apply(null, u.subarray(i, i + 32768)); return btoa(s); })));
      const [reg, bold] = await fontData;
      doc.addFileToVFS('NotoSans-Regular.ttf', reg); doc.addFont('NotoSans-Regular.ttf', 'Noto', 'normal');
      doc.addFileToVFS('NotoSans-Bold.ttf', bold); doc.addFont('NotoSans-Bold.ttf', 'Noto', 'bold'); doc.setFont('Noto', 'normal');
    } catch { fontData = null; }
    return doc;
  }
  const blobToDataUrl = b => new Promise((res, rej) => { const r = new FileReader(); r.onload = () => res(r.result); r.onerror = rej; r.readAsDataURL(b); });
  async function sha256(text) { const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)); return [...new Uint8Array(h)].map(x => x.toString(16).padStart(2, '0')).join(''); }
  const passUrl = token => new URL('./pass.html?t=' + encodeURIComponent(token), location.href).href;
  const download = (blob, name) => { const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name; document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 4000); };
  const safeName = s => String(s || '').normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/ß/g, 'ss').replace(/[^\w.-]+/g, '_').replace(/^_+|_+$/g, '').slice(0, 60) || 'Projekt';

  /* ---------- Service-Inbox und Team ---------- */
  async function listService() {
    if (demo) return ((await get('kv', 'service')) || []).sort((a, b) => b.created_at.localeCompare(a.created_at));
    const { data, error } = await sb.from('fb_service').select('*').order('created_at', { ascending: false }).limit(300); if (error) throw error; return data;
  }
  async function updateService(id, patch) {
    if (demo) { const l = (await get('kv', 'service')) || []; const i = l.findIndex(x => x.id === id); if (i >= 0) l[i] = { ...l[i], ...patch }; await put('kv', 'service', l); return; }
    const { error } = await sb.from('fb_service').update(patch).eq('id', id); if (error) throw error;
  }
  async function deleteService(id) {
    if (demo) { await put('kv', 'service', ((await get('kv', 'service')) || []).filter(x => x.id !== id)); return; }
    const { error } = await sb.from('fb_service').delete().eq('id', id); if (error) throw error;
  }
  async function listTeam() {
    if (demo) return [{ user_id: 'demo-user', name: 'Demo-Nutzer', email: 'demo@example.com', rolle: 'inhaber', aktiv: true }];
    const { data, error } = await sb.from('fb_mitglieder').select('user_id,name,email,rolle,aktiv,created_at').order('created_at'); if (error) throw error; return data;
  }
  async function saveFirma(patch) {
    if (demo) { const cur = (await get('kv', 'firma')) || {}; await put('kv', 'firma', { ...cur, ...patch }); Object.assign(S.firma, patch); return; }
    const { data, error } = await sb.from('fb_firmen').update(patch).eq('id', S.firma.id).select('*').single(); if (error) throw error; S.firma = data;
  }
  async function logLines(projektId) {
    if (demo) return [];
    const { data } = await sb.from('fb_log').select('aktion,created_at,user_id').eq('projekt_id', projektId).order('created_at', { ascending: false }).limit(50); return data || [];
  }


  /* ---------- Termine (Montageplanung) und Wartungsliste ---------- */
  async function listTermine(von, bis) {
    if (demo) return ((await get('kv', 'termine')) || []).filter(t => t.datum >= von && t.datum <= bis).sort((a, b) => (a.datum + (a.von || '')).localeCompare(b.datum + (b.von || '')));
    try {
      const { data, error } = await sb.from('fb_termine').select('*').gte('datum', von).lte('datum', bis).order('datum').order('von', { nullsFirst: true }); if (error) throw error;
      await put('kv', 'termine:' + von, data); return data;
    } catch (e) { const c = await get('kv', 'termine:' + von); if (c) return c; throw e; }
  }
  async function saveTermin(t) {
    const row = { id: t.id || uid(), firma_id: S.firma.id, projekt_id: t.projekt_id || null, service_id: t.service_id || null, art: t.art, datum: t.datum, von: t.von || null, bis: t.bis || null, titel: t.titel || '', notiz: t.notiz || '', monteure: t.monteure || [], erledigt: !!t.erledigt };
    if (demo) { const l = (await get('kv', 'termine')) || []; const i = l.findIndex(x => x.id === row.id); if (i >= 0) l[i] = row; else l.push(row); await put('kv', 'termine', l); return row; }
    const { data, error } = await sb.from('fb_termine').upsert(row, { onConflict: 'id' }).select('*').single(); if (error) throw error; return data;
  }
  async function deleteTermin(id) {
    if (demo) { await put('kv', 'termine', ((await get('kv', 'termine')) || []).filter(x => x.id !== id)); return; }
    const { error } = await sb.from('fb_termine').delete().eq('id', id); if (error) throw error;
  }
  async function listWartung() {
    if (demo) return (await get('kv', 'wartung')) || [];
    const { data, error } = await sb.from('fb_wartung').select('id,projekt_id,name,email,intervall_monate,naechste,bestaetigt_at,abgemeldet_at,letzte_mail_at,created_at').order('naechste', { nullsFirst: false }); if (error) throw error; return data;
  }

  /* ---------- Bestellmaß, Preise, Export-Spalten (gemeinsam für Aufmaß, Angebot, Bestellliste) ---------- */
  function bestell(e) {
    const g = +e.installGapMm || 0, w = e.widthPoints || [], h = e.heightPoints || [];
    const B = e.bestellB || (w.length ? Math.min(...w) - 2 * g : 0), H = e.bestellH || (h.length ? Math.min(...h) - 2 * g : 0);
    const how = e.bestellB || e.bestellH ? 'fest eingetragen' : w.length && h.length ? `kleinstes Maß − 2 × ${g} mm Fuge – bitte gegen Herstellervorgabe prüfen` : 'trägt sich ein, sobald Breite und Höhe gemessen sind';
    return { B: B > 0 ? Math.round(B) : 0, H: H > 0 ? Math.round(H) : 0, how };
  }
  const TYPEN = ['Dreh-Kipp-Fenster', 'Festverglasung', 'Stulpfenster (2-flügelig)', 'Kippfenster', 'Balkontür', 'Hebe-Schiebetür', 'Parallel-Schiebe-Kipp-Tür', 'Haustür', 'Nebeneingangstür', 'Rollladen / Sonnenschutz'];
  /* Preisliste: je Typ Preis pro m² (Rahmenaußenmaß) und Mindestpreis; Zuschläge in € bzw. % */
  const PREISE_DEFAULT = { typen: Object.fromEntries(TYPEN.map(t => [t, { m2: 0, min: 0 }])), farbe_prozent: 0, glas: {}, rollladen: 0, sprossen: 0, insekt: 0, fb_innen_m: 0, fb_aussen_m: 0, montage: 0, demontage: 0 };
  const preise = () => { const p = S.firma?.preise || {}; return { ...PREISE_DEFAULT, ...p, typen: { ...PREISE_DEFAULT.typen, ...(p.typen || {}) }, glas: p.glas || {} }; };
  function positionPreis(e, P = preise()) {
    const b = bestell(e), m2 = b.B && b.H ? (b.B / 1000) * (b.H / 1000) : 0, t = P.typen[e.type] || { m2: 0, min: 0 }, teile = [];
    let basis = Math.max(m2 * (+t.m2 || 0), +t.min || 0); if (basis) teile.push(['Element', basis]);
    if (e.colorAussen || !/^Weiß$/.test(e.color || 'Weiß')) { const z = basis * (+P.farbe_prozent || 0) / 100; if (z) teile.push(['Farbe/Dekor', z]); }
    const gz = +(P.glas[e.glass] || 0) * m2; if (gz) teile.push(['Verglasung', gz]);
    if (e.rollladen && !/kein|Bestand/.test(e.rollladen) && +P.rollladen) teile.push(['Rollladen', +P.rollladen]);
    if (e.options?.muntins && +P.sprossen) teile.push(['Sprossen', +P.sprossen]);
    if (e.options?.insekt && +P.insekt) teile.push(['Insektenschutz', +P.insekt]);
    if (e.options?.fbInnen && +P.fb_innen_m) teile.push(['Fensterbank innen', +P.fb_innen_m * (b.B / 1000 || 1)]);
    if (e.options?.fbAussen && +P.fb_aussen_m) teile.push(['Fensterbank außen', +P.fb_aussen_m * (b.B / 1000 || 1)]);
    if (+P.montage) teile.push(['Montage', +P.montage]);
    if (+P.demontage) teile.push(['Ausbau & Entsorgung Altelement', +P.demontage]);
    const einzel = Math.round(teile.reduce((s, [, v]) => s + v, 0) * 100) / 100;
    return { einzel, teile, m2 };
  }
  const eur = n => (Math.round((+n || 0) * 100) / 100).toLocaleString('de-DE', { style: 'currency', currency: 'EUR' });
  const EXPORT_COLS = [
    ['pos', 'Pos', (e, i) => i + 1], ['bez', 'Bezeichnung', e => e.label], ['typ', 'Typ', e => e.type], ['stk', 'Stück', e => e.anzahl || 1],
    ['b', 'Breite (mm)', e => bestell(e).B || ''], ['h', 'Höhe (mm)', e => bestell(e).H || ''], ['oeff', 'Öffnung', e => e.opening], ['kopp', 'Kopplung', e => e.coupling],
    ['profil', 'Profil', e => e.profil], ['fi', 'Farbe innen', e => e.color], ['fa', 'Farbe außen', e => e.colorAussen || e.color], ['glas', 'Verglasung', e => e.glass],
    ['roll', 'Rollladen', e => e.rollladen || 'kein'], ['spr', 'Sprossen', e => e.options?.muntins ? 'ja' : 'nein'], ['ins', 'Insektenschutz', e => e.options?.insekt ? 'ja' : 'nein'],
    ['fbi', 'Fensterbank innen', e => e.options?.fbInnen ? 'ja' : 'nein'], ['fba', 'Fensterbank außen', e => e.options?.fbAussen ? 'ja' : 'nein'],
    ['wp', 'Breite Messpunkte', e => (e.widthPoints || []).join('/')], ['hp', 'Höhe Messpunkte', e => (e.heightPoints || []).join('/')], ['dg', 'Diagonalen', e => (e.diagonals || []).join('/')], ['fuge', 'Fuge (mm)', e => e.installGapMm],
    ['notiz', 'Notiz', e => e.notiz]];
  function exportCols() {
    const cfg = S.firma?.export_spalten;
    if (!cfg?.cols?.length) return EXPORT_COLS.map(([k, n, f]) => ({ k, n, f }));
    return cfg.cols.map(c => { const d = EXPORT_COLS.find(x => x[0] === c.k); return d ? { k: c.k, n: c.n || d[1], f: d[2] } : null; }).filter(Boolean);
  }

  /* ---------- Foto beschriften (Pfeile, Linien, Text) ---------- */
  function annotate(blob) {
    return new Promise(async res => {
      const bm = await createImageBitmap(blob), d = sheet(`<div class="row between"><h2>Foto beschriften</h2><button class="iconbtn" data-close aria-label="Schließen">✕</button></div>
        <div class="seg" id="anT" style="margin:10px 0">${[['pfeil', 'Pfeil'], ['linie', 'Linie'], ['frei', 'Stift'], ['text', 'Text']].map(([k, l], i) => `<button data-t="${k}" aria-pressed="${i === 0}">${l}</button>`).join('')}</div>
        <div class="row" style="margin-bottom:8px">${['#ef4444', '#facc15', '#22c55e', '#ffffff'].map((c, i) => `<button class="iconbtn" data-c="${c}" aria-label="Farbe" style="background:${c};${i === 0 ? 'outline:3px solid var(--accent)' : ''}"></button>`).join('')}<button class="btn ghost sm" id="anU">Rückgängig</button></div>
        <canvas id="anC" style="width:100%;border-radius:10px;touch-action:none;background:#000"></canvas>
        <div class="row" style="margin-top:12px;justify-content:flex-end"><button class="btn ghost" data-close>Abbrechen</button><button class="btn" id="anOk">Übernehmen</button></div>`, () => res(null));
      const c = $('#anC', d.el), x = c.getContext('2d'), sc = Math.min(1, 1600 / Math.max(bm.width, bm.height));
      c.width = Math.round(bm.width * sc); c.height = Math.round(bm.height * sc);
      let tool = 'pfeil', col = '#ef4444', ops = [], cur = null;
      const lw = () => Math.max(4, c.width / 220);
      const redraw = () => { x.drawImage(bm, 0, 0, c.width, c.height); for (const o of [...ops, cur].filter(Boolean)) drawOp(o); };
      const drawOp = o => {
        x.strokeStyle = x.fillStyle = o.col; x.lineWidth = lw(); x.lineCap = 'round'; x.lineJoin = 'round';
        if (o.t === 'frei') { x.beginPath(); o.p.forEach((q, i) => i ? x.lineTo(q.x, q.y) : x.moveTo(q.x, q.y)); x.stroke(); return; }
        if (o.t === 'text') { const fs = Math.max(22, c.width / 28); x.font = `700 ${fs}px Figtree, sans-serif`; x.lineWidth = fs / 6; x.strokeStyle = o.col === '#ffffff' ? '#000' : '#fff'; x.strokeText(o.s, o.a.x, o.a.y); x.fillText(o.s, o.a.x, o.a.y); return; }
        const { a, b: z } = o; x.beginPath(); x.moveTo(a.x, a.y); x.lineTo(z.x, z.y); x.stroke();
        if (o.t === 'pfeil') { const ang = Math.atan2(z.y - a.y, z.x - a.x), h = lw() * 4.5; x.beginPath(); x.moveTo(z.x, z.y); x.lineTo(z.x - h * Math.cos(ang - .45), z.y - h * Math.sin(ang - .45)); x.lineTo(z.x - h * Math.cos(ang + .45), z.y - h * Math.sin(ang + .45)); x.closePath(); x.fill(); }
      };
      const pt = e => { const r = c.getBoundingClientRect(); return { x: (e.clientX - r.left) * c.width / r.width, y: (e.clientY - r.top) * c.height / r.height }; };
      c.onpointerdown = e => { const p = pt(e); if (tool === 'text') { const s = prompt('Text für das Foto:'); if (s) { ops.push({ t: 'text', s: s.slice(0, 60), a: p, col }); redraw(); } return; } cur = tool === 'frei' ? { t: 'frei', p: [p], col } : { t: tool, a: p, b: p, col }; c.setPointerCapture(e.pointerId); };
      c.onpointermove = e => { if (!cur) return; const p = pt(e); if (cur.t === 'frei') cur.p.push(p); else cur.b = p; redraw(); };
      c.onpointerup = () => { if (cur) { ops.push(cur); cur = null; redraw(); } };
      $$('#anT [data-t]', d.el).forEach(b => b.onclick = () => { tool = b.dataset.t; $$('#anT [data-t]', d.el).forEach(y => y.setAttribute('aria-pressed', y === b)); });
      $$('[data-c]', d.el).forEach(b => b.onclick = () => { col = b.dataset.c; $$('[data-c]', d.el).forEach(y => y.style.outline = y === b ? '3px solid var(--accent)' : ''); });
      $('#anU', d.el).onclick = () => { ops.pop(); redraw(); };
      $('#anOk', d.el).onclick = () => c.toBlob(b2 => { const r0 = res; d.el.parentElement.remove(); r0(b2); }, 'image/jpeg', .85);
      redraw();
    });
  }

  if ('serviceWorker' in navigator && !/localhost|127\.0\.0\.1/.test(location.hostname)) navigator.serviceWorker.register('./sw.js').catch(() => {});

  window.FB = { S, sb, demo, VERSION, $, $$, esc, uid, today, fmtDate, fmtDT, errText, toast, sheet, confirmDlg, call, init, abo, canEdit, canAdmin,
    listProjekte, getProjekt, neuesProjekt, saveProjekt, deleteProjekt, compress, saveFile, fileUrl, fileBlob, removeFile, flush, header, pdf, blobToDataUrl, sha256, passUrl, download, safeName,
    listService, updateService, deleteService, listTeam, saveFirma, logLines, listTermine, saveTermin, deleteTermin, listWartung,
    bestell, TYPEN, PREISE_DEFAULT, preise, positionPreis, eur, EXPORT_COLS, exportCols, annotate,
    kv: { get: k => get('kv', k), put: (k, v) => put('kv', k, v) }, DEMO_FIRMA };
})();
