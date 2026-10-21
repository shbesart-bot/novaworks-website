PRODUKT = dict(
    name="AzubiHub", icon="azubihub-icon.jpeg", paper="#f6f8fc", farben="",
    bild="https://novaworks-it.de/azubihub/img/azubi-start.webp",
    cta_url="https://azubihub-app.de/start/", cta="30 Tage kostenlos testen", cta_kurz="Kostenlos testen",
    band_titel="AzubiHub ausprobieren",
    band_text="Digitales Berichtsheft, Rahmenplan, Unterweisungen und Prüfungstraining für Hotels und Gastronomie – 30 Tage kostenlos, ohne Kreditkarte.",
    ratgeber_titel="Ratgeber: Ausbildung in Hotel und Gastronomie",
    ratgeber_beschreibung="Ratgeber für Ausbildungsbetriebe und Azubis in Hotellerie und Gastronomie: digitales Berichtsheft, Ausbildungsberufe seit 2022, Pflicht-Unterweisungen, Onboarding und weniger Ausbildungsabbrüche.",
    ratgeber_lead="Praktische Antworten für Ausbildungsverantwortliche, Hotelleitungen und Azubis – mit Quellen von IHK und Gesetzgeber.",
)

IHK_GERA = ("IHK Ostthüringen: Ausbildungsnachweis (Berichtsheft)", "https://www.ihk.de/gera/ausbildung-weiterbildung/ausbildung/fuer-auszubildende2/ausbildungsnachweise-2976312")
IHK_STGT = ("IHK Region Stuttgart: Berichtsheft", "https://www.ihk.de/stuttgart/fuer-azubis/vertraege/berichtsheft-670862")
BBIG13 = ("Berufsbildungsgesetz § 13 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bbig_2005/__13.html")
BBIG14 = ("Berufsbildungsgesetz § 14 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bbig_2005/__14.html")
BBIG43 = ("Berufsbildungsgesetz § 43 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bbig_2005/__43.html")
IHK_DUS = ("IHK Düsseldorf: Ausbildung im Gastgewerbe modernisiert", "https://www.ihk.de/duesseldorf/ausbildung/aktuelles/ausbildung-im-gastgewerbe-modernisiert-5473140")

SEITEN = [
  dict(datei="digitales-berichtsheft.html", kurz="Digitales Berichtsheft",
    titel="Digitales Berichtsheft: Ist der elektronische Ausbildungsnachweis erlaubt?",
    beschreibung="Digitales Berichtsheft in der Ausbildung: Was das Berufsbildungsgesetz erlaubt, was im Ausbildungsvertrag stehen muss, wie oft abgezeichnet wird und was für die Zulassung zur Abschlussprüfung zählt.",
    lead="Viele Betriebe führen das Berichtsheft noch auf Papier – aus Sorge, dass die IHK eine digitale Version nicht anerkennt. Diese Sorge ist unbegründet: Das Berufsbildungsgesetz erlaubt den elektronischen Ausbildungsnachweis ausdrücklich.",
    kurzantwort="Ja. Nach § 13 Satz 2 Nr. 7 BBiG dürfen Azubis ihren Ausbildungsnachweis schriftlich <em>oder elektronisch</em> führen. Welche Form gilt, steht im Ausbildungsvertrag. Abgezeichnet werden darf ebenfalls elektronisch.",
    abschnitte=[
      ("Was das Gesetz sagt", ["Auszubildende sind verpflichtet, einen Ausbildungsnachweis zu führen. Das Berufsbildungsgesetz nennt dafür zwei gleichwertige Formen: schriftlich oder elektronisch (§ 13 Satz 2 Nr. 7 BBiG). Diese Wahlmöglichkeit gibt es seit der Reform des Berufsbildungsgesetzes 2020.",
        "Der Betrieb muss den Azubis Gelegenheit geben, den Nachweis während der Ausbildungszeit am Arbeitsplatz zu führen, und die nötigen Mittel kostenlos stellen (§ 14 BBiG). Für ein digitales Berichtsheft heißt das: Zugang zu einem Gerät und zur Software, ohne dass der Azubi dafür bezahlen muss."]),
      ("Die Form gehört in den Ausbildungsvertrag", ["Ob schriftlich oder elektronisch geführt wird, wird im Ausbildungsvertrag festgelegt. Wer bei laufenden Verträgen umstellen möchte, spricht das am besten mit der zuständigen IHK ab und hält die Änderung schriftlich fest."]),
      ("Täglich oder wöchentlich?", ["Beides ist möglich. Die IHK Region Stuttgart nennt als Richtwert etwa eine DIN-A4-Seite pro Woche mit knappen Einträgen. Wichtig ist, dass betriebliche Tätigkeiten, Unterweisungen und die Themen der Berufsschule nachvollziehbar sind. Viele Betriebe entscheiden sich für Wochenberichte mit kurzen Stichpunkten je Tag."]),
      ("Prüfen und abzeichnen", ["Ausbildende bzw. Ausbilderinnen und Ausbilder sehen den Nachweis regelmäßig durch. Die IHK Stuttgart nennt mindestens monatlich, viele Kammern empfehlen wöchentlich. Bei elektronischen Nachweisen ist auch die Bestätigung elektronisch möglich, etwa durch eine Freigabe in der Software."]),
      ("Warum das Berichtsheft für die Prüfung zählt", ["Der vollständig geführte Ausbildungsnachweis ist Voraussetzung für die Zulassung zur Abschlussprüfung (§ 43 Abs. 1 Nr. 2 BBiG). Bei der Anmeldung bestätigen Azubi und Betrieb, dass er ordnungsgemäß geführt wurde. Benotet wird der Inhalt nicht – fehlende Wochen kurz vor der Prüfung nachzuschreiben ist aber mühsam und fällt auf."]),
      ("Woran Sie eine gute Lösung erkennen", None, [
        "Azubis schreiben am Handy oder Tablet, auch mit Stichpunkten je Tag",
        "Ausbilder sehen eingereichte Wochen sofort und zeichnen mit einem Tipp ab",
        "Fehlende Wochen fallen auf, bevor sich Lücken anhäufen",
        "Export als PDF für die Anmeldung zur Prüfung",
        "Datenschutz geklärt: Vertrag zur Auftragsverarbeitung, Server in der EU"]),
    ],
    faq=[("Ist ein digitales Berichtsheft bei der IHK zulässig?", "Ja. § 13 Satz 2 Nr. 7 BBiG erlaubt den Ausbildungsnachweis schriftlich oder elektronisch. Die Form wird im Ausbildungsvertrag festgelegt."),
         ("Muss der Ausbilder jede Woche unterschreiben?", "Gesetzlich ist eine regelmäßige Durchsicht vorgeschrieben; Kammern nennen meist wöchentlich bis mindestens monatlich. Elektronisch geführte Nachweise können elektronisch bestätigt werden."),
         ("Darf der Azubi das Berichtsheft während der Arbeitszeit schreiben?", "Ja. Der Betrieb muss Gelegenheit geben, den Nachweis während der Ausbildungszeit am Arbeitsplatz zu führen (§ 14 BBiG)."),
         ("Was passiert, wenn Wochen fehlen?", "Ohne vollständigen Ausbildungsnachweis gibt es keine Zulassung zur Abschlussprüfung. Fehlende Wochen müssen vorher nachgetragen und abgezeichnet werden.")],
    quellen=[BBIG13, BBIG14, BBIG43, IHK_STGT, IHK_GERA],
    hinweis="Dieser Ratgeber ersetzt keine Rechtsberatung. Verbindliche Auskunft gibt Ihre zuständige Kammer."),

  dict(datei="berichtsheft-schreiben-hotel.html", kurz="Berichtsheft schreiben im Hotel",
    titel="Berichtsheft schreiben im Hotel: Tipps und Beispiele für Azubis",
    beschreibung="So schreibst du dein Berichtsheft als Azubi in Hotel und Gastronomie: was rein gehört, Beispiele für Rezeption, Housekeeping, Service und Küche, typische Fehler und wie du keine Woche vergisst.",
    lead="Das Berichtsheft ist für viele Azubis die lästigste Pflicht der Woche. Mit ein paar Regeln geht es in zehn Minuten – und kurz vor der Prüfung musst du nichts nachschreiben.",
    abschnitte=[
      ("Was ins Berichtsheft gehört", None, [
        "Was du im Betrieb gemacht hast – kurz, in Stichpunkten oder ganzen Sätzen",
        "In welcher Abteilung du warst (zum Beispiel Rezeption, Etage, Service, Küche)",
        "Unterweisungen und Schulungen, etwa Hygiene oder Brandschutz",
        "Die Themen aus der Berufsschule",
        "Abwesenheiten wie Urlaub, Krankheit oder Berufsschulblock"]),
      ("Beispiele aus dem Hotelalltag", [
        """  <table class="t"><thead><tr><th>Abteilung</th><th>Zu knapp</th><th>Besser</th></tr></thead><tbody>
    <tr><td>Rezeption</td><td>Check-in gemacht</td><td>Check-in von 12 Gästen, Meldescheine geprüft, Zimmerkarten codiert, Gäste über Frühstückszeiten informiert</td></tr>
    <tr><td>Housekeeping</td><td>Zimmer geputzt</td><td>Abreisezimmer nach Checkliste gereinigt, Minibar kontrolliert und nachgefüllt, Fundsache an der Rezeption gemeldet</td></tr>
    <tr><td>Service</td><td>Frühstück</td><td>Frühstücksbuffet aufgebaut und nachgefüllt, Allergenkennzeichnung kontrolliert, Tische eingedeckt</td></tr>
    <tr><td>Küche</td><td>Gemüse geschnitten</td><td>Mise en place für den Mittagsservice, Gemüse in Brunoise und Julienne geschnitten, Temperaturen der Kühlung dokumentiert</td></tr>
  </tbody></table>
"""]),
      ("Fünf Regeln, die Zeit sparen", None, [
        "<strong>Jeden Tag zwei Stichpunkte</strong> notieren – am Freitag nur noch zusammenfassen",
        "<strong>Fachbegriffe verwenden</strong>, die in der Prüfung vorkommen: Mise en place, Late Check-out, Overbooking, HACCP",
        "<strong>Nicht kopieren:</strong> Wiederholte Tätigkeiten kurz halten und Neues hervorheben",
        "<strong>Was hast du gelernt?</strong> Ein Satz pro Woche reicht und hilft beim Lernen",
        "<strong>Sofort einreichen</strong>, damit dein Ausbilder zeitnah abzeichnen kann"]),
      ("Typische Fehler", None, [
        "Wochen auf Vorrat schreiben oder kurz vor der Prüfung alles nachholen",
        "Namen von Gästen oder private Daten eintragen – das gehört nicht ins Berichtsheft",
        "Berufsschule vergessen: die Themen gehören dazu",
        "Nicht abzeichnen lassen: ohne Bestätigung zählt die Woche nicht"]),
      ("Digital geht es schneller", ["Mit einem digitalen Berichtsheft schreibst du am Handy, siehst sofort, welche Woche noch fehlt, und dein Ausbilder zeichnet mit einem Tipp ab. In AzubiHub zeigt ein farbiger Balken, wie viel Prozent abgeschlossen sind, was gerade geprüft wird und welche Kalenderwochen fehlen."]),
    ],
    faq=[("Wie viel muss ich pro Woche ins Berichtsheft schreiben?", "Als Richtwert nennen Kammern etwa eine DIN-A4-Seite pro Woche mit knappen Einträgen. Wichtig ist, dass deine Tätigkeiten nachvollziehbar sind."),
         ("Darf ich das Berichtsheft in der Arbeitszeit schreiben?", "Ja. Der Betrieb muss dir Gelegenheit geben, den Ausbildungsnachweis während der Ausbildungszeit zu führen."),
         ("Muss die Berufsschule ins Berichtsheft?", "Ja, die Themen aus dem Berufsschulunterricht gehören dazu."),
         ("Wird das Berichtsheft benotet?", "Nein. Es muss aber vollständig und abgezeichnet sein, sonst wirst du nicht zur Abschlussprüfung zugelassen.")],
    band_text="Berichtsheft am Handy schreiben, fehlende Wochen sofort sehen, mit einem Tipp abzeichnen lassen.",
    quellen=[IHK_STGT, BBIG14, BBIG43]),

  dict(datei="ausbildungsberufe-gastgewerbe.html", kurz="Ausbildungsberufe im Gastgewerbe",
    titel="Ausbildungsberufe im Gastgewerbe seit 2022: der Überblick für Betriebe",
    beschreibung="Die sieben Ausbildungsberufe in Hotel und Gastronomie seit 1. August 2022: Hotelfachmann/-frau, Kaufmann/-frau für Hotelmanagement, Restaurants und Veranstaltungsgastronomie, Systemgastronomie, Koch/Köchin und zwei zweijährige Berufe.",
    lead="Seit dem 1. August 2022 gelten im Gastgewerbe neue Ausbildungsordnungen. Berufe wurden umbenannt, die Prüfung umgestellt und neue zweijährige Berufe geschaffen. Hier der Überblick.",
    abschnitte=[
      ("Die sieben Berufe", [
        """  <table class="t"><thead><tr><th>Beruf</th><th>Dauer</th><th>Hinweis</th></tr></thead><tbody>
    <tr><td>Hotelfachmann/-frau</td><td>3 Jahre</td><td>Rezeption, Etage, Service, Veranstaltungen</td></tr>
    <tr><td>Kaufmann/-frau für Hotelmanagement</td><td>3 Jahre</td><td>früher Hotelkaufmann/-frau</td></tr>
    <tr><td>Fachmann/-frau für Restaurants und Veranstaltungsgastronomie</td><td>3 Jahre</td><td>früher Restaurantfachmann/-frau</td></tr>
    <tr><td>Fachmann/-frau für Systemgastronomie</td><td>3 Jahre</td><td></td></tr>
    <tr><td>Koch/Köchin</td><td>3 Jahre</td><td>Vertiefung vegetarische und vegane Küche möglich</td></tr>
    <tr><td>Fachkraft für Gastronomie</td><td>2 Jahre</td><td>Schwerpunkt Restaurantservice oder Systemgastronomie</td></tr>
    <tr><td>Fachkraft Küche</td><td>2 Jahre</td><td>neu seit 2022</td></tr>
  </tbody></table>
""", "Die beiden zweijährigen Berufe sind aus der früheren Fachkraft im Gastgewerbe hervorgegangen."]),
      ("Gestreckte Abschlussprüfung", ["In allen dreijährigen Berufen gibt es statt Zwischen- und Abschlussprüfung eine gestreckte Abschlussprüfung in zwei Teilen. Teil 1 zählt bereits zur Endnote. Für Betriebe heißt das: Die Inhalte der ersten Ausbildungshälfte müssen bis zu Teil 1 sicher sitzen – ein Ausbildungsplan, der das abbildet, wird wichtiger."]),
      ("Durchlässigkeit zwischen den Berufen", ["Nach einem zweijährigen Beruf kann in einem passenden dreijährigen Beruf weitergelernt werden. Wer die Abschlussprüfung im dreijährigen Beruf nicht besteht, kann unter Umständen den zweijährigen Abschluss erhalten."]),
      ("Neue Inhalte", ["Stärker berücksichtigt werden Digitalisierung, Nachhaltigkeit, Verbraucherschutz, Ernährungstrends und Teamarbeit. In den dreijährigen Hotel- und Gastroberufen sind Vertiefungen wie Bar oder Wein möglich."]),
      ("Was Betriebe jetzt tun sollten", None, [
        "Betrieblichen Ausbildungsplan auf die neue Ausbildungsordnung abstimmen",
        "Abteilungswechsel so planen, dass die Inhalte für Teil 1 der Prüfung rechtzeitig vermittelt sind",
        "Lernziele je Abteilung festlegen und den Stand regelmäßig mit den Azubis besprechen",
        "Berichtsheft und Unterweisungen lückenlos dokumentieren"]),
    ],
    faq=[("Gibt es den Restaurantfachmann noch?", "Nein. Seit dem 1. August 2022 heißt der Beruf Fachmann/Fachfrau für Restaurants und Veranstaltungsgastronomie."),
         ("Was ist aus dem Hotelkaufmann geworden?", "Er wurde zum Kaufmann/zur Kauffrau für Hotelmanagement weiterentwickelt."),
         ("Gibt es noch eine Zwischenprüfung?", "In den dreijährigen Berufen nicht mehr. Stattdessen gibt es eine gestreckte Abschlussprüfung in zwei Teilen."),
         ("Für wen gelten die neuen Regeln?", "Für alle Ausbildungsverhältnisse, die seit dem 1. August 2022 begonnen haben.")],
    quellen=[IHK_DUS]),

  dict(datei="unterweisungen-azubis-gastronomie.html", kurz="Pflicht-Unterweisungen",
    titel="Pflicht-Unterweisungen für Azubis in Hotel und Gastronomie",
    beschreibung="Welche Unterweisungen Azubis in Hotellerie und Gastronomie brauchen: Infektionsschutz nach § 43 IfSG, Arbeitsschutz, Jugendarbeitsschutz, Brandschutz und Allergene – mit Fristen und Tipps zur Dokumentation.",
    lead="Unterweisungen schützen Gäste und Team – und sind Pflicht. Gerade bei Azubis, die oft die Abteilung wechseln, geht schnell eine Belehrung unter. Diese Übersicht zeigt die wichtigsten und wie oft sie fällig sind.",
    abschnitte=[
      ("Infektionsschutz (§ 43 IfSG)", ["Wer gewerbsmäßig mit Lebensmitteln arbeitet – in Küche, Service oder am Frühstücksbuffet – braucht vor der ersten Tätigkeit eine Bescheinigung über die Belehrung durch das Gesundheitsamt bzw. einen beauftragten Arzt. Sie darf bei Beginn der Tätigkeit nicht älter als drei Monate sein.",
        "Danach muss der Arbeitgeber die Belehrung nach Aufnahme der Tätigkeit und anschließend <strong>alle zwei Jahre</strong> wiederholen und dokumentieren."]),
      ("Arbeitsschutz", ["Nach dem Arbeitsschutzgesetz (§ 12 ArbSchG) sind Beschäftigte bei der Einstellung, bei neuen Aufgaben oder Arbeitsmitteln und danach regelmäßig zu unterweisen. Die Unfallversicherungsträger verlangen in der Regel mindestens einmal jährlich. Typische Themen im Gastgewerbe: Schneid- und Verbrennungsgefahren, Rutschgefahr, Heben und Tragen, Reinigungsmittel."]),
      ("Jugendliche Azubis", ["Für Azubis unter 18 Jahren gilt zusätzlich das Jugendarbeitsschutzgesetz: Unterweisung über Unfall- und Gesundheitsgefahren vor Beginn der Beschäftigung und danach mindestens halbjährlich (§ 29 JArbSchG). Dazu kommen Regeln zu Arbeitszeiten, Pausen und Nachtarbeit."]),
      ("Weitere übliche Unterweisungen", None, [
        "Brandschutz und Verhalten im Notfall, Fluchtwege, Sammelplatz",
        "Allergenkennzeichnung und Auskunft an Gäste",
        "HACCP und Temperaturkontrollen",
        "Umgang mit Gefahrstoffen, etwa Reinigungs- und Desinfektionsmitteln",
        "Datenschutz an der Rezeption"]),
      ("Dokumentation, die bei einer Kontrolle hält", None, [
        "Thema, Datum, Dauer und Person, die unterwiesen hat",
        "Bestätigung durch die unterwiesene Person",
        "Automatische Erinnerung, wenn eine Wiederholung fällig wird",
        "Übersicht je Azubi, welche Unterweisung offen ist"]),
    ],
    faq=[("Wie oft muss die Belehrung nach § 43 IfSG wiederholt werden?", "Der Arbeitgeber belehrt nach Aufnahme der Tätigkeit und danach alle zwei Jahre. Die Erstbelehrung durch das Gesundheitsamt darf bei Arbeitsbeginn nicht älter als drei Monate sein."),
         ("Wie oft müssen jugendliche Azubis unterwiesen werden?", "Vor Beginn der Beschäftigung und danach mindestens halbjährlich (§ 29 JArbSchG)."),
         ("Reicht eine mündliche Unterweisung?", "Die Unterweisung kann mündlich erfolgen, sollte aber dokumentiert und von der unterwiesenen Person bestätigt werden.")],
    band_text="AzubiHub erinnert an fällige Unterweisungen, lässt sie bestätigen und zeigt je Azubi, was offen ist.",
    quellen=[("Infektionsschutzgesetz § 43 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ifsg/__43.html"),
             ("Arbeitsschutzgesetz § 12 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/arbschg/__12.html"),
             ("Jugendarbeitsschutzgesetz § 29 (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/jarbschg/__29.html")],
    hinweis="Dieser Ratgeber ersetzt keine Rechtsberatung. Branchenspezifische Vorgaben erhalten Sie von Ihrer Berufsgenossenschaft (BGN) und dem Gesundheitsamt."),

  dict(datei="onboarding-azubis-hotel.html", kurz="Onboarding für Azubis",
    titel="Onboarding für Azubis im Hotel: die ersten 30 Tage",
    beschreibung="So gelingt der Ausbildungsstart im Hotel: Vorbereitung vor dem ersten Tag, Pate oder Buddy, Wochenplan für die ersten 30 Tage, Pflicht-Unterweisungen und regelmäßige Feedbackgespräche.",
    lead="Ob Azubis bleiben, entscheidet sich oft in den ersten Wochen. Wer am ersten Tag erwartet wird, eine feste Ansprechperson hat und weiß, was als Nächstes kommt, fühlt sich schneller zugehörig.",
    abschnitte=[
      ("Vor dem ersten Tag", None, [
        "Willkommensnachricht mit Startzeit, Treffpunkt, Ansprechperson und Kleidung",
        "Dienstkleidung, Namensschild, Spind und Zugänge vorbereiten",
        "Paten oder Buddy aus dem Team festlegen",
        "Belehrung nach § 43 IfSG für Tätigkeiten mit Lebensmitteln klären"]),
      ("Woche 1: Ankommen", ["Hausführung, Vorstellung in allen Abteilungen, Sicherheits- und Hygieneunterweisung, die wichtigsten Abläufe der ersten Abteilung. Am Ende der Woche ein kurzes Gespräch: Was war gut, was ist unklar?"]),
      ("Woche 2 bis 4: Mitarbeiten und lernen", ["Feste Aufgaben mit wachsender Verantwortung, erste Einträge im Berichtsheft, Kennenlernen der Berufsschule. Eine Checkliste mit Aufgaben pro Tag hilft Azubi und Pate, nichts zu vergessen."]),
      ("Nach 30 Tagen: Feedbackgespräch", ["Ein strukturiertes Gespräch vor Ende der Probezeit klärt, wie es läuft – in beide Richtungen. Halten Sie Ziele für die nächsten Monate fest und planen Sie den nächsten Abteilungswechsel."]),
      ("Was neue Azubis brauchen", None, [
        "Eine feste Ansprechperson, die wirklich Zeit hat",
        "Klare Erwartungen: Arbeitszeiten, Dienstplan, Berichtsheft",
        "Wissen zum Nachschlagen: Standards, Checklisten, Hauswiki",
        "Rückmeldung, bevor kleine Probleme groß werden"]),
    ],
    faq=[("Wie lange dauert die Probezeit in der Ausbildung?", "Mindestens einen und höchstens vier Monate (§ 20 BBiG)."),
         ("Was ist ein Buddy im Onboarding?", "Eine erfahrene Kollegin oder ein Kollege, der neue Azubis in den ersten Wochen begleitet und bei Alltagsfragen hilft – zusätzlich zur Ausbilderin oder zum Ausbilder."),
         ("Wann sollte das erste Feedbackgespräch stattfinden?", "Ein kurzes Gespräch am Ende der ersten Woche und ein ausführliches vor Ende der Probezeit haben sich bewährt.")],
    band_text="Onboarding-Checkliste mit Buddy, Hauswiki und Pflicht-Unterweisungen – alles in einer App.",
    quellen=[("Berufsbildungsgesetz § 20 – Probezeit (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bbig_2005/__20.html")]),

  dict(datei="ausbildungsabbruch-vermeiden.html", kurz="Ausbildungsabbrüche vermeiden",
    titel="Ausbildungsabbrüche in Hotel und Gastronomie vermeiden: 7 Hebel",
    beschreibung="Fast jeder dritte Ausbildungsvertrag in Deutschland wird vorzeitig gelöst. Sieben Hebel, mit denen Hotels und Restaurants ihre Azubis halten: Onboarding, Ansprechpartner, Feedback, Planbarkeit, Wertschätzung und frühe Warnzeichen.",
    lead="Laut Bundesinstitut für Berufsbildung wurden 2022 bundesweit 29,5 % der Ausbildungsverträge vorzeitig gelöst – ein Höchststand. Das Gastgewerbe ist besonders betroffen. Viele Abbrüche kündigen sich lange vorher an.",
    abschnitte=[
      ("1. Ein guter Start", ["Die meisten Lösungen passieren früh, oft in der Probezeit. Ein vorbereiteter erster Tag, eine feste Ansprechperson und ein Plan für die ersten 30 Tage senken das Risiko deutlich. Mehr dazu im Ratgeber <a href=\"onboarding-azubis-hotel.html\">Onboarding für Azubis</a>."]),
      ("2. Eine Ansprechperson, die Zeit hat", ["Azubis brauchen jemanden, den sie ohne Hemmschwelle fragen können. Wer im Dienstplan dafür Zeit bekommt, kann Probleme früh auffangen."]),
      ("3. Regelmäßiges Feedback", ["Kurze Gespräche alle paar Wochen sind wirksamer als ein großes Jahresgespräch. Halten Sie Vereinbarungen fest und kommen Sie beim nächsten Mal darauf zurück."]),
      ("4. Planbare Dienste", ["Kurzfristige Dienständerungen und Überstunden gehören zu den häufigsten Klagen. Ein früh veröffentlichter Dienstplan und eingehaltene Ruhezeiten zeigen Respekt – bei Minderjährigen gelten zudem die Regeln des Jugendarbeitsschutzgesetzes."]),
      ("5. Ausbildung statt Aushilfe", ["Wer monatelang nur Teller trägt, verliert die Motivation. Ein Ausbildungsplan mit Abteilungswechseln und sichtbaren Lernzielen macht Fortschritt erlebbar."]),
      ("6. Wertschätzung sichtbar machen", ["Ein Lob im Team, eine Urkunde für die bestandene Zwischenetappe, Verantwortung für ein eigenes Projekt – kleine Gesten wirken."]),
      ("7. Warnzeichen früh erkennen", None, [
        "Berichtsheft-Wochen bleiben liegen",
        "Häufigere kurze Krankmeldungen",
        "Rückzug aus dem Team, weniger Nachfragen",
        "Schlechtere Rückmeldungen aus der Berufsschule"]),
    ],
    faq=[("Wie hoch ist die Abbruchquote in der Ausbildung?", "Laut BIBB wurden 2022 bundesweit 29,5 % der Ausbildungsverträge vorzeitig gelöst. Nicht jede Lösung ist ein endgültiger Abbruch – manche Azubis wechseln nur den Betrieb oder Beruf."),
         ("Wann werden die meisten Ausbildungsverträge gelöst?", "Ein großer Teil der Lösungen fällt in das erste Ausbildungsjahr, häufig schon in die Probezeit."),
         ("Was hilft am meisten gegen Ausbildungsabbrüche?", "Ein gut begleiteter Start, eine feste Ansprechperson und regelmäßiges Feedback gehören zu den wirksamsten Hebeln.")],
    band_text="Die AzubiHub-Ampel zeigt fehlende Berichtswochen, Fehltage und offene Unterweisungen je Azubi – damit Warnzeichen früh auffallen.",
    quellen=[("BIBB: Vertragslösungen 2022 auf Höchststand (Pressemitteilung)", "https://www.bibb.de/dokumente/pdf/finalpmvertragsl%c3%b6sungen.pdf")]),
]
