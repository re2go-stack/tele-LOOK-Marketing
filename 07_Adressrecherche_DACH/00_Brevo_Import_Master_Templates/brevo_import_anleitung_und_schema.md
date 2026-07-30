# Brevo Import Anleitung & CSV-Schema (DACH-Adressrecherche)

> **Zweck:** Anleitung und Feld-Mapping für den direkten CSV-Import von recherchierten B2B-Adressen aus Deutschland (DE), Österreich (AT) und der Schweiz (CH) in **Brevo (ehemals Sendinblue)**.

---

## 1. BREVO FELD-MAPPING (SPALTEN-STRUKTUR)

Damit Brevo die CSV-Dateien ohne manuelles Umbenennen importiert, nutzen wir folgende Spaltenbezeichnungen:

| CSV-Spaltenname | Brevo-Feldtyp | Beispiel-Inhalt | Beschreibung |
| :--- | :--- | :--- | :--- |
| `FIRMENNAME` | Text | `Otte Haustechnik GmbH` | Offizieller Name des Unternehmens |
| `STRASSE_HAUSNUMMER` | Text | `Musterstraße 12` | Straße & Hausnummer des Firmensitzes |
| `PLZ` | Text / Zahl | `89073` | Postleitzahl |
| `ORT` | Text | `Ulm` | Stadt / Gemeinde |
| `LAND` | Text / Code | `Deutschland` (bzw. `DE`, `AT`, `CH`) | Land des Firmensitzes |
| `KATEGORIE` | Text / Attribut | `Handwerk` | Hauptbranche |
| `UNTERKATEGORIE` | Text / Attribut | `SHK` | Spezifisches Gewerk / Nische |
| `WEBSITE` | Text / URL | `https://www.otte-haustechnik.de` | Offizielle Firmenwebseite |
| `EMAIL` | E-Mail (Pflicht) | `info@otte-haustechnik.de` | Allgemeine Firmen-E-Mail (Impressum) |

---

## 2. RECHERTCHE- & RECHTSHINWEISE (DSGVO-KONFORMITÄT)

*   **Öffentliche Firmendaten:** Es werden ausschließlich **öffentlich im Impressum oder in offiziellen Verzeichnissen (HWK, ZVSHK, WKO, Zefix) zugängliche Firmenadressen** und allgemeine E-Mail-Adressen (`info@...`, `kontakt@...`) recherchiert.
*   **B2B-Erstkontakt (Brevo):** Für den Erstkontakt über Brevo empfehlen wir die Verwendung von **Double-Opt-In / Lead-Magneten** (z. B. Zusendung des kostenlosen Förder-Leitfadens oder ROI-Rechners).

---

## 3. IMPORT-SCHRITTE IN BREVO

1. In Brevo auf **Kontakte → Kontakte importieren → Datei hochladen** klicken.
2. Die gewünschte `.csv`-Datei aus den Ordnern `01_Deutschland`, `02_Oesterreich` oder `03_Schweiz` auswählen.
3. Brevo erkennt die Spalten `FIRMENNAME`, `EMAIL`, `PLZ` etc. automatisch.
4. Kontakten das Attribut / Tag der jeweiligen Branche zuweisen (z. B. `SHK_Deutschland_2026`).
