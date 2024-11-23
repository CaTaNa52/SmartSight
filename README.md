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
