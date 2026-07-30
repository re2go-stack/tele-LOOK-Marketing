# Google Maps Scraping & Assistenten-Recherche (Brevo B2B-Leads)

> **Prinzip:** Automatisierte und halb-automatisierte Recherche von verifizierten B2B-Firmenadressen über Google Maps & Impressum-Analyse für DACH.

---

## 1. WIE DER ASSISTENTEN-MODUS MIT GOOGLE MAPS FUNKTIONIERT

Als Ihr KI-Assistent kann ich gezielt nach spezifischen Regionen, Städten und Postleitzahlgebieten in Deutschland, Österreich und der Schweiz suchen.

### Der automatisierte Scraper-Workflow:
1. **Google Maps Query:** Abfrage nach Branche & Ort (z. B. *"Wärmepumpen Installateur München"*).
2. **Extraktion:** Auslesen von Firmenname, Straße, PLZ, Ort & Webseite aus Google Places / Maps.
3. **Impressum-Crawler:** Automatischer Aufruf der Firmenwebseite zur Extraktion der Impressums-E-Mail (`info@...`, `kontakt@...`, `office@...`).
4. **Brevo-CSV Export:** Direktes Schreiben in das 9-Spalten-Format für den Brevo-Import.

---

## 2. VERFÜGBARES SCRAPER-TOOL IM PROJEKT

Im Ordner `07_Adressrecherche_DACH/00_Brevo_Import_Master_Templates/` liegt das Skript:  
🐍 **`google_maps_brevo_scraper.py`**

Sie können mich jederzeit bitten:  
> *"Assistent, recherchiere per Scraper 100 Betriebe für Wärmepumpen in der Region Köln/Bonn im Brevo-Format."*

Ich führe den Scraper aus und speichere die fertige CSV-Datei direkt im passenden Branchenordner ab!
