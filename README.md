<!-- ALL-MAINTAINER-BADGE:START - Do not remove or modify this section -->
[![All Maintainer](https://img.shields.io/badge/maintainer-1-red.svg?style=flat-square)](#maintainer-)
<!-- ALL-MAINTAINER-BADGE:END -->

## Maintainer ✨
<!-- ALL-MAINTAINER-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/CaTaNa52"><img src="https://avatars.githubusercontent.com/u/168981162?v=4?s=70" width="70px;" alt="Habib Kilic"/><br /><sub><b>Habib Kilic</b></sub></a><br /> </td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- MAINTAINER:END -->

# SmartSight

SmartSight ist ein innovatives System zur Erkennung von Katzen und deren tierfreundlicher Abwehr. Mithilfe des Raspberry Pi, einer Kamera und OpenCV erkennt das System Katzen und gibt ein hochfrequentes Signal ab, um sie vom Grundstück fernzuhalten.

## Funktionen
- **Katzenerkennung**: Erkennt Katzen mithilfe von Bildverarbeitung (OpenCV).
- **Ultraschall-Abwehr**: Gibt ein hochfrequentes Signal ab, um Katzen zu vertreiben, ohne ihnen zu schaden.
- **Automatisierung**: Läuft vollständig autonom auf einem Raspberry Pi.

## Voraussetzungen
- Raspberry Pi (Zero, 3, 4 oder neuer)
- Raspberry Pi Kamera (oder kompatible USB-Kamera)
- Lautsprecher oder Ultraschall-Generator für die Abwehr
- Installierte Software:
  - Python 3
  - OpenCV
  - NumPy

## Installation
1. Raspberry Pi einrichten und sicherstellen, dass die Kamera aktiviert ist:
   ```bash
   sudo raspi-config

2. Repository klonen:
    ```bash
    git clone https://github.com/CaTaNa52/SmartSight.git
    cd smartsight

3. Abhängigkeiten installieren:
    ```bash
    sudo apt update && sudo apt install python3-pip
    pip3 install -r requirements.txt
    
4. Kamera testen:
    ```bash
    python3 camera_test.py

## Verwendung
1. Programm starten:
    ```bash
    python3 camera_stream.py

2. Das System startet die Katzenerkennung und gibt bei einer Erkennung ein Signal ab.

## Struktur des Projekts
- smartsight.py: Hauptprogramm zur Katzenerkennung und Signalsteuerung.
- kamera_test.py: Testskript für die Kamera.
- requirements.txt: Enthält alle benötigten Python-Pakete.

## Zukunftsplanung
- Verbesserung der Erkennungsgenauigkeit durch ein vortrainiertes Machine-Learning-Modell.
- Integration von Bewegungsmeldern, um Energie zu sparen.
- Speicherung von Bildern und Videos zur späteren Analyse.

# Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der LICENSE-Datei.

