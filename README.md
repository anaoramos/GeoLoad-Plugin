# GeoLoad Plugin
	Geoload plugin can be used to load multiple shapefiles from GeoSaude and from your computer to QGIS.


### Installing

	To Run the project you must have 2 softwares installed: QGis3 and PgAdmin

	Some problems may appear when installing these software.
	If this happens, please see the links below that explain the installation of QGis and PgAdmin, respectively.
		-> https://github.com/qgis
		-> https://github.com/AdrianoModa/CodigosADS/wiki/Configurar-pgAdmin-4-v1.3-no-Ubuntu-16.04-Desktop

## Running And Configuration
	1. Open PgAdmin
	2. Create a DataBase and restore the "geoload.backup" file
	3. Open "geo_load.py" and set the host name, port, database name, username and password
	4. Open QGis3
	5. Install the plugin

The restore of the "geoload.backup" file has some problems, with respect to the parameters that must be placed. So, to be easier, the configuration of this is in the image below:

(https://github.com/ReginaSousa8/GeoSaude/blob/master/config.reload.png)


## Built With

* Python - The language used
* [PyCharm CE](https://www.jetbrains.com/pycharm/) - The framework used to program
* [Qt](https://www.qt.io) - The framework used to create the plugin
* [Qgis](https://qgis.org/en/site/) - The geographic Information System used in the project


## Versioning

Version 1.0

## Authors

* **ANA MACHADO** - *University of Minho* (https://github.com/anamsmachado)
* **ANA RAMOS** - *University of Minho* (https://github.com/anaoramos)
* **ANA SOUSA** - *University of Minho* (https://github.com/ReginaSousa8)

                                                                 
