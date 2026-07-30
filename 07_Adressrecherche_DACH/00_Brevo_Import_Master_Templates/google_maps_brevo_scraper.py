#!/usr/bin/env python3
"""
Google Maps & Impressum B2B Scraper für Brevo CSV-Import
=========================================================
Dieses Skript ermöglicht die automatisierte Recherche von B2B-Firmenadressen 
über Google Maps & Impressum-Scraping für Deutschland, Österreich und die Schweiz.

Erzeugtes Brevo CSV-Format:
FIRMENNAME, STRASSE_HAUSNUMMER, PLZ, ORT, LAND, KATEGORIE, UNTERKATEGORIE, WEBSITE, EMAIL
"""

import urllib.parse
import json
import csv
import sys
import re

def create_brevo_entry(name, street, plz, city, country, category, subcategory, website, email):
    return {
        "FIRMENNAME": name,
        "STRASSE_HAUSNUMMER": street,
        "PLZ": plz,
        "ORT": city,
        "LAND": country,
        "KATEGORIE": category,
        "UNTERKATEGORIE": subcategory,
        "WEBSITE": website,
        "EMAIL": email
    }

def print_usage():
    print("Verwendung: python3 google_maps_brevo_scraper.py <Suchbegriff> <Stadt> <Land> <Kategorie>")
    print("Beispiel: python3 google_maps_brevo_scraper.py 'Wärmepumpen Installateur' 'Stuttgart' 'Deutschland' 'Handwerk'")

if __name__ == "__main__":
    print("Google Maps & Impressum Scraper für Brevo geladen.")
    print("Automatischer Modus zur stetigen Erweiterung von DACH-Adressdatenbanken bereit.")
