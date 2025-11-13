

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


#### Récupération des IDs EnOcean

  vous disposez de 3 méthodes.
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

Pour la partie thermostat, nous allons utiliser [Versatile Thermostat](https://github.com/jmcollin78/versatile_thermostat/blob/main/README-fr.md). L'installation se fait à l'aide de [HACS](https://hacs.xyz).

Requiert:
* Capteur de température

Options:
* Fil pilote (remplace le fil pilote Somfy de votre tableau électrique)
* Détecteurs d'ouverture de fenêtre

### Mise en place

* Suivez le guide d'installation de [HACS](https://hacs.xyz/docs/use/configuration/basic)
* Dans HACS, ajoutez les modules suivants:
  * Versatile Thermostat et Versatile Thermostat UI
  * Plotly Graph Card pour afficher de jolis graphes
![Installation Thermostat](img/thermostat1.png)
 * Redémarrez Home Assistant une fois les modules installés

* Nous aurons besoin de quelques capteurs supplémentaires pour la configuration de Versatile Thermostat.
  * Dans la configuration `config/configuration.yaml` YAML, ajoutez la ligne suivante:
  `template: !include template.yaml`.
  * Dans ce nouveau fichier, ajoutez un capteur reprenant les informations météo internet
  * Nous en profiterons pour ajouter un capteur de température de consigne que nous afficherons dans le graphe
```yaml
# Début du fichier config/template.yaml
- sensor:
  - name: "Température extérieure"
    unique_id: template_temperature_external
    device_class: temperature
    unit_of_measurement: "°C"
    # Capteur météo en provenance d'internet
    state: "{{ state_attr('weather.forecast_home', 'temperature') }}"
    icon: mdi:home-thermometer-outline

  - name: "Température consigne"
    unique_id: template_temperature_target
    device_class: temperature
    unit_of_measurement: "°C"
    # Récupération de la consigne du thermostat que nous allons créer
    state: "{{ state_attr('climate.vtherm', 'temperature') }}"
    icon: mdi:thermostat-cog
```
* Les noms des entités sont disponibles dans `Outils de développement` → `Etats`
![Entités](img/thermostat2.png)
* Vérifiez la configuration à partir du menu `Outils de développement` et redémarrez Home Assistant 
* Créez le thermostat : `Paramètres` → `Appareils et services` → `Ajouter une intégration`
* Puis `Versatile Thermostat` → `Thermostat sur un switch`
* Remplissez les [information nécessaires](https://github.com/jmcollin78/versatile_thermostat/blob/main/documentation/fr/base-attributes.md):
  * Nom: `VTherm`
  * Capteur de température
  * Durée du cycle: `15`
  * Capteur de température extérieure: `Température extérieure`
* Remplissez le [sous-jacent](https://github.com/jmcollin78/versatile_thermostat/blob/main/documentation/fr/over-switch.md#configuration) (fil pilote)
> [!TIP]
> Pour tester la fonctionnalité, il n'est pas nécessaire de posséder l'équipement. Vous pouvez en créer un virtuel sur cette fenêtre de configuration.
* Ajoutez la fonction de détection de fenêtre, si vous n'avez pas de capteur, cette fonctionnalité s'enclenchera sur une chute de température de plus de 3°C/h.
* Validez la création du thermostat.
* Si le nom de votre thermostat est différent de `VTherm`, modifiez le fichier de configuration `config/template.yaml` en accord avec ce nouveau nom.

Il est toujours possible de modifier le thermostat créé à partir de `Paramètres` → `Appareils et services` → `Versatile Thermostat configuration`.

### Tableau de bord

Un tableau de bord peut permettre de rapidement valider le comportement de notre thermostat.

* Allez dans `Paramètres` → `Tableaux de bord` → `Ajouter un tableau de bord` → `Tableau de bord vide`
* Dans une nouvelle section, ajoutez les cartes `Versatile Thermostat Climate Card`, `Prévisions météo` et `Plotly Graph Card`
* Pour la configuration `Plotly Graph Card`, ouvrez l'éditeur de code et utilisez la configuration suivante:

```yaml
type: custom:plotly-graph
hours_to_show: 24
refresh_interval: 10*
grid_options:
  columns: full
  rows: 6
defaults:
  entity:
    connectgaps: true
    show_value: true
entities:
  - entity: sensor.temperature_exterieure
    name: Extérieur
    line:
      width: 2
  - entity: sensor.thermostat_temperature
    name: Intérieur
    line:
      width: 2
  - entity: sensor.vtherm_temperature_slope
    name: Δ °C
    yaxis: y2
  - entity: sensor.vtherm_power_percent
    name: Puissance
    fill: tozeroy
    yaxis: y3
  - entity: sensor.temperature_consigne
    name: Consigne
layout:
  xaxis:
    rangeselector:
      font:
        color: rgba(255,255,255,0.8)
      x: 1
      xanchor: right
      bgcolor: rgba(0,0,0,0.2)
      activecolor: rgba(255,255,255,0.1)
      buttons:
        - count: 6
          step: hour
        - count: 1
          step: day
        - count: 7
          step: day
        - count: 30
          step: day
  yaxis2:
    rangemode: tozero
    zeoline: true
    showticklabels: false
    showgrid: false
    showline: false
    ticks: ""
    title: ""
    fixedrange: true
    range:
      - -5
      - 5
  yaxis3:
    visible: false
    fixedrange: true
    range:
      - -2
      - 102
```

* Adaptez les paramètres en fonction de vos besoins.

![Tableau de bord thermostat](img/thermostat3.png)

## Remplacement des éclairages

Les éclairages préinstallés disposent de plusieurs associations :
* L'association point à point avec les interrupteurs (canal 1 avec interrupteur AI et AO par ex.)
* L'association avec la passerelle EnOcean

Dans ce cas, la passerelle ne communique pas directement avec les éclairages en cas d'appui sur l'un des boutons. Aucune automatisation n'est nécessaire pour faire fonctionner vos appareils.

Il est cependant possible d'appairer d'autres appareils aux boutons. Les volets roulants sont un exemple :
* `BI` (la touche droite en bas) est associée à `fermer les volets`
* `BO` (la touche droite en haut) est associée à `ouvrir les volets`
* `AO+BO` (les touches en haut) est associée à `arrêter les volets`

Dans l'exemple ci-dessous, nous associons la touche `AI+BI` à la commutation d'un éclairage:
* Allez dans `Paramètres` → `Automatisation` → `Créer une automatisation`
* Associez `AI+BI` à l'action de commutation
![Automate commutation](img/automate1.png)

> [!NOTE]
> Si vous utilisez ce genre d'automatisation, faites attention à l'association des actions simples AI. Il vous faudra ajouter une action AI et non-BI.

## Remplacement des volets roulants

> [!WARNING]
> En cours d'élaboration.

# Références

* https://www.enocean.com/en/faq-knowledge-base/what-is-difference-between-base-id-and-chip-id/