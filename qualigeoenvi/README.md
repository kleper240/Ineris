# Challenge GD4H - QualiGéoEnvi

*For an english translated version of this file, follow this [link](/README.en.md)*

Le <a href="https://gd4h.ecologie.gouv.fr/" target="_blank" rel="noreferrer">Green Data for Health</a> (GD4H) est une offre de service incubée au sein de l’ECOLAB, laboratoire d’innovation pour la transition écologique du Commissariat Général au Développement Durable.

Dans ce cadre, un challenge permettant le développement d’outils ancrés dans la communauté de la donnée en santé-environnement afin d’adresser des problématiques partagées a été organisé en 2023.

Liens : 
<a href="https://qualigeoenvi.fr" target="_blank" rel="noreferrer">Application web</a> /
<a href="https://gd4h.ecologie.gouv.fr/defis" target="_blank" rel="noreferrer">Site</a> 

## QualiGéoEnvi

De nombreuses bases de données environnementales contiennent des informations temporelles et géographiques (adresse, code postal, coordonnées), mais il est fréquent d’avoir des valeurs erronées ou un manque de cohérence entre ces différentes variables géographiques. 

L’exploitation de ces bases à des fins de croisement requiert une exploration préalable.

Cette application a été développée afin de permettre à un public non technique de détecter rapidement dans un jeu de données les **incohérences spatiales**. Elle permet de charger des données de latitude / longitude et d'adresses postales, de la cartographier et de vérifier éventuellement leur cohérence géographique. La mesure de la distance qui sépare les coordonnées renseignées dans le jeu de données de celles obtenues suite à la conversion des adresses en coordonnées géographique permet de mettre en évidence ces incohérences spatiales : si la distance est très élevée, les coordonnées renseignées sont a priori incohérentes. 

L'application ne gère pas la multiplicité des systèmes de coordonnées géographiques dans le jeu de données. Il faut privilégier les jeux de données avec un seul système de coordonnées géographiques et de préférence, WGS84.

**Présentation de la solution:**

- Solution de chargement de fichier tabulaire au format CSV dans le navigateur, analyse des en têtes et détection des champs géographiques
- Représentation cartographique des données pour vérification de la cohérence de localisation.
- Conversion des adresses en coordonnées géographiques et vérification de leur cohérence.

**Langage utilisé:**

> [React.js](https://react.dev/)

**Produit final:**

> Application web: https://qualigeoenvi.fr/


<a href="https://gd4h.ecologie.gouv.fr/defis/798" target="_blank" rel="noreferrer">En savoir plus sur le défi</a>


## **Documentation**

> Documentation du code [ici](./code/front/code_documentation.md)

### **Installation**

> Guide d'installation [ici](./INSTALL.md)


### **Contributions**

Si vous souhaitez contribuer à ce projet, merci de suivre les [recommendations](/CONTRIBUTING.md).

### **Fonctionnalités à développer**

> Veuillez lister les besoins en nouvelles fonctionnalités / corrections de fonctionnalités existentes sur les [issues du Gitlab](https://gitlab.com/data-challenge-gd4h/qualigeoenvi/-/issues).

### **Licence**

Le code est publié sous licence [MIT](/licence.MIT).

Les données référencés dans ce README et dans le guide d'installation sont publiés sous [Etalab Licence Ouverte 2.0](/licence.etalab-2.0).
