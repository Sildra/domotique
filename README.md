

# Préface

Ce document a pour but de centraliser les connaissances sur la maintenance de la domotique installée par Bouygues dans le cadre de Flexom.
Avec la fin du service Flexom et la reprise par Building Care de la maintenance du système, une réflexion sur les alternatives a été amorcée.


## Technologies

* EnOcean : Protocole open-source en perte de vitesse.
* Zigbee : Protocole open-source supporté par une large variété d'équipements.
* RTS : Protocole propriétaire Somfy utilisé par le thermostat.
* IO : Protocole propriétaire Somfy utilisé par les volets roulants.

| Technologie | Interopérabilité | Confiance pour une migration | Note                                                  |
| ----------- | ---------------- | ---------------------------- | ----------------------------------------------------- |
| EnOcean     | ★★★★        | ★★★★                    |                                                       |
| Zigbee      | ★★★★★        | ★★★★★                    | Nouveaux équipements uniquement                       |
| RTS         | ★        | ★★★                    | Le remplacement total du thermostat est moins onéreux | 
| IO          | ☆        | ☆                    | Aucune garantie de compatibilité                      |

<div style="page-break-after: always;"></div>

## Equipements

| Equipement           | Flexom                           | Building Care | Remplacement (exemples)       |
| -------------------- | -------------------------------- | ------------- | ----------------------------- |
| Système domotique    | Hattara Din Rail (IO, EnOcean)   | ?             | Raspberry PI + dongle USB 300 |
| Interrupteur         | Vimar Plana VITA1001 et VITA1002 | ?             | Interrupteur générique        |
| Eclairage            | Ubiwizz Eclairage EnOcean        | ?             | NodOn Eclairage               |
| Volet Roulant        | Somfy IO ?                       | ?             | NodOn Chauffage               |
| Thermostat           | Somfy Thermostat 5117427A        | ?             | NodOn Capteur de temperature  |
| Fil Pilote chauffage | Somfy Home Motion 5117322A       | ?             | NodOn Fil pilote              |

![Flexom](img/Flexom.dot.svg#gh-light-mode-only)
![Flexom](img/Flexom-dark.dot.svg#gh-dark-mode-only)


<div style="page-break-after: always;"></div>

# Remplacement vers un système open-source

## Références de prix

| Equipement           | Remplacement                 | Prix    | Notes                                  |
| -------------------- | ---------------------------- | ------- | -------------------------------------- |
| Système domotique    | Raspberry Pi + SD + chargeur | 80€     |                                        |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€     |                                        |
| Pont Zigbee          | SONOFF dongle Zigbee         | 25€     |                                        |
| Pont RTS             | Somfy Tahoma switch          | 200€    | Si non-remplacement du thermostat      |
| Pont IO              | Somfy Tahoma switch          | 200€    | Potentiellement impossible à connecter |
| Interrupteur         | Vimar Plana                  | ~65€    |                                        |
| Eclairage            | NodOn Eclairage              | 62€/45€ | EnOcean/Zigbee                         |
| Volet Roulant        | NodOn Volet Roulant          | 57€/45€ | EnOcean/Zigbee                         |
| Thermostat           | NodOn Capteur de temperature | 55€/50€ | EnOcean/Zigbee                         |
| Thermostat           | SONOFF SNZB-02D              | 20€     | Alternative Zigbee                     |
| Fil Pilote chauffage | NodOn Fil pilote             | 55€/47€ | EnOcean/Zigbee                         |

<div style="page-break-after: always;"></div>

## Solutions

| Solution       | Interopérabilité | Facilité de migration | Cout      | Note                                           |
| -------------- | ---------------- | --------------------- | --------- | ---------------------------------------------- |
| Building Care  | ★        | ★★★★★             | ☆ | 100€/an + tributaire de Building Care          |
| Sans domotique | ☆        | ★★★★★             | ★★★★★ | Remplacement des équipements au fil des pannes |
| Minimale       | ★★★★        | ★★★             | ★★★ | Possiblement impossible                        |
| EnOcean        | ★★★★        | ★★             | ★ |                                                |
| Mixte          | ★★★★★        | ★★             | ★★ |                                                |

<div style="page-break-after: always;"></div>

### Solution sans domotique

![Sans domotique](img/SansDomotique.dot.svg#gh-light-mode-only)
![Sans domotique](img/SansDomotique-dark.dot.svg#gh-dark-mode-only)

#### Evaluation des couts

| Equipement           | Remplacement                 | Cout  | Quantité | Total |
| -------------------- | ---------------------------- | ----- | -------- | ----- |
| Système domotique    | Raspberry Pi                 | 80€   | 1        | 80€   |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€   | 1        | 50€   |
| **Total**            |                              |       |          | 130€  |

<div style="page-break-after: always;"></div>

### Solution minimale

⚠️ Cette solution part du principe que la box Tahoma Switch peut se connecter aux volets roulants.

![Minimale](img/Minimale.dot.svg#gh-light-mode-only)
![Minimale](img/Minimale-dark.dot.svg#gh-dark-mode-only)

#### Evaluation des couts

| Equipement           | Remplacement                 | Cout  | Quantité | Total |
| -------------------- | ---------------------------- | ----- | -------- | ----- |
| Système domotique    | Raspberry Pi                 | 80€   | 1        | 80€   |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€   | 1        | 50€   |
| Pont IO/RTS          | Somfy Tahoma switch          | 200€  | 1        | 200€  |
| **Total**            |                              |       |          | 330€  |

<div style="page-break-after: always;"></div>

### Solution EnOcean

Cette solution utilise en intégralité le protocole EnOcean et est totalement homogène.

![Enocean](img/Enocean.dot.svg#gh-light-mode-only)
![Enocean](img/Enocean-dark.dot.svg#gh-dark-mode-only)

#### Evaluation des couts

| Equipement           | Remplacement                 | Cout | Quantité | Total |
| -------------------- | ---------------------------- | ---- | -------- | ----- |
| Système domotique    | Raspberry Pi                 | 80€  | 1        | 80€   |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€  | 1        | 50€   |
| Volet Roulant        | NodOn Volet Roulant          | 57€  | 7        | 399€  |
| Thermostat           | NodOn Capteur de temperature | 55€  | 1        | 55€   |
| Fil Pilote chauffage | NodOn Fil pilote             | 55€  | 1        | 55€   |
| **Total**            |                              |      |          | 639€  |

<div style="page-break-after: always;"></div>

### Solution mixte

Au vu de la popularité de EnOcean par rapport à Zigbee, un modèle utilisant les 2 protocoles est possible. L'installation n'est pas plus compliquée qu'un système EnOcean et la plupart des appareils sont moins cher.

![Mixte](img/Mixte.dot.svg#gh-light-mode-only)
![Mixte](img/Mixte-dark.dot.svg#gh-dark-mode-only)

#### Evaluation des couts

| Equipement           | Remplacement                 | Cout | Quantité | Total |
| -------------------- | ---------------------------- | ---- | -------- | ----- |
| Système domotique    | Raspberry Pi                 | 80€  | 1        | 80€   |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€  | 1        | 50€   |
| Pont Zigbee          | SONOFF dongle Zigbee         | 25€  | 1        | 25€   |
| Volet Roulant        | NodOn Volet Roulant          | 45€  | 7        | 315€  |
| Thermostat           | SONOFF SNZB-02D              | 20€  | 1        | 20€   |
| Fil Pilote chauffage | NodOn Fil pilote             | 47€  | 1        | 47€   |
| **Total**            |                              |      |          | 537€  |

<div style="page-break-after: always;"></div>

# Installation

## Mise en place du système domotique

Requiert:
* Raspberry Pi 5 - 2Go ([Farnell](https://fr.farnell.com/raspberry-pi/rpi5-2gb-single/raspberry-pi-5-model-b-2gb-2-4ghz/dp/4531087))
* Alimentation 25W fiche Europe ([Farnell](https://fr.farnell.com/raspberry-pi/sc1157/alimentation-usb-c-5-1v-5a-noire/dp/4263045))
* USB dongle 300 ([Farnell](https://fr.farnell.com/enocean/usb-300/passerelle-usb-pour-radio-868mhz/dp/2342011))
* Carte SD 128Go Classe A2 ([Amazon](https://www.amazon.fr/SanDisk-microSDXC-Adaptateur-RescuePRO-Performance/dp/B09X7DNF6G))

Options:
* SONOFF dongle Zigbee ([Amazon](https://www.amazon.fr/SONOFF-Coordinator-Universelle-Passerelle-Assistant/dp/B09KXTCMSC))

⚠️ En cours d'élaboration.

## Remplacement des volets roulants

⚠️ En cours d'élaboration.

## Remplacement du thermostat

⚠️ En cours d'élaboration.

## Remplacement des éclairages

⚠️ En cours d'élaboration.