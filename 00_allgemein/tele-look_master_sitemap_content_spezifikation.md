# Master-Sitemap & Content-Spezifikation für die neue tele-LOOK Webseite (Agentur-Briefing: antigravity)

Dieses Dokument dient als detaillierte und umfassende Inhaltsangabe sowie als struktureller Leitfaden für die Konzeption und Texterstellung der neuen tele-LOOK Webseite durch die Agentur **antigravity**. Alle aufgeführten Daten, Funktionen, Use Cases und Förderkonditionen sind strikt durch offizielle Quellen und Analysen gedeckt und referenziert.

---

## 1. STRUKTURELLER AUFBAU DER WEBSEITE (SITEMAP)

*   **Page 1: Home (Startseite)** – Der emotionale und pragmatische Einstieg für Service-Entscheider.
*   **Page 2: Features & Technologie** – Die funktionale Tiefe der "App-freien" Kollaboration.
*   **Page 3: Branchen & Use Cases** – Zielgruppenspezifische Landingpages für vertikale Märkte.
*   **Page 4: Business Case & ROI-Rechner** – Harte betriebswirtschaftliche Argumente und Rentabilitätsberechnungen.
*   **Page 5: Service-Monetarisierung** – Wie Support vom Kostenfaktor zum Profitcenter wird.
*   **Page 6: Staatliche Förderungen (Update 2025/2026)** – Der Refinanzierungs-Hebel für KMU.
*   **Page 7: Über uns & Mission** – Historie, Auszeichnungen (KVD-Preis, Freiburger Innovationspreis).
*   **Page 8: Kontakt & Demobuchung** – Direkte Lead-Generierung.

---

## 2. DETAIL-GLIEDERUNG & CONTENT-ARCHITEKTUR (INHALTSANGABE)

### TEIL I: DIE KERNPHILOSOPHIE & LEITPRINZIPIEN (Für die Hero- & Mission-Sektionen)
*   **Das Leitprinzip: "Smart Simplicity"**
    *   Fokus auf das Wesentliche: tele-LOOK ist ein pragmatisches Werkzeug für Macher.
    *   Kein Feature-Overload: Technische Probleme schnell und einfach lösen, ohne langwierige Datenimplementierung oder überladene Menüs.
*   **Das Zero-Barrier-Paradigma (App-Free)**
    *   100 % browserbasierte Kommunikation via WebRTC.
    *   Keine App-Installation, kein Registrierungs- oder Login-Zwang für den Endkunden.
    *   Zugang über einen simplen Einladungs-Link per SMS, E-Mail oder QR-Code.
    *   Beseitigt die "App-Müdigkeit" (App Fatigue) und senkt die Hemmschwelle in akuten Stresssituationen.
*   **Die Definition der Akteure (Rollenverteilung)**
    *   **Der Experte (Service-Geber):** Der tele-LOOK-Kunde (z. B. der Handwerksbetrieb oder das Industrieunternehmen), der die Session am PC steuert.
    *   **Der Service-Nehmer:** Die Person vor Ort an der Anlage – entweder der Endkunde (B2B/B2C) oder ein eigener Mitarbeiter/Azubi, der Remote Mentoring erhält.

---

### TEIL II: DAS TECHNISCHE FUNDAMENT & CORE FEATURES (Für die Feature-Seiten)
*   **Kollaborative Video- & Audiokommunikation**
    *   Echtzeit-Videostreaming in HD-Qualität direkt aus dem mobilen Browser.
    *   Sichere VoIP-Sprachverbindung parallel zum Videobild.
*   **Der "tele-PUNKT" (Augmented-Reality-Live-Zeiger)**
    *   Ein virtueller Cursor, den der Experte per Maus steuert und der in Echtzeit als farbiger Kreis auf dem Kunden-Smartphone erscheint.
    *   Ermöglicht fehlerfreie, präzise Instruktionen im physischen Raum ("Genau dieses Ventil drehen").
*   **HD-Fern-Fotos per Mausklick**
    *   Der Experte kann während des Videostreams hochauflösende Fotos der Anlage erstellen.
    *   Die Fotos sind oft schärfer als das Live-Video und werden ohne störende Metadaten erfasst.
*   **Screensharing & Dokumenten-Einblendung**
    *   Teilen des Bildschirms des Experten (Schaltpläne, Explosionszeichnungen, Handbücher) direkt im Live-Bild des Kunden-Smartphones.
    *   Kein lästiges App-Wechseln für den Kunden nötig.
*   **Remote-Taschenlampe**
    *   Der Experte kann die Smartphone-Taschenlampe des Kunden aus der Ferne aktivieren – ideal für unbeleuchtete Keller oder dunkle Maschinenräume.
*   **API-Schnittstellen & Systemintegration**
    *   Offene REST-APIs ermöglichen die nahtlose bi-direktionale Integration in Branchensoftware und ERP/CRM-Systeme (z. B. pds, KWP, WinWorker, Zoho, Zendesk).
    *   Vermeidung von Medienbrüchen: Automatischer Rückfluss der Protokolle in die digitale Projektakte des Kunden.
*   **Automatisches Service-Protokoll (Der "Proof of Service")**
    *   Jede Sitzung generiert automatisch ein fälschungssicheres PDF-Protokoll mit Gesprächsdauer, HD-Fotos, Notizen und optionaler digitaler Unterschrift des Kunden.
*   **Datensparsamkeit, Sicherheit & DSGVO**
    *   Volle DSGVO-Konformität: Hosting ausschließlich auf zertifizierten deutschen Servern mit 256-Bit-AES-Ende-zu-Ende-Verschlüsselung.
    *   "Privacy by Design": Keine permanente Speicherung fließender Videostreams (Live-Only-Prinzip).
    *   Consent-Workflow: Der Service-Nehmer muss Kamera und Mikrofon vor dem Start aktiv freigeben.
*   **Custom Messaging & Bandbreitenmanagement**
    *   "Branding Light": Individuelle Anpassung des SMS-Textes und des Absendernamens der Einladung an das Firmen-Branding.
    *   Dynamisches Bandbreitenmanagement: Stabil auch bei schlechter Netzabdeckung (Edge/3G) durch Reduzierung der Framerate oder Wechsel in den Foto-Modus.

---

### TEIL III: ABGRENZUNG ZU STANDARD-MESSENGERN (Der IT- & HR-Entscheider-Pitch)
*   **tele-LOOK vs. WhatsApp / FaceTime (Schatten-IT)**
    *   **Mitarbeiterschutz:** Techniker müssen keine privaten Handynummern mehr herausgeben. Einladungen erfolgen über Einmal-Links, was die Privatsphäre schützt und Anrufe am Wochenende oder im Urlaub verhindert.
    *   **Rechtssicherheit:** Die Nutzung von US-Messengern zu gewerblichen Zwecken verletzt in der Regel die DSGVO. tele-LOOK bietet eine rechtssichere, datenschutzkonforme Umgebung.
    *   **Prozessintegrierte Dokumentation:** Bilder landen nicht in der privaten Smartphone-Galerie des Technikers, sondern fließen strukturiert und zentralisiert in die Firmendatenbank.

---

### TEIL IV: BUSINESS CASES, ROI & KPI-METRIKEN (Für kaufmännische Entscheider)
*   **Die Kosten der Ineffizienz ("Windschutzscheiben-Zeit")**
    *   Inhaber und Techniker verbringen täglich unproduktive Stunden auf der Straße für reine Diagnose- oder Besichtigungsfahrten.
*   **Die "Truck Roll"-Reduzierung**
    *   Vermeidung von "No-Fault-Found" (NFF)-Einsätzen, bei denen vor Ort kein echter Fehler vorliegt oder das Problem per einfachem Handgriff (z. B. Reset, Stecker stecken) lösbar gewesen wäre.
    *   Kosten einer Servicefahrt (Fahrzeug, Kraftstoff, Arbeitszeit) betragen durchschnittlich **150 Euro**. tele-LOOK amortisiert sich bereits nach **einer einzigen** vermiedenen Fahrt pro Monat.
*   **Maximierung der First-Time-Fix-Rate (FTFR)**
    *   Visuelle Vorab-Diagnose (Visual Triage): Der Experte identifiziert das exakte Ersatzteil (z. B. über Typenschild-Zoom) vor der Abfahrt.
    *   Der Techniker fährt optimal vorbereitet mit dem passenden Material zum Kunden, was die Zweitanfahrtsquote drastisch senkt.
*   **Der "Stay-Active"- & "Re-Active"-Ansatz (HR-Strategie)**
    *   **Stay-Active:** Körperlich eingeschränkte, ältere Mitarbeiter wechseln vom Außendienst in das Büro und leiten von dort aus jüngere Kollegen im Feld per Video an (Wissenserhalt).
    *   **Re-Active:** Pensionierte Fachkräfte werden als "stille Reserve" stundenweise aus dem Homeoffice für schwierige Spezialdiagnosen zugeschaltet.
*   **Nachhaltigkeit & ESG-Kriterien**
    *   Ein durchschnittlicher physischer Serviceeinsatz verbraucht ca. 1,4 Gallonen Benzin und emittiert **12,5 kg CO₂**.
    *   Bereits die Vermeidung eines Fahrtwegs von nur **300 Metern** entspricht der CO₂-Äquivalenz einer 60-minütigen tele-LOOK Live-Video-Session.
*   **Krisenresilienz & Business Continuity Management (BCM nach ISO 22301)**
    *   Gewährleistung der Handlungsfähigkeit bei unvorhergesehenen Disruptionen (Pandemien, extreme Wetterlagen, Cyberangriffe).
    *   Schutz vor dem "Key Person Risk" durch Dezentralisierung und Digitalisierung des unternehmenseigenen Expertenwissens.

---

### TEIL V: DIE BRANCHENSPEZIFISCHE USE-CASE-DATENBANK (Für vertikale Landingpages)

#### 1. Sektor: Bau- und Ausbauhandwerk (SHK, Elektro, Dach, Holz)
*   **Heizungsbau & Wärmetechnik (SHK):**
    *   *Notdienst-Triage:* Der Notdienst-Meister prüft Störungen (z. B. am Wochenende) vorab visuell. Er leitet Kunden bei Bagatellfehlern (z. B. Wasserdruck füllen, Reset) zur Selbsthilfe an.
    *   *Wärmepumpen-Einstellung:* Werkssupport oder Meister unterstützen den Gesellen vor Ort bei der Justierung komplexer Hydraulik- und Heizkurven.
*   **Sanitärtechnik & Badplanung:**
    *   *Virtuelles Aufmaß:* Der Kunde führt den Planer per Video durch das Badezimmer. Anschlüsse, Maße und Dachschrägen werden für ein erstes Richtpreisangebot erfasst.
    *   *Leckage-Ortung:* Visuelle Vorab-Prüfung, ob es sich um akutes Druckwasser (Haupthahn zu!) oder Kondensat handelt.
*   **Elektrohandwerk & Haus- und Gebäudetechnik:**
    *   *Verteilerkasten-Check:* Kunden unter Anleitung anweisen, gefallene FI-Schalter sicher wieder umzulegen.
    *   *Azubi-Unterstützung:* Live-Prüfung der korrekten Adernbelegung von Patchfeldern bei Netzwerk-Installationen.
    *   *Wallbox-Vorqualifizierung:* Sichtprüfung des Zählerschranks vor Angebotserstellung auf Eignung für E-Mobilität.
*   **Dachdecker & Zimmerer:**
    *   *Sturmschaden-Sichtung:* Dringlichkeit von losen Ziegeln per Live-Video (oder Drohnen-Controller-Display) ohne teures Gerüst/Hubsteiger bewerten.
    *   *Ziegel-Bestimmung:* Exakte Bestimmung von Typ, Farbe und Hersteller des Ziegels direkt auf dem Dach.

#### 2. Sektor: Industrie, Maschinen- und Anlagenbau
*   **Globaler After-Sales-Support (Remote Troubleshooting):**
    *   Maschinenstillstände (Downtime) kosten enorme Summen. Experten aus dem Stammwerk unterstützen lokale Instandhalter weltweit live bei der SPS-Fehlersuche.
*   **Remote Factory Acceptance Tests (R-FAT) & Commissioning:**
    *   Kunden nehmen Maschinen und Anlagen per HD-Videostream virtuell ab, statt kostspielig anzureisen.
    *   Begleitung lokaler Teams bei der physischen Erst-Inbetriebnahme komplexer Großkomponenten.
*   **"Smarte Servicekoffer"-Integration:**
    *   Kooperationen mit Kofferherstellern (z. B. KKC): Auslieferung von Messgeräten oder Ersatzteilen in Koffern, die ab Werk im Deckel einen QR-Code für den direkten tele-LOOK-Support enthalten.
*   **Medizintechnik-Support:**
    *   Wartungsanleitung für hochkomplexe Geräte (CT/MRT) direkt im Krankenhaus. Vorteil: Externe Techniker müssen keine sensiblen Hygienebereiche betreten, Patientendaten verlassen das gesicherte Kliniknetzwerk nicht.
*   **Homecare- & Patienten-Support:**
    *   Sofortige visuelle Hilfestellung für Patienten bei Alarmen an Heimbeatmungs- oder Dialysegeräten zur Vermeidung von Fehlretouren und Angstzuständen.

#### 3. Sektor: Facility Management & Immobilienverwaltung
*   **Bagatell-Filterung & Mieter-Support:**
    *   Mieter meldet "Heizung kalt". Der Hausmeister prüft per Video, ob nur das Thermostat falsch eingestellt ist, bevor ein teurer Fachbetrieb beauftragt wird.
*   **Fremdfirmen-Einweisung:**
    *   Objektleiter lotsen externe Handwerker zielsicher per Video zu den richtigen Technikräumen, Heizkellern oder Absperrventilen.
*   **Qualitäts-Audits im FM (Reinigung & Grünpflege):**
    *   Stichprobenartige Kontrollen der Reinigungsleistung an schwer zugänglichen Stellen oder Dokumentation der Verkehrssicherungspflicht nach Unwettern (z. B. abgebrochene Äste).
*   **Wohnungsübergaben & Schadensaufnahme:**
    *   Fotoprotokollierung von Mängeln bei Mieterwechseln sowie ad-hoc Schadensaufnahme bei akuten Wasserschäden.
*   **Technical Due Diligence (TDD):**
    *   Fachübergreifende visuelle Begutachtung von Gebäudesubstanz und TGA bei Transaktionsprüfungen durch remote zugeschaltete Spezialisten.

#### 4. Sektor: Versicherungswirtschaft (Schadenmanagement)
*   **Ad-hoc Schadensregulierung ("Fast Track"):**
    *   Sofortige Live-Sichtung von Hagel-, Elementar- oder Kfz-Blechschäden direkt über das Smartphone des Versicherten zur Freigabe von Sofortzahlungen.
*   **Betrugsprävention:**
    *   Live-Video-Aufzeichnungen inklusive fälschungssicherer kryptografischer Zeitstempel und Geotagging erschweren Manipulationen im Vergleich zu nachträglich eingereichten statischen Fotos massiv.

#### 5. Sektor: Handel & E-Commerce
*   **Reklamations-Check & Retourenvermeidung:**
    *   Prüfung von Mängelmeldungen an gelieferten Möbeln oder Großgeräten. Unterscheidung zwischen Transportschaden, Produktionsfehler oder Aufbaufehler des Kunden zur Vermeidung extrem teurer Speditionsretouren.
*   **Guided Do-It-Yourself (DIY):**
    *   Neues Geschäftsmodell für Baumärkte: Kunden können sich für 15 Minuten einen Profi-Handwerker per Video zuschalten, der sie live beim Fliesenlegen oder Küchenaufbau anleitet.

#### 6. Sektor: Neue Märkte (Bildung, Veterinär, Nischen)
*   **Remote-Nachhilfe & Hausaufgabenbetreuung (z. B. sofatutor):**
    *   Die Smartphone-Kamera des Schülers filmt von oben das analoge Schulheft. Der Nachhilfelehrer sieht Lösungswege live und zeichnet per Live-Zeiger Korrekturen direkt in das Display des Schülers.
*   **Live-Lese-Coaching bei Legasthenie:**
    *   Das Kind liest aus einem echten, gedruckten Buch vor. Der Lesetherapeut zeichnet live Silbenbögen ein oder schiebt einen virtuellen "Leseschlitz" zur Fokuslenkung über die Textzeilen.
*   **Großtier-Veterinärmedizin:**
    *   Landwirte zeigen Verletzungen von Pferd oder Rind per Video. Der Tierarzt begutachtet die Wunde remote, leitet Erste Hilfe an und spart stundenlange Anfahrten auf Bauernhöfe.
*   **Notfall, Erstversorgung & Betriebssicherheit:**
    *   *Video-Notruf ohne App:* Ersthelfer vor Ort im Betrieb oder Rettungsdienst-Einsatzkräfte leiten ungeschultes Personal per Live-Stream und tele-PUNKT bei Reanimation, Blutstillung oder Erstversorgung an. 100% browserbasiert ohne App-Download.
*   **Digitaler Produktpass (DPP):**
    *   Einhaltung der ab 2026/2028 in Kraft tretenden EU-Bauprodukteverordnung: tele-LOOK dient der mobilen Datenerhebung (Seriennummern scannen, Zustand) am Einbauort sowie als Konformitätsnachweis.

---

### TEIL VI: SERVICE-MONETARISIERUNG (Die Sales-Strategie für Kunden)
*   **Expertise als abrechenbares Produkt ("Paid Remote Support")**
    *   Verwandlung von ehemals unbezahlter, zeitintensiver Telefonberatung in ein eigenständiges, digitales Dienstleistungsprodukt.
*   **Preismodelle & Kundenakzeptanz**
    *   Kunden akzeptieren Fallpauschalen für eine "Digitale Erstdiagnose" (typischerweise zwischen **39 und 59 Euro**, im SHK-Notdienst teils **70 Euro und mehr**) sehr gut.
    *   Der Kunde spart im Gegenzug die deutlich teurere physische Anfahrtspauschale (meist 35 bis 55 Euro) sowie Zeit und Urlaubstage.
*   **Der physische Leistungsnachweis**
    *   Das automatisch erstellte PDF-Sitzungsprotokoll (inklusive HD-Fotos mit Zeitstempel und Notizen) wird dem Kunden als Beleg zugesendet. Dies "materialisiert" die digitale Dienstleistung und legitimiert die gestellte Rechnung transparent.

---

### TEIL VII: STAATLICHE FÖRDERUNGEN 2025/2026 (Der unschlagbare Verkaufshebel)
*   **Der Wandel in der Förderpolitik**
    *   Reine "Ersatzbeschaffungen" (der bloße Austausch alter Laptops/iPads) werden von den Förderstellen konsequent abgelehnt.
    *   Gefördert werden **Prozessinnovationen**. Die Hardware (z. B. robuste Tablets für Monteure) wird dann förderfähig, wenn sie im Digitalisierungsplan als zwingend benötigte "mobile Diagnoseeinheit" für die Nutzung einer innovativen Remote-Service-Software (tele-LOOK) deklariert wird.
*   **Der neue KfW-ERP-Förderkredit Digitalisierung (Kredit Nr. 511/512)**
    *   Eingeführt am 1. Juli 2025, bundesweit verfügbar.
    *   Zinsgünstiges Darlehen (bis zu 25 Mio. Euro pro Vorhaben) gepaart mit einem **ERP-Förderzuschuss / Tilgungszuschuss von bis zu 5 % (maximal 200.000 Euro)**.
    *   **Stufe 1 (Basis):** Keine Zuschüsse, nur Kredite für KMU (vorgeschalteter KfW-Digitalisierungs-Check zwingend).
    *   **Stufe 2 (LevelUp):** Bis zu 3 % Tilgungszuschuss für systematische Datenverwendung, vernetzte ERP/MES-Systeme, IT-Sicherheit und Mitarbeiterweiterbildung.
    *   **Stufe 3 (HighEnd):** Bis zu 5 % Tilgungszuschuss für den Einsatz von Zukunftstechnologien (KI unter Nutzung unternehmensinterner Daten, Big Data).
    *   *Wichtig für tele-LOOK:* Im Rahmen der Basisförderung (Stufe 1a) sind Lizenz- und Servicegebühren explizit förderfähig.
*   **Die BAFA-Unternehmensberatungsförderung**
    *   Zuschüsse für konzeptionelle Beratungen zur Einführung von IT-Systemen. Maximaler bewilligter Beratungszeitraum: 5 Tage.
    *   Förderhöhe: **80 % Zuschuss** (max. 2.800 €) in den neuen Bundesländern, **50 % Zuschuss** (max. 1.750 €) in den alten Bundesländern bei einer maximalen Bemessungsgrundlage von 3.500 Euro.
    *   *Update ab November 2025:* Auch die **Bruttobeträge** (inkl. Umsatzsteuer) sind für nicht vorsteuerabzugsberechtigte Freiberufler, Kleinunternehmer und Solo-Selbstständige voll förderfähig.
*   **Die attraktivsten Landesprogramme im Vergleich (Stand 2026)**
    *   **Bayern (Digitalbonus Bayern):** Richtlinie bis 31.12.2027 gültig. Bietet bis zu 50 % Zuschuss (Standard: max. 7.500 € / Plus mit hohem Innovationsgehalt: max. 30.000 € bzw. 50.000 €). *Wichtig:* Seit Mai 2025 ist die Anmeldung zwingend über ein **ELSTER-Unternehmenskonto** durchzuführen. Das monatliche Budget-Kontingent ist extrem schnell ausgeschöpft.
    *   **NRW (Mittelstand Innovativ & Digital - MID):** Zuschuss bis 50 % (max. 15.000 €) im Baustein *MID-Digitalisierung*. Seit 1. Juli 2025 sind die Bausteine *MID-Analyse* und *MID-Innovation* beendet. Die Vergabe erfolgt monatlich über ein faires **Losverfahren** im NRW.Bank-Kundenportal.
    *   **Hessen (DIGI-Zuschuss):** Bis zu 10.000 Euro Zuschuss (50 % Quote) ab 4.000 Euro Investitionssumme. Vergabe erfolgt ebenfalls über ein wöchentliches **Zufallsauswahlverfahren (Losverfahren)** im Kundenportal der WIBank.
    *   **Sachsen (Digitalisierung Zuschuss EFRE):** Extrem attraktiv durch hohe Quoten. Heranführungsprojekte für Kleinstunternehmen erhalten bis zu 60 % Zuschuss (max. 10.000 €). Transformationsprojekte für mittlere Unternehmen erhalten bis zu 100.000 Euro Zuschuss. Fördert Miet- und SaaS-Kosten explizit für den Durchführungszeitraum.
    *   **Thüringen (Digitalbonus Thüringen):** Bis zu 50 % Zuschuss (max. 15.000 €). *Achtung im Jahr 2026:* Die Richtlinie läuft zwar formal bis Ende 2026, die Mittel sind aktuell jedoch wegen der enormen Nachfrage **vollständig ausgeschöpft**. Alternativ steht das Investitionsprogramm *InnoInvest* zur Verfügung (ab 20.000 € Investition, max. 50.000 € Zuschuss).
*   **Das goldene Gesetz der Förderung**
    *   **Verbot des vorzeitigen Maßnahmebeginns:** Es darf zwingend keine rechtsverbindliche Bestellung der Software, kein Kauf von Hardware und keine Vertragsunterzeichnung (auch nicht mündlich) vor der offiziellen Bewilligung oder dem Erhalt des Zuwendungsbescheids erfolgen.

---

### TEIL VIII: DER IMPLEMENTIERUNGSPLAN FÜR BETRIEBE (Für die Onboarding-Sektion)
*   **Schritt 1: Konzeptionsphase**
    *   Herausfiltern der Kernprozesse (z. B. Notdienst, Erstbesichtigungen), die auf Remote-Support umgestellt werden sollen. Einholen von mindestens drei Vergleichsangeboten für Hard- und Software zur Einreichung bei den Förderstellen.
*   **Schritt 2: Infrastruktur- & Hardware-Check**
    *   Ausstatten der Monteure mit mobilen Datenflats und robusten Endgeräten (Ruggedized Tablets) für den Baustellenalltag.
*   **Schritt 3: Die Pilotphase ("Quick Wins")**
    *   Starten Sie mit einem kleinen, technikaffinen Team, um erste Prozesse zu optimieren und schnelle, motivierende Erfolge im Betrieb sichtbar zu machen.
*   **Schritt 4: Schulung & AGB-Anpassung**
    *   Schulen Sie die Mitarbeiter in technischer Handhabung, gezielter Kundenführung am Telefon ("Kamera ruhig halten") und im rechtssicheren Einholen des mündlichen Einverständnisses vor Bildaufnahmen.
    *   Einarbeitung der neuen "Pay-on-Demand"-Dienstleistungstarife in die Preislisten und Allgemeinen Geschäftsbedingungen (AGB).
