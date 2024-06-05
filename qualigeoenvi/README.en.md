# Challenge GD4H - QualiGéoEnvi

<a href="https://gd4h.ecologie.gouv.fr/" target="_blank" rel="noreferrer">Green Data for Health</a> (GD4H) is an initiative led by the Innovation Lab (Ecolab) of the French ministry of ecology.

A challenge has been organised in 2023 to develop tools, rooted in the health-environment data community, aiming at addressing shared issues.

Links : 
<a href="https://qualigeoenvi.fr" target="_blank" rel="noreferrer">Web application</a> /
<a href="https://gd4h.ecologie.gouv.fr/defis" target="_blank" rel="noreferrer">Website</a> 


## Qualigéoenvi

Many environmental databases have geographic information (addresses, postcodes, coordinates) and errors or lack of consistency are commonly observed in the data. The analysis of the data is always necessary before further exploitation.

The current application has been developped for non-technical users enabling them to quickly detect **spatial inconsistencies** in a dataset. It enables the loading and mapping of coordinates, as well as the conversion of addresses into latitude and longitude.

**Presentation of the solution:**

- CSV data loading through the web navigator, header analysis and detection of geographic fields.
- Data mapping to check the consistency of their geolocation.
- Conversion of the plain-text addresses into geographic coordinates (in France only).

**Programming language:**

> [React.js](https://react.dev/)

**Final product:**

> Web application: https://qualigeoenvi.fr/

## **Documentation**

> Code documentation [here](./code/front/code_documentation.md)

### **Installation**

> Installation guide [here](./INSTALL.md)

### **Contributing**

If you wish to conribute to this project, please follow the [recommendations](/CONTRIBUTING.md).

### **Functionalities for development**

> Please list new functionalities and bugs on existing functionalities on the [Gitlab issues](https://gitlab.com/data-challenge-gd4h/qualigeoenvi/-/issues).


### **Licence**

The code is published under [MIT Licence](/LICENSE).

The data referenced in this README and in the installation guide is published under <a href="https://www.etalab.gouv.fr/wp-content/uploads/2018/11/open-licence.pdf">Open Licence 2.0</a>.
