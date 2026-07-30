# 🚀 Multi-Channel Content Expansion Blueprint (tele-LOOK 2026)

Dieser Leitfaden beschreibt das **standardisierte System**, um aus **einem einzelnen Thema / News-Artikel** (z. B. Gesetzgebung, DHZ-Beitrag, Branchen-Trend) ein komplettes Paket für alle tele-LOOK Marketing-Kanäle zu erstellen.

---

## 📁 Ordner-Struktur für ein neues Thema (Beispiel BEG-Förderung)

```text
tele-LOOK Marketing/
├── 01_Social_Media/
│   ├── 01_Linkedin/
│   │   └── YYYY-MM-DD_post-XX_thema_name/
│   │       └── post_content.md              <-- B2B LinkedIn Post
│   └── 02_Instagram/
│       └── YYYY-MM-DD_post-XX_thema_name/
│           └── post_content.md              <-- Instagram Carousel (5-6 Slides Text)
│
├── 03_Presse_und_PR/
│   └── 02_Service_Blog/
│       ├── elementor_html_widget_THEMA.html <-- WordPress Elementor HTML-Widget (Hauptdatei)
│       ├── elementor_full_page_THEMA.html   <-- Vollständige HTML-Datei (Backup & Head)
│       └── YYYY-MM-DD_thema_name.md         <-- Markdown-Version des Beitrags
│
└── 05_SEO_Keywords_und_Google_Push/
    └── 00_GOOGLE_HELPFUL_CONTENT_UND_EEAT_STANDARDS_2026.md <-- Standards & FAQ Disclaimer
```

---

## ⚡ Der 5-Stufen Content-Pipeline Ablauf

Wenn ein neues Thema (z. B. ein Artikel der *Deutschen Handwerks Zeitung* oder eine Gesetzesänderung) reinkommt, erstellen wir immer automatisch folgende **5 Bausteine**:

### 1️⃣ B2B LinkedIn Post (`01_Social_Media/01_Linkedin/`)
* **Format:** Hook -> Problemstellung im Handwerk -> Lösung / Fakten -> Call-to-Action (Link).
* **Tonfall:** Pragmatisch, auf Augenhöhe mit Inhabern & Meistern.

### 2️⃣ Instagram Carousel (`01_Social_Media/02_Instagram/`)
* **Format:** 5 bis 6 Slides (Canva Bulk-Template geeignet).
* **Slide 1:** Catchy Headline + Datum/Quelle.
* **Slide 2-4:** Die wichtigsten Punkte leicht verständlich auf den Punkt gebracht.
* **Slide 5:** CTA ("Speichern & Teilen").

### 3️⃣ Service-Blog HTML-Widget (`03_Presse_und_PR/02_Service_Blog/`)
* **Farben & CSS-Schutz:** Immer isoliert in `#tele-look-main-wrapper` mit `!important` Farbschutz.
* **Bausteine:**
  * Hero-Bereich + E-E-A-T Autor & Review-Badge (*"Fachlich geprüft durch SHK-Meister"*).
  * KPI Bento-Cards (Schnellübersicht).
  * **Erfahrungsbericht aus der Praxis:** Natürlicher Fließtext für Google Helpful Content.
  * Remote-Service Lösung mit **interner Verlinkung** auf `https://www.tele-look.com/web/shk`.
  * Offizielle Links & Hotlines (KfW, BAFA, BMWE).
  * **FAQ mit gesetzlichem Haftungsausschluss-Banner** (tele-LOOK ist kein Beratungsunternehmen).
  * Structured Schema.org JSON-LD `@graph` (Organisation, TechArticle, FAQPage).

### 4️⃣ Rank Math & WordPress SEO-Maske
* **Titel:** `[Hauptthema]: [Sub-Headline] | tele-LOOK`
* **Slug:** `thema-in-kleinbuchstaben-mit-bindestrichen`
* **Meta Description:** Max. 155 Zeichen mit Klarem Nutzen & Aufruf.
* **Tags & Focus Keyword:** Passende Suchbegriffe für das Handwerk.

### 5️⃣ GitHub Versionierung
* Alle Dateien werden automatisch im Haupt-Repository versioniert und synchronisiert.

---

## 🛡️ Pflicht-Regel für alle FAQ-Abschnitte (Disclaimer Rule)

Jede FAQ-Sektion muss zwingend folgenden Disclaimer-Hinweis enthalten:
> ⚠️ **Rechtlicher Hinweis:** tele-LOOK ist ein Softwareanbieter für Live-Video-Support und **kein Energie- oder Rechtsberatungsunternehmen**. Sämtliche Auskünfte zu Förderungen oder Gesetzen sind ohne Gewähr. Verbindliche Entscheidungen obliegen ausschließlich den zuständigen Behörden.
