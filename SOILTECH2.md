# SoilTech Library Design

## preface

This document is intended to be a collection of suggestions on how best to structure and refactor the current codebase to become a working library with intuitive API design. The perspective held, whilst making this document, is in the form of a software engineer attempting to integrate the soiltech tools with the guidance of an agronomist. Therefore the object structure and names will have to reflect existing agricultural structures (Tools, Zone, Sample...). Lastly, when practical, the UI (API) should be abstracted away from the underlying science and statistical methods for basic usage; but still, be accessible.




```scala
Import org.soiltech.agriculture.{Tools, Zone, Sample}


samsFarm.addPaddock("paddock01", "docs/inputs/paddock01/")
samsFarm.addPaddock("paddock02", "docs/inputs/paddock02/")
samsFarm.addPaddock("paddock07", "docs/inputs/paddock07/")
samsFarm.addPaddock("paddock07", "docs/inputs/paddock11/")

samsFarm.removePaddock("paddock11")
```

Gouped paddocks

```scala
val paddocks = samsFarm.getPaddocks()
println(paddocks) // [paddock01, paddock02, paddock07]

val groups = samsFarm.getGroupedPaddocks()
println(groups[0]) // [paddock01, paddock02]
println(groups[1]) // [paddock07]
samsFarm.removePaddock(paddock07)
samsFarm.removePaddocks([paddock07,paddock01])
```

Creating Zones

```scala
samsFarm.generateZones(3, "docs/zones/", "AllFarm") // For all paddocks
samsFarm.generateZones(3, "docs/zones/", "South", [paddock01, paddock02]) // for only these two paddocks
samsFarm.generateZones(6, "docs/zones/", "South2", groups[0])

val southZones = samsFarm.getZones("South")
println(southZones) // [Zone01, Zone02, Zone03]

val zBoundatry1 = Zone01.boundary()



samsFarm.removeZones("South2")
println(samsFarm.getZoneGroups()) // ["AllFarm","South"]
```

### Zone(boundary: Boundary,  type: String)

 -  boundary - The boundary of the Zone
 -  The type of zone: "Paddock", "PotentialManagementZone", "ManagementZone"

#### methods

- **addAttribute(attributeName: String, grid: RDD[((Double,Double),Double)], unit: String, type: String, lifeSpan: Double)**: _2dAttribute_
- **getAttribute(attributeName: String)**: _2dAttribute_
- **removeAttribute(attributeName: String)**

#### properties

- **attributeNames()**: _List[String]_
- **boundary()**: _Boundary_

#### examples

Adding an attribute to paddock

```scala

val stanAtt = samsFarm.starndardAttributes()
println(stanAtt) // ["sand", "silt", "clay", "ph", "ndvi" …...]

val ndvi = stanAtt[4]

val paddock07 = samsFarm.paddock("paddock07")

println(paddock07.attributes()) // ["elevation","kgamma","ugamma"]
paddock07.addAttribute(ndvi, "path/to/ndvi.tif")
println(paddock07.attributes()) // ["elevation","kgamma","ugamma", "ndvi"]

// can also be done with Zones
println(southZones[2].attributes()) // []
southZones[2].addAttribute(ndvi, "path/to/ndvi.tif")
println(southZones[2].attributes()) // ["ndvi"]
```

Properties of attributes

```scala
println(paddock07.elevation().unit()) // "m"
println(paddock07.elevation().type()) // "static"

println(paddock07.ph().type()) // "dynamic"
println(paddock07.ph().timestep()) // 0.25 - years
println(paddock07.ph().sampleDate()) // 05-02-2020

println(paddock07.ndvi().type()) // "cyclic"
println(paddock07.ndvi().timestep()) // 0.125 - years
println(paddock07.ndvi().lifecycle()) // 1 - year
println(paddock07.ndvi().sampleDate()) // 14-05-2020


// Weighting
println(paddock07.ndvi().weighting()) // 1
println(paddock07.ndvi().updateWeighting(3))
println(paddock07.ndvi().weighting()) // 3

// NOTE: these concepts will be useful for nutrients
```

### Sample(location: (Double,Double), date: String)

#### methods

- **addAttribute(attributeName: Sting, depthRanges: List[(Double, Double)], values: List[Double])**: _1dAttribute_
- **getAttribute(attributeName: String)**: _1dAttribute_
- **removeAttribute(attributeName: String)**

#### properties

- **location**: **(Double, Double)**

```scala




val smple01 = samsFarm.addSample((-33.466643, 151.217735), "05-02-2020")
                .addAttribute("clay", [(0,10),(10,40),(40,70)], [35.4, 27.8, 38.5])
                .addAttribute("ph", [(0,10),(10,40),(40,70)], [8.5, 6.2, 7.7])

val clay = sample01.getAttribute("clay")

println(clay.depthRanges) // [(0,10),(10,40),(40,70)]
println(clay.values(clay.depthRanges)) // [35.4, 27.8, 38.5]

// You can even get values form custom depthRanges

clay.values([(0,15),(15,30),(30,70)]) // [33.2, 29.9, 36.7]
sample01.removeAttribute("ph")
```

## Analyse your Farm (Tools)

### Suggest Soil sample locations

#### method

- **GenSampleLocations(method: String, numSamples: Double, boundedGrids: List[either(Paddock, Zone)], attributes: 2dAttribute)**: _List[(Double, Double)]_

#### example

```scala
val samplesLocationsAll = samsFarm.GenSampleLocations("clhc", 10) // whole farm, all  2dAttributes
val samplesLocationsSouth = samsFarm.GenSampleLocations("clhc", 10, paddocks = [paddock01, paddock02], attributes = ["ndvi", "uGamma"])
val samplesLocationsZones = samsFarm.GenSampleLocations("clhc", 3, [zone01])

println(samplesLocationsZones) // [(-33.466644, 151.217701), (-33.466677, 151.217722),(-33.466683, 151.217755)]
samplesLocationsZones.toFile("path/to/file")
```

### Convert Attributes to new Attribute

#### method

- **unlockAttributes(attributeNames: List[String])**

#### properties

- **availableAttributes**: _List[String]_

#### example

```scala
println(samsFarm.available1dAttributes) // ["awc", "dul"]
println(samsFarm.available2dAttributes) // ["bulkDensity"]

println(samsFarm.getPaddocks()[0].attributeNames()) // ["clay"m "bd"]
samsFarm.unlockAttributes(["awc"])
println(samsFarm.getPaddocks()[0].attributeNames()) // ["clay"m "bd", "awc"]
```

### Create 3D digital soil map

#### method

- **createDSM(filePath: String)**: _List[((Double, Double), boundedGrid)]_

List for each depth range

#### example

```scala
samsFarm.createDSM("path/to/out/dir")
samsFarm.createDSM("path/to/out/dir", [paddock01, paddock02], ["clay"])
```
