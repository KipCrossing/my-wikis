# Python for QGIS

## Documentation

* [QGIS](https://qgis.org/pyqgis/master/)
* [GDAL](https://pcjericks.github.io/py-gdalogr-cookbook/)

---

## Popular Libraries

### iface

Move camera to layer:

```python
layer = iface.addVectorLayer("/home/kipling/Documents/Tute/Data/TM_WORLD_BORDERS-0.3","TM_WORLD_BORDERS-0.3","ogr")

iface.mapCanvas().setExtent(-125,31,-133,38)
iface.mapCanvas().setExtent(QgsRectangle(-125,31,-133,38))
iface.mapCanvas().refresh()
```

Add generated files to layer list:

```Python
self.outBuffer = self.dlg.le_outBuffer.text()
self.outRaster = self.dlg.le_outRaster.text()
self.iface.addVectorLayer(self.outBuffer, str.split(os.path.basename(self.outBuffer),".")[0],"ogr")
self.iface.addRasterLayer(self.outRaster, str.split(os.path.basename(self.outRaster),".")[0])

```

---

### qgis.core

Using `QgsProject`:

```Python
from qgis.core import QgsProject

def loadVectors(self):
		"""
		Load vectors from QGIS table of contents
		"""
		self.dlg.cb_inVector.clear()
		layers = [layer for layer in QgsProject.instance().mapLayers().values()]
		vector_layers = []
		for layer in layers:
				if layer.type() == QgsMapLayer.VectorLayer:
						vector_layers.append(layer.name())
		self.dlg.cb_inVector.addItems(vector_layers)

def loadRasters(self):
		"""
		Load rasters from QGIS table of contents
		"""
		self.dlg.cb_inRaster.clear()
		layers = [layer for layer in QgsProject.instance().mapLayers().values()]
		raster_layers = []
		for layer in layers:
				if layer.type() == QgsMapLayer.RasterLayer:
						raster_layers.append(layer.name())
		self.dlg.cb_inRaster.addItems(raster_layers)

```

Using `QgsVectorFileWriter` and `QgsWkbTypes`:

```Python
from qgis.core import QgsWkbTypes

def buffer_maker(self):
		"""Buffer feature of vector layer"""
		fields = self.inVector.fields()
		writer = QgsVectorFileWriter(self.outBuffer,
		 								"CP1250",
										fields,
										QgsWkbTypes.Polygon,
										self.inVector.sourceCrs(),
										"ESRI Shapefile")
		features = self.inVector.getFeatures()
		for feature in features:
				geom = feature.geometry()
				buffer = geom.buffer(self.bufDist, 5)
				feature.setGeometry(buffer)
				writer.addFeature(feature)
		del writer

```
Using `QgsMapLayer`:

```Python
from qgis.core import QgsMapLayer

if layer.type() == QgsMapLayer.VectorLayer:
	print("Is vector")
elif layer.type() == QgsMapLayer.RasterLayer:
	print("Is Raster")

```

---

### PyQt5

```python
from PyQt5.QtGui import QColor
iface.mapCanvas().setCanvasColor(QColor("#6060FF"))
iface.mapCanvas().refresh()

for feature in layer.getFeatures():
	geo = feature.geometry()
	cen = geo.centroid().asPoint()
	name = feature.attribute("NAME")
	print(name,cen.x(),cen.y())
```

---

### GDAL

Using `Warp`:

```Python
from osgeo import gdal

def clip(self):
		"""Clip input raster file with buffer result"""
		warpOptions = gdal.WarpOptions(format="GTiff",
																		cutlineDSName=self.outBuffer,
																		cropToCutline=True,
																		dstNodata=-9999.0)
		gdal.Warp(self.outRaster,
								self.inRaster.dataProvider().dataSourceUri(),
								options=warpOptions)
```
