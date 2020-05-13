# SoilTech Library Design

## preface

This document is intended to be a collection of suggestions on how best to structure and refactor the current codebase to become a working library with intuitive API design. The perspective held, whilst making this document, is in the form of a software engineer attempting to integrate the soiltech tools with the guidance of an agronomist. Therefore the object structure and names will have to reflect existing agricultural structures (Farms, paddocks, samples...). Lastly, when practical, the UI (API) should be abstracted away from the underlying science and statistical methods for basic usage; but still, be accessible.

Overall Structure
This is a WIP and can be viewed and edited here: https://app.creately.com/diagram/qcFaiYqyJnU/view

---

## Object and Method Descriptions

---

### Farm(farmName: String, hadoopPath: String)

#### methods

- **addPaddock(paddockName: String, filePath: string)**: *Paddock*
- **removePaddock(paddockName: String)**
- **allPaddockNames()**: *List[String]*
- **allPaddocks()**: *List[Paddock]*
- **getGroupedPaddocks()**: *List[Lists[Paddock]]*
- **paddock(paddockName: String)**: *Paddock*
- **generateZones(numZones: Int, filePath: String, zoneGroupName: String, List[Paddock])**: *List[Zone]*
- **removeZones(zoneGroupName: String)**
- **zone(zoneGroupName: String)**: *List[Zone]*

#### properties

- **starndardAttributes()**: *List[String]*

#### examples

Adding paddocks to farm

```scala
Import org.soiltech.agriculture.{Farm}
val samsFarm = Farm("samsFarm", "local[*]")

val stanAtt = samsFarm.starndardAttributes()
println(stanAtt) // ["sand", "silt", "clay", "ph", "ndvi" …...]

val ndvi = stanAtt[4]

samsFarm.addPaddock("paddock01", "docs/inputs/paddock01/")
samsFarm.addPaddock("paddock02", "docs/inputs/paddock02/")
samsFarm.addPaddock("paddock07", "docs/inputs/paddock07/")
samsFarm.addPaddock("paddock07", "docs/inputs/paddock11/")

samsFarm.removePaddock("paddock11")

```

Creating Zones




### Paddock(boundary: Boundary, grids: List[grids])


#### methods


#### properties

```scala

val paddock07 = samsFarm.paddock("paddock07")

println(paddock07.attributes()) // ["elevation","kgamma","ugamma"]
paddock07.addAttribute(ndvi, "path/to/ndvi.tif")
println(paddock07.attributes()) // ["elevation","kgamma","ugamma", "ndvi"]

println(paddock07.elevation().unit()) // "m"
println(paddock07.elevation().type()) // "static"
println(paddock07.ph().type()) // "dynamic"
println(paddock07.ph().lifecycle()) // 0.25 - years


val stanAtt = samsFarm.starndardAttributes()
println(stanAtt) // ["sand", "silt", "clay", "ph", …...]

val paddocks = samsFarm.getPaddocks()
println(paddocks) // ["paddock01"," paddock02", "paddock07"]

val groups = samsFarm.getGroupedPaddocks()
println(groups[0]) // ["paddock01", "paddock02"]
println(groups[1]) // ["paddock07"]
samsFarm.deletePaddock("paddock07")
samsFarm.deletePaddocks(["paddock07"])



samsFarm.generateZones(3, "docs/zones/", "AllFarm") // For all paddocks
samsFarm.generateZones(3, "docs/zones/", "South", ["paddock01", "paddock02"]) // for only these two paddocks

val southZones = samsFarm.getSones("South")
println(southZones) // ["Zone01", "Zone02", "Zone03"]

samsFarm.deleteZones("South")

samsFarm.getZoneGroups()
```
