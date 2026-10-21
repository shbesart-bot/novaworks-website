PRODUKT = dict(
    name="GuestFlow", icon="guestflow-icon.png", paper="#f4f7fd",
    farben="--blue:#1c6be0;--blue-d:#1552b3;--soft:#e4eefc;--ink:#101d36;--paper:#f4f7fd",
    bild="https://novaworks-it.de/guestflow/img/gaeste-app.webp",
    cta_url="mailto:info@novaworks-it.de?subject=Demo%20GuestFlow", cta="Demo anfragen", cta_kurz="Demo anfragen",
    band_titel="GuestFlow kennenlernen",
    band_text="Gäste-App, Admin- und Mitarbeiter-Dashboard für Hotels und Restaurants – wir zeigen es Ihnen in einer unverbindlichen Vorführung.",
    ratgeber_titel="Ratgeber: Digitalisierung in Hotel und Restaurant",
    ratgeber_beschreibung="Ratgeber für Hotels und Restaurants: Meldeschein seit 2025, digitaler Check-in, Allergenkennzeichnung, digitale Gästemappe und weniger Anrufe an der Rezeption.",
    ratgeber_lead="Praktische Antworten für Hoteliers, Rezeption und Gastronomie – mit Quellen von IHK und Fachpresse.",
)

IHK_OS = ("IHK Osnabrück: Meldeschein für deutsche Gäste fällt weg", "https://www.ihk.de/osnabrueck/standortpolitik/branchen/tourismusstandort/newsaktuelles-tourismuswirtschaft/abschaffung-meldeschein-6274322")
HAUFE = ("Haufe: Bürokratieentlastungsgesetz IV schafft Meldepflicht für deutsche Gäste ab", "https://www.haufe.de/recht/weitere-rechtsgebiete/wirtschaftsrecht/meldepflicht-in-beherbergungsstaetten_210_639508.html")
BMG29 = ("Bundesmeldegesetz § 29 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bmg/__29.html")
IHK_SN = ("IHK Schwerin: Kennzeichnung von allergenen Stoffen in der Gastronomie", "https://www.ihk.de/schwerin/standort-westmecklenburg/tourismus-und-gastgewerbe/rechtsfragen/kennzeichnung-von-allergenen-stoffen-in-der-gastronomie-6200314")
HINWEIS = "Dieser Ratgeber ersetzt keine Rechtsberatung. Verbindliche Auskunft geben Ihre IHK, die Meldebehörde bzw. die Lebensmittelüberwachung."

SEITEN = [
  dict(datei="meldeschein-hotel.html", kurz="Meldeschein im Hotel",
    titel="Meldeschein im Hotel seit 2025: Was nach dem Wegfall für deutsche Gäste gilt",
    beschreibung="Seit 1. Januar 2025 brauchen deutsche Hotelgäste keinen Meldeschein mehr. Was für ausländische Gäste weiter gilt: Unterschrift, Ausweis, Aufbewahrung 12 Monate, elektronischer Meldeschein – kompakt für Hotels.",
    lead="Mit dem Vierten Bürokratieentlastungsgesetz ist die Hotelmeldepflicht für deutsche Staatsangehörige zum 1. Januar 2025 entfallen. Für Gäste aus dem Ausland bleibt der Meldeschein Pflicht – und viele Betriebe sind unsicher, was genau noch nötig ist.",
    kurzantwort="<strong>Deutsche Gäste:</strong> kein Meldeschein mehr seit 1.1.2025. <strong>Ausländische Gäste:</strong> weiterhin Meldeschein am Anreisetag, gültiger Pass oder Passersatz, Aufbewahrung 12 Monate, danach innerhalb von 3 Monaten löschen.",
    abschnitte=[
      ("Was sich geändert hat", ["Das Bürokratieentlastungsgesetz IV wurde am 29. Oktober 2024 verkündet. Seit dem 1. Januar 2025 müssen Beherbergungsbetriebe für deutsche Gäste keine Meldedaten mehr erheben, speichern oder löschen. Das spart an der Rezeption Zeit und vermeidet Papierstapel."]),
      ("Was für ausländische Gäste weiter gilt", None, [
        "Meldeschein am Tag der Ankunft ausfüllen und handschriftlich unterschreiben lassen",
        "Gültigen, anerkannten Pass oder Passersatz vorlegen lassen",
        "Meldescheine 12 Monate aufbewahren",
        "Danach spätestens innerhalb von 3 Monaten vernichten bzw. löschen",
        "Auf Verlangen bestimmten Behörden (z. B. Polizei, Staatsanwaltschaft) zur Einsicht vorlegen"]),
      ("Elektronischer Meldeschein", ["Statt Papier ist ein elektronischer Meldeschein möglich, wenn der Gast zustimmt. Die Daten werden digital erfasst und der Gast bestätigt am Anreisetag ihre Richtigkeit – zum Beispiel im Zusammenhang mit einer Kartenzahlung, mit der Online-Ausweisfunktion oder durch das Auslesen eines elektronischen Ausweises vor Ort. Die genauen Voraussetzungen stehen in § 29 Bundesmeldegesetz."]),
      ("Kurbeitrag und Bettensteuer nicht vergessen", ["Unabhängig vom Meldegesetz können kommunale Satzungen – etwa zum Kurbeitrag, Gästebeitrag oder zur Übernachtungsteuer – eigene Angaben verlangen. Klären Sie mit Ihrer Gemeinde, welche Daten Sie dafür weiterhin brauchen."]),
      ("So setzen Sie es digital um", None, [
        "Im Check-in-Formular die Staatsangehörigkeit abfragen und nur bei Bedarf die Meldeschein-Felder zeigen",
        "Fristen automatisch überwachen und abgelaufene Meldescheine löschen",
        "Für Behördenanfragen eine Suchfunktion nach Anreisedatum und Name bereithalten",
        "Gäste vorab per App ausfüllen lassen, damit an der Rezeption nur noch die Unterschrift fehlt"]),
    ],
    faq=[("Brauchen deutsche Hotelgäste noch einen Meldeschein?", "Nein. Seit dem 1. Januar 2025 entfällt die Meldepflicht in Beherbergungsstätten für deutsche Staatsangehörige."),
         ("Wie lange muss ein Hotel Meldescheine aufbewahren?", "Zwölf Monate. Danach sind sie spätestens innerhalb von drei Monaten zu vernichten bzw. zu löschen."),
         ("Ist ein digitaler Meldeschein erlaubt?", "Ja, mit Zustimmung des Gastes und wenn die Bestätigung am Anreisetag auf einem der im Bundesmeldegesetz genannten Wege erfolgt, etwa über Kartenzahlung oder elektronischen Ausweis.")],
    band_text="GuestFlow bildet Check-in und Meldeschein digital ab – mit Export der Meldescheine, etwa für Behördenanfragen.",
    quellen=[HAUFE, IHK_OS, BMG29], hinweis=HINWEIS),

  dict(datei="allergenkennzeichnung-restaurant.html", kurz="Allergenkennzeichnung im Restaurant",
    titel="Allergenkennzeichnung im Restaurant: die 14 Allergene richtig angeben",
    beschreibung="Allergene in Restaurant und Hotelküche kennzeichnen: die 14 Hauptallergene nach LMIV, Speisekarte mit Fußnoten oder mündliche Auskunft mit Dokumentation – und wie eine digitale Speisekarte dabei hilft.",
    lead="Auch für lose Ware – also alles, was im Restaurant, am Buffet oder beim Zimmerservice serviert wird – müssen Gäste erfahren können, welche Hauptallergene enthalten sind. Das geht schriftlich oder mündlich, aber nie ohne Dokumentation.",
    abschnitte=[
      ("Die 14 Hauptallergene", [
        """  <table class="t"><tbody>
    <tr><td>Glutenhaltiges Getreide</td><td>Krebstiere</td><td>Eier</td></tr>
    <tr><td>Fisch</td><td>Erdnüsse</td><td>Soja</td></tr>
    <tr><td>Milch (inkl. Laktose)</td><td>Schalenfrüchte (Nüsse)</td><td>Sellerie</td></tr>
    <tr><td>Senf</td><td>Sesam</td><td>Schwefeldioxid und Sulfite</td></tr>
    <tr><td>Lupinen</td><td>Weichtiere</td><td></td></tr>
  </tbody></table>
"""]),
      ("Schriftlich auf der Speisekarte", ["Am einfachsten ist die schriftliche Angabe: direkt beim Gericht oder über Fußnoten bzw. Kennbuchstaben mit einer Legende. Auch eine separate Allergenkarte ist erlaubt, wenn im Restaurant gut sichtbar darauf hingewiesen wird."]),
      ("Mündliche Auskunft – nur mit Dokumentation", None, [
        "Es muss eine schriftliche Dokumentation geben, die Gäste und Lebensmittelkontrolle einsehen können (eine Tabelle mit Kreuzen genügt)",
        "Ein gut sichtbarer Hinweis muss sagen, dass die Information mündlich erhältlich ist und die Dokumentation eingesehen werden kann",
        "Die Auskunft muss vor dem Kauf bzw. vor der Abgabe der Speise erfolgen"]),
      ("Typische Fehlerquellen", None, [
        "Rezept geändert, Allergenliste nicht – zum Beispiel neue Soße mit Senf",
        "Buffet-Schilder fehlen oder passen nicht mehr zum Gericht",
        "Aushilfen kennen die Dokumentation nicht",
        "Zimmerservice- oder Frühstückskarte vergessen"]),
      ("Digitale Speisekarte als Hilfe", ["Wenn Allergene einmal pro Gericht gepflegt werden, erscheinen sie automatisch auf Speisekarte, Buffet-Schild und in der Gäste-App. Gäste können nach Allergenen filtern, und die Küche hat immer den aktuellen Stand als Dokumentation."]),
    ],
    faq=[("Wie viele Allergene müssen im Restaurant gekennzeichnet werden?", "Die 14 Hauptallergene nach Anhang II der Lebensmittelinformationsverordnung (LMIV)."),
         ("Reicht es, wenn das Personal mündlich Auskunft gibt?", "Nur, wenn es zusätzlich eine schriftliche Dokumentation gibt, die eingesehen werden kann, und ein gut sichtbarer Hinweis darauf aufmerksam macht."),
         ("Gilt die Pflicht auch für das Frühstücksbuffet?", "Ja, auch für lose Ware am Buffet müssen die Allergene angegeben oder auf Nachfrage dokumentiert verfügbar sein.")],
    band_text="In GuestFlow pflegen Sie Allergene einmal je Gericht – sichtbar in Speisekarte und Gäste-App.",
    quellen=[IHK_SN], hinweis=HINWEIS),

  dict(datei="digitale-gaestemappe.html", kurz="Digitale Gästemappe",
    titel="Digitale Gästemappe im Hotel: Was rein gehört und wie Gäste sie nutzen",
    beschreibung="Die digitale Gästemappe ersetzt den Ordner auf dem Zimmer: Inhalte, die Gäste wirklich suchen, Mehrsprachigkeit, Aktualität, QR-Code im Zimmer und wie sie Anrufe an der Rezeption reduziert.",
    lead="Die Gästemappe auf dem Zimmer ist oft veraltet, abgegriffen und nur auf Deutsch. Eine digitale Gästemappe auf dem Handy des Gastes ist immer aktuell, mehrsprachig – und beantwortet die Fragen, die sonst an der Rezeption landen.",
    abschnitte=[
      ("Was Gäste am häufigsten suchen", None, [
        "WLAN-Zugang", "Frühstückszeiten und Restaurant-Öffnungszeiten", "Check-out-Zeit und Late Check-out",
        "Parken, Laden von E-Autos, Anreise", "Speisekarte und Zimmerservice", "Ausflugstipps, Wetter und Veranstaltungen",
        "Notfallnummern und Fluchtwege"]),
      ("Vom Zimmer aufs Handy", ["Ein QR-Code im Zimmer, auf der Schlüsselkarte oder in der Buchungsbestätigung öffnet die Gästemappe. Ob als installierte App oder direkt im Browser: Gäste brauchen keine Anmeldung, um die wichtigsten Informationen zu sehen."]),
      ("Mehrsprachig ohne Mehraufwand", ["Wer internationale Gäste hat, sollte die Inhalte mindestens auf Deutsch und Englisch anbieten. Gut gemachte Systeme zeigen die Sprache des Smartphones automatisch an."]),
      ("Aktuell halten", ["Der größte Vorteil gegenüber Papier: Änderungen sind sofort überall sichtbar – geänderte Öffnungszeiten, ein neues Tagesgericht, eine Baustelle vor dem Haus. Legen Sie fest, wer die Inhalte pflegt, und prüfen Sie sie einmal im Monat."]),
      ("Mehr als Information", ["Aus der Gästemappe wird ein Service-Kanal, wenn Gäste direkt bestellen, reservieren oder eine Nachricht an die Rezeption schreiben können. Das entlastet das Telefon und bringt Zusatzumsatz, etwa beim Zimmerservice oder beim Spa."]),
    ],
    faq=[("Müssen Gäste dafür eine App installieren?", "Nicht unbedingt. Viele Lösungen funktionieren über einen QR-Code im Browser; eine App bietet zusätzlich Push-Mitteilungen und Offline-Zugriff."),
         ("Darf die Papiermappe ganz verschwinden?", "Gesetzlich vorgeschriebene Aushänge wie Fluchtwegpläne bleiben. Für alles andere reicht meist ein QR-Code mit kurzem Hinweis."),
         ("Wie oft sollte man die Inhalte prüfen?", "Mindestens monatlich sowie bei jeder Änderung von Öffnungszeiten, Preisen oder Angeboten.")],
    band_text="GuestFlow ist digitale Gästemappe, Zimmerservice und Concierge-Chat in einem – in vier Sprachen."),

  dict(datei="weniger-anrufe-rezeption.html", kurz="Weniger Anrufe an der Rezeption",
    titel="Weniger Anrufe an der Rezeption: 6 Wege, das Front Office zu entlasten",
    beschreibung="Das Telefon an der Rezeption klingelt ständig? Sechs Wege, wie Hotels wiederkehrende Fragen, Bestellungen und Wünsche digital abfangen – ohne den persönlichen Service zu verlieren.",
    lead="Ein großer Teil der Anrufe an der Rezeption dreht sich um immer gleiche Fragen: WLAN, Frühstück, Check-out, Handtücher. Jeder Anruf unterbricht den Check-in des nächsten Gastes. Mit ein paar digitalen Bausteinen bleibt mehr Zeit für das persönliche Gespräch.",
    abschnitte=[
      ("1. Häufige Fragen sichtbar beantworten", ["Sammeln Sie eine Woche lang, wonach gefragt wird. Die zehn häufigsten Antworten gehören prominent in die digitale Gästemappe und in die Buchungsbestätigung."]),
      ("2. Chat statt Telefon", ["Viele Gäste schreiben lieber eine kurze Nachricht als anzurufen. Ein Chat mit der Rezeption lässt sich zwischendurch beantworten – und Übersetzungen helfen bei internationalen Gästen."]),
      ("3. Wünsche direkt erfassen", ["Zusätzliche Handtücher, Weckruf, Taxi: Wenn Gäste solche Wünsche direkt in der App auswählen, landen sie ohne Umweg beim richtigen Team – Housekeeping oder Rezeption."]),
      ("4. Zimmerservice digital bestellen", ["Eine Speisekarte mit Bestellfunktion spart Telefonate und Missverständnisse. Die Küche sieht die Bestellung sofort, der Gast den Status."]),
      ("5. Digitaler Check-in", ["Wenn Gäste ihre Daten vorab erfassen, verkürzt sich der Check-in. Seit 2025 entfällt zudem der Meldeschein für deutsche Gäste – mehr dazu im Ratgeber <a href=\"meldeschein-hotel.html\">Meldeschein im Hotel</a>."]),
      ("6. Notfälle trotzdem sofort erreichen", ["Für echte Notfälle muss der schnelle Weg bleiben: eine Notrufnummer und ein SOS-Knopf in der App, der sofort beim Personal ankommt."]),
    ],
    faq=[("Wirkt eine Hotel-App unpersönlich?", "Nicht, wenn sie Routinefragen übernimmt und so mehr Zeit für das persönliche Gespräch an der Rezeption lässt."),
         ("Welche Fragen eignen sich für digitale Antworten?", "Wiederkehrende Informationen wie WLAN, Zeiten, Anreise, Parken und Speisekarte sowie einfache Wünsche wie Handtücher oder Weckruf."),
         ("Was ist mit Gästen ohne Smartphone?", "Telefon und Rezeption bleiben selbstverständlich erreichbar – die digitalen Wege sind ein Angebot, kein Zwang.")],
    band_text="GuestFlow: Concierge-Chat, Zimmerservice, Wünsche und SOS-Knopf – weniger Anrufe, zufriedenere Gäste."),
]
