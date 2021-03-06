# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoLoad
                                 A QGIS plugin
 This plugin loads data from GeoSaude
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Load from GeoSaude
        email                : a74727@alunos.uminho.pt
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from qgis.core import *
import qgis.utils
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .geo_load_dialog import GeoLoadDialog
import os.path



import psycopg2

 # set host name, port, database name, username and password
hname = "localhost"
port = "5432"
dbName = "aula2"
username = "postgres"
password = "viladoconde"
class GeoLoad:
    """QGIS Plugin Implementation."""

   



    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeoLoad_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = GeoLoadDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&GeoLoad')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'GeoLoad')
        self.toolbar.setObjectName(u'GeoLoad')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('GeoLoad', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/Users/anaramos/Desktop/SIG/geoload/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'GeoLoad'),
            callback=self.run,
            parent=self.iface.mainWindow())

        #self.dlg.comboBox.clear()

        self.dlg.toolButton.clicked.connect(self.openC)
        self.dlg.checkBox_1.clicked.connect(self.openTable1)
        self.dlg.checkBox_2.clicked.connect(self.openTable2)
        self.dlg.checkBox_3.clicked.connect(self.openTable3)
        self.dlg.checkBox_4.clicked.connect(self.openTable4)
        self.dlg.checkBox_5.clicked.connect(self.openTable5)
        self.dlg.checkBox_6.clicked.connect(self.openTable6)
        self.dlg.checkBox_7.clicked.connect(self.openTable7)
        self.dlg.checkBox_8.clicked.connect(self.openTable8)
        self.dlg.checkBox_9.clicked.connect(self.openTable9)
        self.dlg.checkBox_10.clicked.connect(self.openTable10)
        self.dlg.checkBox_11.clicked.connect(self.openTable11)
        self.dlg.checkBox_12.clicked.connect(self.openTable12)
        self.dlg.checkBox_13.clicked.connect(self.openTable13)
        self.dlg.checkBox_14.clicked.connect(self.openTable14)
        self.dlg.checkBox_15.clicked.connect(self.openTable15)
        self.dlg.checkBox_16.clicked.connect(self.openTable16)
        self.dlg.checkBox_17.clicked.connect(self.openTable17)
        self.dlg.checkBox_18.clicked.connect(self.openTable18)
        self.dlg.checkBox_19.clicked.connect(self.openTable19)
        self.dlg.checkBox_20.clicked.connect(self.openTable20)
        self.dlg.checkBox_21.clicked.connect(self.openTable21)
        self.dlg.checkBox_22.clicked.connect(self.openTable22)
        self.dlg.checkBox_23.clicked.connect(self.openTable23)
        self.dlg.checkBox_24.clicked.connect(self.openTable24)

        self.loadCom()



    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&GeoLoad'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar



    def loadCom(self):
        #load datas to combobox
        self.dlg.comboBox.clear()
        c = [layer for layer in QgsProject.instance().mapLayers().values()]
        c_list=[]
        for cp in c:
            if cp.type()== QgsMapLayer.VectorLayer:
                c_list.append(cp.name())
        self.dlg.comboBox.addItems(c_list)


    def openC(self):
        #open data from file dialog
        infile = str(QFileDialog.getOpenFileName(filter="Shapefiles (*.shp)")[0])
        if infile is not None:
            self.iface.addVectorLayer(infile, str.split(os.path.basename(infile),".")[0], "ogr")
            self.loadCom()


    def openTable1(self):
        if self.dlg.checkBox_1.isChecked:
            self.dlg.checkBox_1.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Adolescent births", "geom", 'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Adolescent births", username)
        QgsProject.instance().addMapLayer(vlayer)

        self.loadCom()



    def openTable2(self):
        if self.dlg.checkBox_2.isChecked:
            self.dlg.checkBox_2.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Cervical cancer screening rate", "geom",  'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Cervical cancer screening rate", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable3(self):
        if self.dlg.checkBox_3.isChecked:
            self.dlg.checkBox_3.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Consumption of quinolones/total consumption of antibiotics in o", "geom", 'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Consumption of quinolones/total consumption of antibiotics in o", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable4(self):
        if self.dlg.checkBox_4.isChecked:
            self.dlg.checkBox_4.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Crude mortality rate due to HIV/AIDS before the age of 65", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Crude mortality rate due to HIV/AIDS before the age of 65", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable5(self):
        if self.dlg.checkBox_5.isChecked:
            self.dlg.checkBox_5.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Crude mortality rate due to ischemic heart diseases before the ", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Crude mortality rate due to ischemic heart diseases before the ", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable6(self):
        if self.dlg.checkBox_6.isChecked:
            self.dlg.checkBox_6.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Hospital admission due to Chronic Obstructive Pulmonary Disease", "geom", 'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Hospital admission due to Chronic Obstructive Pulmonary Disease", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable7(self):
        if self.dlg.checkBox_7.isChecked:
            self.dlg.checkBox_7.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Hospital admission due to asthma", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Hospital admission due to asthma", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable8(self):
        if self.dlg.checkBox_8.isChecked:
            self.dlg.checkBox_8.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "In-hospital lethality due to ischemic heart disease", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "In-hospital lethality due to ischemic heart disease", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable9(self):
        if self.dlg.checkBox_9.isChecked:
            self.dlg.checkBox_9.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Incidence of CVA", "geom", 'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Incidence of CVA", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable10(self):
        if self.dlg.checkBox_10.isChecked:
            self.dlg.checkBox_10.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Incidence of congenital syphilis", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Incidence of congenital syphilis", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable11(self):
        if self.dlg.checkBox_11.isChecked:
            self.dlg.checkBox_11.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Infant Mortality", "geom", 'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Infant Mortality", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable12(self):
        if self.dlg.checkBox_12.isChecked:
            self.dlg.checkBox_12.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Mortality from 1 to 4 years of age", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Mortality from 1 to 4 years of age", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable13(self):
        if self.dlg.checkBox_13.isChecked:
            self.dlg.checkBox_13.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Number of deaths due to alcohol-related motor accidents", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Number of deaths due to alcohol-related motor accidents", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable14(self):
        if self.dlg.checkBox_14.isChecked:
            self.dlg.checkBox_14.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Obesity (ages 18 to 24)", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Obesity (ages 18 to 24)", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable15(self):
        if self.dlg.checkBox_15.isChecked:
            self.dlg.checkBox_15.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Overweight (ages 35 to 44)", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Overweight (ages 35 to 44)", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable16(self):
        if self.dlg.checkBox_16.isChecked:
            self.dlg.checkBox_16.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Perinatal Mortality", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Perinatal Mortality", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()

    def openTable17(self):
        if self.dlg.checkBox_17.isChecked:
            self.dlg.checkBox_17.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Potential Years of Life Lost due to diabetes", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Potential Years of Life Lost due to diabetes", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable18(self):
        if self.dlg.checkBox_18.isChecked:
            self.dlg.checkBox_18.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Potential Years of Life Lost due to malignant neoplasm of the t", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Potential Years of Life Lost due to malignant neoplasm of the t", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable19(self):
        if self.dlg.checkBox_19.isChecked:
            self.dlg.checkBox_19.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Ratio between hospital emergencies and outpatient appointments", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Ratio between hospital emergencies and outpatient appointments", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable20(self):
        if self.dlg.checkBox_20.isChecked:
            self.dlg.checkBox_20.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Schools with good health and safety conditions", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Schools with good health and safety conditions", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable21(self):
        if self.dlg.checkBox_21.isChecked:
            self.dlg.checkBox_21.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Standardised mortality rate due to alcohol-related diseases bef", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Standardised mortality rate due to alcohol-related diseases bef", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable22(self):
        if self.dlg.checkBox_22.isChecked:
            self.dlg.checkBox_22.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Tobacco - daily consumption (ages 65-74)", "geom", 'id>=0','id')
        vlayer = QgsVectorLayer(uri.uri(False), "Tobacco - daily consumption (ages 65-74)", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()


    def openTable23(self):
        if self.dlg.checkBox_23.isChecked:
            self.dlg.checkBox_23.setChecked(False)
        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Used orphan medication", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Used orphan medication", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()

    def openTable24(self):
        if self.dlg.checkBox_24.isChecked:
            self.dlg.checkBox_24.setChecked(False)

        uri = QgsDataSourceUri()
        uri.setConnection(hname, port, dbName, username, password)
        uri.setDataSource("public", "Alcohol - consumption over the last 12 months (ages 65-74)", "geom",'id>=0', 'id')
        vlayer = QgsVectorLayer(uri.uri(False), "Alcohol - consumption over the last 12 months (ages 65-74)", username)
        QgsProject.instance().addMapLayer(vlayer)
        self.loadCom()



    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:

            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
