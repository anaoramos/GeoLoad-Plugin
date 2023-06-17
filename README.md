# GeoLoad Plugin

GeoLoad Plugin is a tool that allows you to load multiple shapefiles from GeoSaude and your computer into QGIS. This plugin simplifies the process of importing shapefiles and enables seamless integration with the QGIS software.

## Installation

To run the project, you must have the following software installed:

- QGIS 3
- PgAdmin

Please follow the instructions below to install these software components:

1. **QGIS**: Visit the [QGIS GitHub repository](https://github.com/qgis) for installation instructions specific to your operating system.

2. **PgAdmin**: Refer to the [PgAdmin installation guide](https://github.com/AdrianoModa/CodigosADS/wiki/Configurar-pgAdmin-4-v1.3-no-Ubuntu-16.04-Desktop) for detailed steps on configuring PgAdmin on your system.

Note: Some problems may arise during the installation process. If you encounter any issues, please refer to the provided links for assistance.

## Running and Configuration

Follow the steps below to run and configure the GeoLoad Plugin:

1. Open PgAdmin and create a database. Restore the "geoload.backup" file into the database.

2. Open the "geo_load.py" file and set the hostname, port, database name, username, and password according to your database configuration.

3. Open QGIS 3.

4. Install the GeoLoad Plugin.

For detailed configuration instructions, please refer to the image [config.reload.png](https://github.com/ReginaSousa8/GeoSaude/blob/master/config.reload.png).

## Built With

The GeoLoad Plugin is built using the following technologies:

- Python - The programming language used for development.
- PyCharm CE - The integrated development environment (IDE) used for coding.
- Qt - The framework used for creating the plugin's user interface.
- QGIS - The geographic information system (GIS) used for visualizing and managing geospatial data.
