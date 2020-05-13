from qgis.core import *
from qgis.gui import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import sys, os

class MapViewer(QMainWindow):
    def __init__(self, shapefile):
        QMainWindow.__init__(self)
        self.setWindowTitle("Map Viewer")

        canvas = QgsMapCanvas()
        # canvas.useImageToRender(False)
        canvas.setCanvasColor(Qt.white)
        canvas.show()

        layer = QgsVectorLayer(shapefile,"Layer1","ogr")
        if not layer.isValid():
            raise IOError("Invalid Shapefile")

        QgsMapLayerRegistry.instance().addMapLayer(layer)
        # Make layer visible
        canvas.setExtent(layer.extent())
        canvas.setLayerSet([QgsMapCanvasLayer(layer)])

        slef.setCentralWidget(canvas)


# From PyQt5.QtWidgets
app = QApplication(sys.argv)
# Dont need it
# QgsApplication.setPrefixPath(os.environ['QGIS_PREFIX'], True)
QgsApplication.initQgis()

viewer = MapViewer("/home/kipling/Documents/Tute/Data/TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp")
viewer.show()
app.exec_()

QgsApplication.exitQgis()
