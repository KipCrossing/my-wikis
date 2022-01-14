# my-wikis

A Repository for me to keep my wikis in one place

## Table of Contents

- [SQL WIKI](SQL.md)
- [VUE.JS WIKI](VUE-JS.md)
- [ESP2866-MicroPython](https://github.com/KipCrossing/Micropython-AD9833/blob/master/README.md)
- [MicroPython on the ESP32](https://github.com/KipCrossing/Micro-Camera/blob/master/README.md)
- [Making pip packages](https://packaging.python.org/tutorials/packaging-projects/#configuring-your-project)
- [Python for QGIS](QGIS-Python.md)
- [Scala](SCALA.md)
- [SQL](SQL.md)

---

```python
from collections import Counter,namedtuple

Point = namedtuple("point", "x,y")

pt = Point(1,-2)
print(pt.x,pt.y)
print(pt[0])
```

### Docker

Add env vars then run command

```
docker exec -i CONTAINER_ID /bin/bash -c "export VAR1=VAL1 && export VAR2=VAL2 && your_cmd"
```