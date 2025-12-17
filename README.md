# 🐾 Animal Website Generator

Ein Python-basiertes Tool, das Tierdaten über eine REST-API abruft und daraus automatisch eine ansprechende, kartenbasierte HTML-Webseite generiert.

## 🚀 Features

* **API-Integration:** Dynamischer Datenabruf von der [API-Ninjas Animals API](https://api-ninjas.com/api/animals).
* **Automatisierte HTML-Generierung:** Verwandelt JSON-Daten in saubere HTML-Komponenten.
* **Template-System:** Nutzt eine Basis-Vorlage (`animals_template.html`), um Design und Logik zu trennen.
* **Sicherheit:** Verwendung von `python-dotenv` zum Schutz des API-Keys.

## 🛠️ Technologien

* **Sprache:** Python 3.x
* **API:** API-Ninjas
* **Libraries:** * `requests` (für HTTP-Anfragen)
    * `python-dotenv` (für das Management von Umgebungsvariablen)

## 📋 Voraussetzungen

Bevor du startest, benötigst du einen API-Key. Registriere dich kostenlos bei [api-ninjas.com](https://api-ninjas.com/) und kopiere deinen Key.

## ⚙️ Installation & Setup

1.  **Repository klonen:**
    ```bash
    git clone [https://github.com/DEIN-USERNAME/PROJEKTNAME.git](https://github.com/DEIN-USERNAME/PROJEKTNAME.git)
    cd PROJEKTNAME
    ```

2.  **Virtuelle Umgebung erstellen (empfohlen):**
    ```bash
    python -m venv .venv
    # Aktivieren (Windows):
    .venv\Scripts\activate
    # Aktivieren (Mac/Linux):
    source .venv/bin/activate
    ```

3.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **API-Key konfigurieren:**
    Erstelle eine Datei namens `.env` im Hauptverzeichnis und füge deinen Key ein:
    ```env
    API_KEY=DEIN_GEHEIMER_API_KEY
    ```

## 💻 Benutzung

Führe das Programm aus und gib den Namen eines Tieres in der Konsole ein.

