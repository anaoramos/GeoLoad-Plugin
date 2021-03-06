# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoLoad
                                 A QGIS plugin
 This plugin loads data from GeoSaude
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-11
        copyright            : (C) 2018 by Load from GeoSaude
        email                : a74727@alunos.uminho.pt
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeoLoad class from file GeoLoad.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geo_load import GeoLoad
    return GeoLoad(iface)
