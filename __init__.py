# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AltibasePlugin
                                 A QGIS plugin
 This plugin allows Altibase vector layer.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-29
        copyright            : (C) 2020 by Altibase Corp.
        email                : us@altibase.com
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
    """Load AltibasePlugin class from file AltibasePlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .plugin import AltibasePlugin
    return AltibasePlugin(iface)