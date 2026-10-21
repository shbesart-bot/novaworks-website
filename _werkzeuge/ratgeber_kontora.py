PRODUKT = dict(
    name="Kontora", icon="kontora-icon.png", paper="#f5f7f4",
    farben="--blue:#247548;--blue-d:#1a5a36;--soft:#e2efe6;--ink:#17344a;--paper:#f5f7f4",
    bild="https://novaworks-it.de/kontora/img/dashboard.webp",
    cta_url="https://mykontora.de/", cta="Kontora kostenlos laden", cta_kurz="Kostenlos laden",
    band_titel="Buchhaltung, die auf Ihrem PC bleibt",
    band_text="Kontora erstellt Rechnungen und E-Rechnungen, liest Belege per Handy und bereitet EÜR und DATEV-Export vor – kostenlos starten, ohne Anmeldung.",
    ratgeber_titel="Ratgeber: Buchhaltung für Selbstständige",
    ratgeber_beschreibung="Ratgeber für Selbstständige und kleine Firmen: E-Rechnungspflicht, XRechnung und ZUGFeRD, Kleinunternehmerregelung, Pflichtangaben auf Rechnungen, Aufbewahrungsfristen und EÜR.",
    ratgeber_lead="Verständliche Antworten auf die häufigsten Fragen rund um Rechnung, Umsatzsteuer und Belege – mit Quellen von IHK, Finanzverwaltung und Gesetzgeber.",
)

IHK_ER = ("IHK Ostthüringen: Übergangsregelungen zur E-Rechnung", "https://www.ihk.de/gera/recht-und-steuern/fokus-erechnung/uebergangsregelung-6246184")
USTDV34A = ("§ 34a UStDV – Rechnungen von Kleinunternehmern (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ustdv_1980/__34a.html")
USTG14 = ("§ 14 UStG – Ausstellung von Rechnungen (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ustg_1980/__14.html")
USTG19 = ("§ 19 UStG – Kleinunternehmer (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ustg_1980/__19.html")
IHK_KU = ("IHK Ostwürttemberg: Kleinunternehmerregelung in der Umsatzsteuer", "https://www.ihk.de/ostwuerttemberg/produktmarken/recht/steuerrecht-neu/kleinunternehmerregelung-in-der-umsatzsteuer-4857380")
IHK_BEG = ("IHK Karlsruhe: 4. Bürokratieentlastungsgesetz – Neuerungen im Steuerrecht", "https://www.ihk.de/karlsruhe/fachthemen/steuerrecht/aktuelles/neuer-inhalt4-buerokratieentlastungsgesetz-6347138")
BMF_ER = ("BMF: Fragen und Antworten zur E-Rechnung", "https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html")
HINWEIS = "Dieser Ratgeber ersetzt keine Steuerberatung. Für Ihren Einzelfall wenden Sie sich an Ihre Steuerberatung oder das Finanzamt."

SEITEN = [
  dict(datei="e-rechnung-kleinunternehmer.html", passend=("E-Rechnung erstellen mit Kontora (XRechnung und ZUGFeRD)", "https://mykontora.de/e-rechnung-erstellen.html"), kurz="E-Rechnung für Kleinunternehmer",
    titel="E-Rechnung für Kleinunternehmer und Selbstständige: Was gilt 2025 bis 2028?",
    beschreibung="E-Rechnungspflicht verständlich: Seit 2025 müssen alle Unternehmen E-Rechnungen empfangen können. Wann Sie selbst E-Rechnungen schreiben müssen, welche Übergangsfristen gelten und warum Kleinunternehmer ausgenommen sind.",
    lead="Seit dem 1. Januar 2025 gilt im Geschäftsverkehr zwischen Unternehmen in Deutschland schrittweise die E-Rechnungspflicht. Für Selbstständige stellen sich zwei Fragen: Muss ich E-Rechnungen empfangen? Und ab wann muss ich selbst welche schreiben?",
    kurzantwort="<strong>Empfangen</strong> müssen seit 1.1.2025 alle Unternehmen können – auch Kleinunternehmer. <strong>Ausstellen</strong> müssen Sie E-Rechnungen an andere Unternehmen spätestens ab 2027 bzw. 2028. Kleinunternehmer nach § 19 UStG sind vom Ausstellen dauerhaft ausgenommen.",
    abschnitte=[
      ("Was ist eine E-Rechnung?", ["Eine E-Rechnung ist eine Rechnung in einem strukturierten, maschinenlesbaren Format nach der europäischen Norm EN 16931 – zum Beispiel XRechnung oder ZUGFeRD in einem geeigneten Profil. Ein PDF per E-Mail ist <em>keine</em> E-Rechnung, sondern eine „sonstige Rechnung“. Mehr zum Unterschied der Formate im Ratgeber <a href=\"xrechnung-zugferd-unterschied.html\">XRechnung oder ZUGFeRD</a>."]),
      ("Die Fristen im Überblick", [
        """  <table class="t"><thead><tr><th>Zeitraum</th><th>Was gilt für Rechnungen an andere Unternehmen (B2B, Inland)</th></tr></thead><tbody>
    <tr><td>seit 1.1.2025</td><td>Alle Unternehmen müssen E-Rechnungen empfangen und verarbeiten können.</td></tr>
    <tr><td>bis 31.12.2026</td><td>Papierrechnungen bleiben erlaubt; PDF und andere Formate, wenn der Empfänger zustimmt.</td></tr>
    <tr><td>bis 31.12.2027</td><td>Verlängerung für Unternehmen mit höchstens 800.000 € Vorjahresumsatz. Auch EDI-Verfahren bleiben bis dahin möglich.</td></tr>
    <tr><td>ab 1.1.2028</td><td>E-Rechnung im Format nach EN 16931 ist Pflicht.</td></tr>
  </tbody></table>
"""]),
      ("Ausnahmen", None, [
        "<strong>Kleinunternehmer nach § 19 UStG</strong> dürfen dauerhaft sonstige Rechnungen schreiben, also Papier oder PDF (§ 34a UStDV)",
        "<strong>Kleinbetragsrechnungen</strong> bis 250 € brutto",
        "<strong>Fahrausweise</strong>",
        "Rechnungen an <strong>Privatkunden</strong> (B2C) sind von der Pflicht nicht betroffen"]),
      ("Was Sie jetzt tun sollten", None, [
        "Eine E-Mail-Adresse für eingehende Rechnungen festlegen",
        "Ein Programm nutzen, das XRechnung und ZUGFeRD lesbar anzeigt und archiviert",
        "Wenn Sie nicht Kleinunternehmer sind: Rechnungssoftware rechtzeitig auf E-Rechnung umstellen",
        "Die E-Rechnung im Originalformat aufbewahren – ein Ausdruck reicht nicht"]),
      ("Empfangen heißt auch: aufbewahren", ["Eine empfangene E-Rechnung ist im Originalformat aufzubewahren, also die XML-Datei bzw. das ZUGFeRD-PDF mit eingebetteter XML. Aufbewahrungsfristen erklärt der Ratgeber <a href=\"aufbewahrungsfristen-belege.html\">Aufbewahrungsfristen für Belege</a>."]),
    ],
    faq=[("Müssen Kleinunternehmer E-Rechnungen empfangen können?", "Ja. Die Empfangspflicht seit 1.1.2025 gilt für alle Unternehmen. Ein E-Mail-Postfach genügt, wenn Sie die Rechnungen lesen und im Original archivieren können."),
         ("Müssen Kleinunternehmer E-Rechnungen schreiben?", "Nein. Nach § 34a UStDV dürfen Kleinunternehmer ihre Rechnungen stets als sonstige Rechnung, also auf Papier oder als PDF, übermitteln."),
         ("Ist ein PDF eine E-Rechnung?", "Nein. Ein reines PDF ist eine sonstige Rechnung. Ein ZUGFeRD-PDF mit eingebetteten Daten nach EN 16931 gilt dagegen als E-Rechnung."),
         ("Gilt die E-Rechnungspflicht für Rechnungen an Privatkunden?", "Nein, sie betrifft nur Umsätze zwischen inländischen Unternehmen.")],
    band_text="Kontora erstellt XRechnung und ZUGFeRD nach EN 16931 und zeigt eingehende E-Rechnungen lesbar an.",
    quellen=[IHK_ER, USTDV34A], hinweis=HINWEIS),

  dict(datei="xrechnung-zugferd-unterschied.html", passend=("E-Rechnung erstellen mit Kontora", "https://mykontora.de/e-rechnung-erstellen.html"), kurz="XRechnung oder ZUGFeRD",
    titel="XRechnung oder ZUGFeRD: Was ist der Unterschied?",
    beschreibung="XRechnung und ZUGFeRD im Vergleich: reines XML gegen PDF mit eingebetteten Daten, welche ZUGFeRD-Profile als E-Rechnung gelten, was Behörden verlangen und welches Format sich für kleine Firmen eignet.",
    lead="Beide Formate erfüllen die E-Rechnungspflicht – sie sehen aber sehr unterschiedlich aus. Für kleine Firmen und Selbstständige ist die Wahl einfacher, als es klingt.",
    abschnitte=[
      ("Die beiden Formate", [
        """  <table class="t"><thead><tr><th></th><th>XRechnung</th><th>ZUGFeRD</th></tr></thead><tbody>
    <tr><td>Aufbau</td><td>reine XML-Datei</td><td>PDF/A-3 mit eingebetteter XML-Datei</td></tr>
    <tr><td>Für Menschen lesbar</td><td>nur mit Programm oder Viewer</td><td>ja, wie ein normales PDF</td></tr>
    <tr><td>Grundlage</td><td>deutsche Ausprägung der EN 16931</td><td>deutsch-französischer Standard (in Frankreich Factur-X)</td></tr>
    <tr><td>Typischer Einsatz</td><td>Rechnungen an Behörden, große Unternehmen</td><td>Rechnungen an Firmen und Kundschaft, die auch ein PDF sehen will</td></tr>
  </tbody></table>
"""]),
      ("Welche ZUGFeRD-Profile zählen?", ["ZUGFeRD gibt es in mehreren Profilen. Die Profile <strong>MINIMUM</strong> und <strong>BASIC WL</strong> enthalten zu wenige Angaben und gelten laut Bundesfinanzministerium nicht als E-Rechnung. Die höheren Profile (BASIC, EN 16931, EXTENDED, XRECHNUNG) erfüllen die Norm. Am verbreitetsten und für die meisten Fälle zu empfehlen ist das Profil <strong>EN 16931</strong> (früher COMFORT)."]),
      ("Rechnungen an Behörden", ["Wer Bund, Länder oder Kommunen beliefert, schickt in der Regel eine XRechnung über das jeweilige Rechnungsportal und braucht dafür die Leitweg-ID der Behörde. Sie steht im Auftrag oder lässt sich bei der Behörde erfragen."]),
      ("Welches Format für kleine Firmen?", ["Für Rechnungen an andere Unternehmen ist ZUGFeRD im Profil EN 16931 meist die bequemste Wahl: Der Empfänger kann sie als PDF lesen und seine Software liest die Daten automatisch aus. Verlangt ein Kunde ausdrücklich XRechnung, schicken Sie XRechnung. Gute Rechnungsprogramme erzeugen beides aus denselben Daten."]),
      ("Typische Fehler", None, [
        "Ein PDF mit „E-Rechnung“ im Dateinamen verschicken – es fehlt die strukturierte Datei",
        "Nur den Ausdruck archivieren statt der Originaldatei",
        "Pflichtangaben fehlen, etwa Leistungsdatum oder Steuernummer, und die Prüfung beim Empfänger schlägt fehl"]),
    ],
    faq=[("Ist ZUGFeRD eine gültige E-Rechnung?", "Ja, in den Profilen ab BASIC aufwärts, empfohlen ist EN 16931. Die Profile MINIMUM und BASIC WL gelten nicht als E-Rechnung."),
         ("Kann ich eine XRechnung ohne Software lesen?", "Nur schwer, da sie eine reine XML-Datei ist. Viele Buchhaltungsprogramme und kostenlose Viewer zeigen sie lesbar an."),
         ("Brauche ich für Behörden immer XRechnung?", "In der Regel ja, zusammen mit der Leitweg-ID der Behörde. Einige Portale akzeptieren auch ZUGFeRD im passenden Profil.")],
    band_text="Kontora erzeugt XRechnung und ZUGFeRD (EN 16931) aus derselben Rechnung und prüft die Pflichtfelder vorher.",
    quellen=[IHK_ER, ("Fonoa: BMF-Schreiben vom 15.10.2024 zur E-Rechnung (englisch)", "https://www.fonoa.com/blog/german-ministry-of-finance-publishes-final-e-invoicing-guidelines")], hinweis=HINWEIS),

  dict(datei="kleinunternehmerregelung.html", passend=("Rechnung als Kleinunternehmer schreiben – so geht es in Kontora", "https://mykontora.de/kleinunternehmer-rechnung.html"), kurz="Kleinunternehmerregelung",
    titel="Kleinunternehmerregelung seit 2025: die Grenzen 25.000 und 100.000 Euro",
    beschreibung="Die Kleinunternehmerregelung nach § 19 UStG seit 2025: neue Umsatzgrenzen 25.000 € und 100.000 € netto, was beim Überschreiten passiert, was für Gründer gilt und welche Angaben auf die Rechnung gehören.",
    lead="Seit dem 1. Januar 2025 gelten für die Kleinunternehmerregelung neue Grenzen – und eine wichtige Änderung beim Überschreiten. Wer keine Umsatzsteuer berechnet, sollte sie kennen.",
    kurzantwort="Kleinunternehmer bleibt, wer im Vorjahr höchstens <strong>25.000 €</strong> und im laufenden Jahr höchstens <strong>100.000 €</strong> netto umsetzt. Wer die 100.000 € überschreitet, ist <em>sofort</em> regelbesteuert – schon für den Umsatz, mit dem die Grenze überschritten wird.",
    abschnitte=[
      ("Die Grenzen seit 2025", [
        """  <table class="t"><thead><tr><th></th><th>bis 2024</th><th>seit 2025</th></tr></thead><tbody>
    <tr><td>Vorjahr</td><td>22.000 € (brutto)</td><td>25.000 € (netto)</td></tr>
    <tr><td>Laufendes Jahr</td><td>Prognose 50.000 € (brutto)</td><td>tatsächlich höchstens 100.000 € (netto)</td></tr>
  </tbody></table>
"""]),
      ("Was beim Überschreiten passiert", ["Überschreitet der Umsatz im laufenden Jahr 100.000 €, endet die Kleinunternehmerregelung sofort. Schon der Umsatz, mit dem die Grenze überschritten wird, unterliegt der Umsatzsteuer. Umsätze davor bleiben steuerfrei. Wer im Vorjahr mehr als 25.000 € umgesetzt hat, ist ab 1. Januar regelbesteuert."]),
      ("Gründer im ersten Jahr", ["Wer neu gründet, kann ohne Prognose als Kleinunternehmer starten. Im Gründungsjahr gilt aber die Grenze von 25.000 €: Wird sie überschritten, endet die Regelung sofort."]),
      ("Was auf die Rechnung gehört", ["Kleinunternehmer weisen keine Umsatzsteuer aus und müssen auf die Steuerbefreiung hinweisen, etwa: „Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.“ Seit 2025 nennt § 34a UStDV vereinfachte Pflichtangaben:"],
        ["Name und Anschrift von Ihnen und dem Kunden",
         "Steuernummer, USt-IdNr. oder Kleinunternehmer-Identifikationsnummer",
         "Ausstellungsdatum",
         "Menge und Art der Lieferung bzw. Umfang und Art der Leistung",
         "Entgelt als Gesamtbetrag und Hinweis auf die Steuerbefreiung"]),
      ("Lohnt sich der Verzicht?", ["Auf die Kleinunternehmerregelung kann man verzichten und ist dann fünf Jahre an die Regelbesteuerung gebunden. Das kann sich lohnen, wenn Sie vor allem an Unternehmen verkaufen und hohe Vorsteuer aus Anschaffungen haben. Für Kundschaft aus dem Privatbereich bleibt die Regelung meist günstiger, weil Ihre Preise ohne Umsatzsteuer niedriger sind."]),
    ],
    faq=[("Wie hoch ist die Umsatzgrenze für Kleinunternehmer 2025?", "Vorjahr höchstens 25.000 € netto, laufendes Jahr höchstens 100.000 € netto."),
         ("Was passiert, wenn ich mitten im Jahr 100.000 € überschreite?", "Die Kleinunternehmerregelung endet sofort. Bereits der Umsatz, mit dem Sie die Grenze überschreiten, ist umsatzsteuerpflichtig."),
         ("Muss ich als Kleinunternehmer eine Rechnungsnummer angeben?", "§ 34a UStDV verlangt sie nicht ausdrücklich. Für eine saubere Buchhaltung und die Zuordnung von Zahlungen sind fortlaufende Nummern trotzdem sehr zu empfehlen."),
         ("Muss ich als Kleinunternehmer E-Rechnungen schreiben?", "Nein, aber Sie müssen E-Rechnungen empfangen können.")],
    band_text="Kontora setzt den Hinweis nach § 19 UStG automatisch auf jede Rechnung und warnt, wenn Sie sich den Umsatzgrenzen nähern.",
    quellen=[IHK_KU, USTG19, USTDV34A], hinweis=HINWEIS),

  dict(datei="rechnung-pflichtangaben.html", passend=("Kostenloses Rechnungsprogramm für Windows", "https://mykontora.de/rechnungsprogramm-kostenlos.html"), kurz="Pflichtangaben auf Rechnungen",
    titel="Rechnung schreiben: alle Pflichtangaben mit Checkliste",
    beschreibung="Welche Angaben eine Rechnung enthalten muss: die Pflichtangaben nach § 14 UStG, Besonderheiten für Kleinbetragsrechnungen bis 250 € und Kleinunternehmer – mit Checkliste zum Abhaken.",
    lead="Fehlt auf einer Rechnung eine Pflichtangabe, kann Ihr Kunde die Vorsteuer nicht abziehen – und fordert eine neue Rechnung. Mit dieser Checkliste passiert das nicht.",
    abschnitte=[
      ("Pflichtangaben nach § 14 Abs. 4 UStG", None, [
        "Vollständiger Name und Anschrift von Ihnen und Ihrem Kunden",
        "Ihre Steuernummer oder Umsatzsteuer-Identifikationsnummer",
        "Ausstellungsdatum",
        "Fortlaufende, einmalige Rechnungsnummer",
        "Menge und Art der Lieferung bzw. Umfang und Art der Leistung",
        "Zeitpunkt der Lieferung oder Leistung (auch als Monat, z. B. „Leistungszeitraum Oktober 2026“)",
        "Nettobetrag, aufgeschlüsselt nach Steuersätzen, und vereinbarte Entgeltminderungen wie Skonto",
        "Steuersatz und Steuerbetrag – oder ein Hinweis auf die Steuerbefreiung"]),
      ("Kleinbetragsrechnungen bis 250 €", ["Für Rechnungen bis 250 € brutto reichen weniger Angaben (§ 33 UStDV): Name und Anschrift des leistenden Unternehmens, Ausstellungsdatum, Menge und Art der Leistung, Bruttobetrag und Steuersatz. Kundendaten und Rechnungsnummer sind nicht nötig."]),
      ("Rechnungen von Kleinunternehmern", ["Kleinunternehmer haben seit 2025 eigene, vereinfachte Pflichtangaben nach § 34a UStDV. Details im Ratgeber <a href=\"kleinunternehmerregelung.html\">Kleinunternehmerregelung</a>."]),
      ("Besondere Hinweise", None, [
        "<strong>Reverse Charge</strong> bei Leistungen an Unternehmen im EU-Ausland: „Steuerschuldnerschaft des Leistungsempfängers“ und die USt-IdNr. beider Seiten",
        "<strong>Gutschrift</strong>: Stellt der Kunde die Rechnung aus, muss das Wort „Gutschrift“ darauf stehen",
        "<strong>Handwerkerleistungen an Privatkunden</strong>: Hinweis auf die Aufbewahrungspflicht des Kunden"]),
      ("Fristen", ["Rechnungen an Unternehmen sind innerhalb von sechs Monaten nach der Leistung auszustellen. Eine falsche Rechnung wird nicht gelöscht, sondern durch eine Rechnungskorrektur oder Stornorechnung mit Bezug auf die ursprüngliche Nummer berichtigt."]),
    ],
    faq=[("Was passiert, wenn eine Pflichtangabe fehlt?", "Der Empfänger darf die Vorsteuer erst abziehen, wenn die Rechnung berichtigt ist. Sie müssen dann eine korrigierte Rechnung ausstellen."),
         ("Muss die Rechnungsnummer lückenlos sein?", "Sie muss fortlaufend und einmalig sein. Mehrere Nummernkreise, etwa je Jahr, sind erlaubt."),
         ("Was ist eine Kleinbetragsrechnung?", "Eine Rechnung bis 250 € brutto. Für sie gelten vereinfachte Pflichtangaben nach § 33 UStDV.")],
    band_text="Kontora prüft Pflichtangaben vor dem Versand, vergibt Rechnungsnummern automatisch und erstellt Korrekturen mit Bezug zur Originalrechnung.",
    quellen=[USTG14, ("§ 33 UStDV – Rechnungen über Kleinbeträge (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ustdv_1980/__33.html"), USTDV34A], hinweis=HINWEIS),

  dict(datei="aufbewahrungsfristen-belege.html", passend=("Buchhaltung ohne Cloud: Belege sicher auf dem eigenen PC", "https://mykontora.de/buchhaltung-ohne-cloud.html"), kurz="Aufbewahrungsfristen für Belege",
    titel="Aufbewahrungsfristen: Belege 8 Jahre, Bücher 10 Jahre",
    beschreibung="Wie lange Selbstständige Rechnungen, Belege und Bücher aufbewahren müssen: 8 Jahre für Buchungsbelege seit dem Bürokratieentlastungsgesetz IV, 10 Jahre für Bücher und Abschlüsse, 6 Jahre für Geschäftsbriefe – und wann die Frist beginnt.",
    lead="Mit dem Vierten Bürokratieentlastungsgesetz wurde die Aufbewahrungsfrist für Buchungsbelege von zehn auf acht Jahre verkürzt. Was das für Rechnungen und Kontoauszüge bedeutet – und was weiter zehn Jahre bleibt.",
    abschnitte=[
      ("Die Fristen im Überblick", [
        """  <table class="t"><thead><tr><th>Unterlage</th><th>Frist</th></tr></thead><tbody>
    <tr><td>Buchungsbelege: Eingangs- und Ausgangsrechnungen, Quittungen, Kontoauszüge</td><td>8 Jahre</td></tr>
    <tr><td>Bücher und Aufzeichnungen, Jahresabschlüsse, Inventare</td><td>10 Jahre</td></tr>
    <tr><td>Empfangene und abgesandte Geschäftsbriefe (z. B. Angebote, Auftragsbestätigungen)</td><td>6 Jahre</td></tr>
  </tbody></table>
""", "Die verkürzte Frist von acht Jahren gilt für Belege, deren Aufbewahrungsfrist beim Inkrafttreten des Gesetzes noch nicht abgelaufen war."]),
      ("Wann beginnt die Frist?", ["Die Frist beginnt mit dem Ende des Kalenderjahres, in dem der Beleg entstanden ist. Eine Rechnung vom März 2026 darf also frühestens nach dem 31.12.2034 vernichtet werden."]),
      ("Digital aufbewahren", ["Digital entstandene Belege – E-Rechnungen, PDF-Rechnungen per E-Mail – müssen im Original digital aufbewahrt werden; ein Ausdruck reicht nicht. Papierbelege dürfen eingescannt und anschließend vernichtet werden, wenn das Scannen nach einem festgelegten Verfahren erfolgt und das Ergebnis unveränderbar gespeichert ist (GoBD)."]),
      ("Ausnahmen beachten", None, [
        "Laufende Betriebsprüfung oder offener Steuerbescheid: Unterlagen bis zum Abschluss aufbewahren",
        "Belege zu Anlagegütern, die noch abgeschrieben werden",
        "Verträge, aus denen noch Ansprüche bestehen"]),
    ],
    faq=[("Wie lange muss ich Rechnungen aufbewahren?", "Rechnungen sind Buchungsbelege und müssen seit dem Bürokratieentlastungsgesetz IV acht Jahre aufbewahrt werden."),
         ("Darf ich Papierbelege nach dem Scannen wegwerfen?", "Ja, wenn das Scannen nach einem festgelegten Verfahren erfolgt und die Datei unveränderbar und lesbar aufbewahrt wird. Ausnahmen gibt es für einzelne Unterlagen wie Zollbelege."),
         ("Wann darf ich Belege aus 2017 vernichten?", "Buchungsbelege aus 2017 haben mit acht Jahren Ablauf Ende 2025 erreicht und dürfen seit 2026 vernichtet werden – sofern keine Ausnahme greift.")],
    band_text="Kontora speichert Belege mit Änderungsprotokoll und täglicher Sicherung und erstellt den GoBD-Export für die Betriebsprüfung.",
    quellen=[IHK_BEG], hinweis=HINWEIS),

  dict(datei="euer-erstellen.html", passend=("EÜR-Software für Selbstständige", "https://mykontora.de/euer-software.html"), kurz="EÜR erstellen",
    titel="EÜR erstellen: Einnahmen-Überschuss-Rechnung Schritt für Schritt",
    beschreibung="Die Einnahmen-Überschuss-Rechnung für Selbstständige erklärt: wer sie erstellen darf, das Zufluss-Abfluss-Prinzip, Abschreibungen und GWG, die Anlage EÜR in ELSTER und typische Fehler.",
    lead="Freiberufler und kleine Gewerbetreibende ermitteln ihren Gewinn meist mit der Einnahmen-Überschuss-Rechnung (EÜR). Das Prinzip ist einfach: Betriebseinnahmen minus Betriebsausgaben. Die Tücken liegen im Detail.",
    abschnitte=[
      ("Wer die EÜR nutzen darf", ["Freiberufler dürfen immer die EÜR nutzen. Gewerbetreibende, solange sie nicht buchführungspflichtig sind – also nicht als Kaufmann ins Handelsregister eingetragen sind und die Grenzen nach § 141 AO nicht überschreiten: seit 2024 mehr als 800.000 € Umsatz oder mehr als 80.000 € Gewinn im Jahr."]),
      ("Zufluss und Abfluss", ["In der EÜR zählt, wann Geld tatsächlich fließt (§ 11 EStG), nicht wann die Rechnung geschrieben wurde. Eine Rechnung vom Dezember, die im Januar bezahlt wird, gehört ins neue Jahr.",
        "Ausnahme sind regelmäßig wiederkehrende Zahlungen wie Miete oder Umsatzsteuer-Vorauszahlungen, die bis zu zehn Tage vor oder nach dem Jahreswechsel fällig und gezahlt werden: Sie zählen zu dem Jahr, zu dem sie wirtschaftlich gehören."]),
      ("Anschaffungen und Abschreibung", None, [
        "<strong>Geringwertige Wirtschaftsgüter</strong> bis 800 € netto können sofort voll abgesetzt werden",
        "Teurere Anschaffungen werden über die Nutzungsdauer abgeschrieben (AfA)",
        "Für Computer und Software gilt eine Nutzungsdauer von einem Jahr",
        "Das Anlagenverzeichnis gehört zur EÜR"]),
      ("Die Anlage EÜR in ELSTER", ["Die EÜR wird mit dem amtlichen Vordruck „Anlage EÜR“ elektronisch über ELSTER übermittelt, zusammen mit der Einkommensteuererklärung. Eine Abgabe auf Papier ist nur in Härtefällen möglich. Aus der Buchhaltung übertragen Sie die Summen je Zeile – eine gute Software ordnet Ihre Buchungen den Zeilen bereits zu."]),
      ("Typische Fehler", None, [
        "Private Ausgaben vermischt, etwa beim Handy- oder Autovertrag ohne Aufteilung",
        "Umsatzsteuer vergessen: Erstattungen vom Finanzamt sind Einnahmen, Zahlungen Ausgaben",
        "Laptop sofort abgesetzt, obwohl er über 800 € netto kostet, oder umgekehrt",
        "Belege fehlen für Bewirtungen und Reisekosten"]),
    ],
    faq=[("Bis wann muss die EÜR abgegeben werden?", "Zusammen mit der Einkommensteuererklärung, ohne Steuerberatung in der Regel bis zum 31. Juli des Folgejahres. Mit Steuerberatung gelten längere Fristen."),
         ("Muss ich die EÜR elektronisch abgeben?", "Ja, die Anlage EÜR ist grundsätzlich elektronisch über ELSTER zu übermitteln."),
         ("Darf ich als Gewerbetreibender eine EÜR machen?", "Ja, solange Sie nicht im Handelsregister als Kaufmann eingetragen sind und unter 800.000 € Umsatz und 80.000 € Gewinn im Jahr bleiben.")],
    band_text="Kontora ordnet Buchungen den Zeilen der Anlage EÜR zu, führt das Anlagenverzeichnis mit AfA und GWG und bereitet alles für ELSTER vor.",
    quellen=[("§ 141 AO – Buchführungspflicht (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ao_1977/__141.html"),
             ("§ 11 EStG – Zufluss und Abfluss (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/estg/__11.html"),
             ("ELSTER – Mein ELSTER", "https://www.elster.de/")], hinweis=HINWEIS),
]
