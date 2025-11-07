

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



## Solutions

| Solution       | Interopérabilité | Facilité de migration | Cout      | Note                                           |
| -------------- | ---------------- | --------------------- | --------- | ---------------------------------------------- |
| Building Care  | ★        | ★★★★★             | ☆ | 100€/an + tributaire de Building Care          |
| Sans domotique | ☆        | ★★★★★             | ★★★★★ | Remplacement des équipements au fil des pannes |
| Minimale       | ★★★★        | ★★★             | ★★★ | Possiblement impossible                        |
| EnOcean        | ★★★★        | ★★             | ★ |                                                |
| Mixte          | ★★★★★        | ★★             | ★★ |                                                |



### Solution sans domotique

![Sans domotique](img/SansDomotique.dot.svg#gh-light-mode-only)
![Sans domotique](img/SansDomotique-dark.dot.svg#gh-dark-mode-only)

#### Evaluation des couts

| Equipement           | Remplacement                 | Cout  | Quantité | Total |
| -------------------- | ---------------------------- | ----- | -------- | ----- |
| Système domotique    | Raspberry Pi                 | 80€   | 1        | 80€   |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€   | 1        | 50€   |
| **Total**            |                              |       |          | 130€  |



### Solution minimale

> [!WARNING]
> Cette solution part du principe que la box Tahoma Switch peut se connecter aux volets roulants.

![Minimale](img/Minimale.dot.svg#gh-light-mode-only)
![Minimale](img/Minimale-dark.dot.svg#gh-dark-mode-only)

#### Evaluation des couts

| Equipement           | Remplacement                 | Cout  | Quantité | Total |
| -------------------- | ---------------------------- | ----- | -------- | ----- |
| Système domotique    | Raspberry Pi                 | 80€   | 1        | 80€   |
| Pont EnOcean         | USB dongle 300 EnOcean       | 50€   | 1        | 50€   |
| Pont IO/RTS          | Somfy Tahoma switch          | 200€  | 1        | 200€  |
| **Total**            |                              |       |          | 330€  |



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



# Installation

Pour le système de domotique j'ai choisi la Raspberry Pi et Home Assistant qui sont des produits très bien supportés par la communauté open-source.
Des Box domotiques préinstallées sont disponibles sur le marché à un cout supérieur et sont moins flexibles en cas de panne.

> [!NOTE]
> Toutes les références sont proposées à titre indicatif.

## Mise en place du système domotique

Requiert:
* Raspberry Pi 5 - 2Go ([Farnell](https://fr.farnell.com/raspberry-pi/rpi5-2gb-single/raspberry-pi-5-model-b-2gb-2-4ghz/dp/4531087))
* Alimentation 25W fiche Europe ([Farnell](https://fr.farnell.com/raspberry-pi/sc1157/alimentation-usb-c-5-1v-5a-noire/dp/4263045))
* USB dongle 300 EnOcean ([Farnell](https://fr.farnell.com/enocean/usb-300/passerelle-usb-pour-radio-868mhz/dp/2342011)) ou Pi Hat EnOcean([Domadoo](https://www.domadoo.fr/fr/dongle-enocean/2466-enocean-module-radio-enocean-pi-868mhz.html))
* Carte SD 128Go Classe A2 ([Amazon](https://www.amazon.fr/SanDisk-microSDXC-Adaptateur-RescuePRO-Performance/dp/B09X7DNF6G))

Options:
* Boitier DIN Rail pour Raspberry Pi ([Amazon](www.amazon.fr/GeeekPi-Raspberry-Boîtier-Cooling-Electrical/dp/B0D19T5NYP))
* SONOFF dongle Zigbee ([Amazon](https://www.amazon.fr/SONOFF-Coordinator-Universelle-Passerelle-Assistant/dp/B09KXTCMSC))

* Suivez le guide d'installation de [Home Assistant](https://www.home-assistant.io/installation/raspberrypi).

### Zigbee

Pour l'intégration Zigbee, le plugin Zigbee2MQTT est réputée plus stable que le plugin officiel ZHA.

* Suivez le processus d'installation de [Zigbee2MQTT](https://www.hacf.fr/zigbee2mqtt-config).
  * Dans les intégrations, commencez par désactiver ZHA
  * Allez sur la page d'installation des plugins:
![Plugins](img/plugins.png)
  * Installez Mosquitto et Zigbee2MQTT:
    * Mosquitto:
    [![](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_mosquitto)
    * Zigbee2MQTT:
      [![intégration Zigbee2MQTT](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https://github.com/zigbee2mqtt/hassio-zigbee2mqtt)


    ![MQTT](img/plugins_mqtt.png)
  * Allez sur la page de configuration de Mosquitto puis Zigbee2MQTT pour les démarrer et les configurer:
    ![alt text](img/plugins_mqtt2.png)
  * Choisissez le dongle Zigbee:
    ![alt text](img/plugins_mqtt3.png)
  * Une fois démarré, allez de nouveau sur l'interface Zigbee2MQTT et activez la découverte d'appareils:
    ![alt text](img/plugins_mqtt4.png)
  * Ajoutez et renommez vos équipements:
    ![alt text](img/plugins_mqtt5.png)


### EnOcean

> [!CAUTION]
> Etude de faisabilité en cours.

L'intégration par défaut de EnOcean pour Home Assistant nécessite une configuration complexe des équipements, nous allons donc en utiliser une autre. L'intégration EnOcean choisie se base aussi sur l'architecture MQTT et est sortie en version 1.0 en octobre 2025.

* Suivez le processus d'installation de [EnOceanMQTT](https://github.com/ChristopheHD/HA_enoceanmqtt-addon)
  * Allez sur la page d'installation des plugins:
![Plugins](img/plugins.png)
  * Installez Mosquitto si ce n'est pas déjà fait, l'éditeur éditeur de texte et EnOceanMQTT:
    * Mosquitto:
      [![intégration Mosquitto](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_mosquitto)
    * Editeur:
      [![intégration Editeur de texte](https://my.home-assistant.io/badges/supervisor_addon.svg)](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_configurator)
    * EnOcean:
      [![intégration EnOcean](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https://github.com/ChristopheHD/HA_enoceanmqtt-addon)

    ![EnOcean](img/plugins_enocean.png)
  * Récupérez les addresses des équipements, vous disposez de 3 méthodes.
    > [!WARNING]
> Il est recommandé de récupérer l'adresse de la passerelle avant l'arrêt des services Flexom. Vous devrez changer le BaseID de votre clé pour correspondre à la passerelle.
    * Le code est écrit à l'arrière des interrupteurs ou sur les éclairages.
    * Il est disponible sur l'application Flexom depuis le menu suivant:
    `Menu principal`  → `Fonctions avancées, Paramètres` → `Mes objets`
    Puis `Objets` → `<objet>` → `Infos` → `Détails` → `ComID`
    * Depuis les logs de l'application, quand vous appuyez sur un interrupteur, l'interrupteur et l'éclairage envoient des informations:
    ![Logs EnOcean](img/plugins_enocean3.png)
  * Créez et éditez le fichier `enoceanmqtt.devices`
    ![Edition devices EnOcean](img/plugins_enocean2.png)
    Les interrupteurs utilisent le code EEP F6-02-01 et les éclairages le code EEP D2-01-12.
    ```yaml
    [passerelle_flexom]
    address         = 0xFA57C0DE
    ignore          = 1

    [interrupteur_chambre_1]
    address         = 0xDEADBEEF
    rorg            = 0xF6
    func            = 0x02
    type            = 0x01

    [eclairage_chambre_1]
    address         = 0xABADC0DE
    rorg            = 0xD2
    func            = 0x01
    type            = 0x12
    ```
  * Pour changer le BaseID de votre clé, téléchargez le logiciel [Dolphin View](https://www.enocean.com/en/product/dolphinview) (nécessite de créer un compte).
  * Ouvrez le logiciel et exécutez les commandes comme décrites sur l'image.
  > [!CAUTION]
> Le changement de BaseID est limité à 10 fois sur les clés EnOcean.
  La commande en vert permet de récupérer l'ID courant de la clé.
  La commande en rouge permet de changer l'ID de la clé. Utilisez l'ID votre ancienne passerelle.
  ![Remplacement ID passerelle](img/plugins_enocean6.png)
  * Réaffectez et renommez les appareils créés:
  ![Affectation EnOcean](img/plugins_enocean4.png)
  * Une fois la migration effectuée, vous pourrez controller vos luminaires depuis Home Assistant.
  ![Utilisation EnOcean](img/plugins_enocean5.png)
      

## Remplacement du thermostat

> [!WARNING]
> En cours d'élaboration.

## Remplacement des éclairages

> [!WARNING]
> En cours d'élaboration.

## Remplacement des volets roulants

> [!WARNING]
> En cours d'élaboration.

# Références

* https://www.enocean.com/en/faq-knowledge-base/what-is-difference-between-base-id-and-chip-id/