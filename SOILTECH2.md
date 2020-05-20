# SoilTech Library Design

## preface

This document is intended to be a collection of suggestions on how best to structure and refactor the current codebase to become a working library with intuitive API design. The perspective held, whilst making this document, is in the form of a software engineer attempting to integrate the soiltech tools with the guidance of an agronomist. Therefore the object structure and names will have to reflect existing agricultural structures (Tools, Zone, Sample...). Lastly, when practical, the UI (API) should be abstracted away from the underlying science and statistical methods for basic usage; but still, be accessible.

### ZoneAttribute(attributeName: String, grid: RDD[((Double,Double),Double)], unit: String, type: String, lifeSpan: Double)

- **name**: Attribute Name - "clay", "ndvi", "elevation"
- **type**: Attribute Type - "static", "dynamic", "cyclic"
- **unit**: Attribute Type - "m", "mm",
- **lifespan**: (Only dynamic samples) Period that the reading is valid - 0.25 years
- **lifecycle**: (only cyclic samples) Period that the reading should generally repeat - 1 year
- **date**: Date that the reading was taken
- **weighting**: Importance weighting. Useful for creating PMZ
- **managed**: true, false

  #### Methods

Used to set or return properties

- name()
- type()
- unit()
- lifespan()
- lifecycle()
- date()
- weighting()
- managed()

### Zone(boundary: List[List[(Double,Double)]], type: String)

- **boundary** - The boundary of the Zone
- **type** of zone: "Paddock", "Potential", "Management"

#### methods

- **addAttribute(attribue: GridAttribute)**:
- **AllAttributes()** _Map[(String,2dAttribute)]_
- **Attribute(attributeName: String)**: _2dAttribute_
- **removeAttribute(attributeName: String)**

#### properties

- **attributeNames()**: _List[String]_
- **boundary()**: _Boundary_ -

```scala
Import org.soiltech.agriculture.{Tools, Zone, Sample, ZoneAttribute, SampleAttribute}

// ndviGrid of type RDD[((Double,Double),Double)]

val ndvi = ZoneAttribute("ndvi", ndviGrid, "", "cyclic", 1.0, "05-05-2020", 1, false)
val elevation = ZoneAttribute("elevation", elevationGrid, "m", "static", "05-05-2020", 1, false)
val ugamma = ZoneAttribute("ugamma", ugammaGrid, "", "dynamic", 5.0, "05-05-2017", 1, false)
val kgamma = ZoneAttribute("kgamma", kgammaGrid, "", "dynamic", 5.0, "05-05-2017", 1, false)

// boundary01 type List[List[(Double,Double)]]

val paddock01 = Zone(boundary01, "Paddock")
paddock01.addAttribute(ndvi)
paddock01.addAttribute(elevation)
paddock01.addAttribute(ugamma)
paddock01.addAttribute(kgamma)
```

--------------------------------------------------------------------------------

# OLD

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

## Sample(location: (Double,Double), date: String)

### methods

- **addAttribute(attributeName: Sting, depthRanges: List[(Double, Double)], values: List[Double])**: _1dAttribute_
- **getAttribute(attributeName: String)**: _1dAttribute_
- **removeAttribute(attributeName: String)**

### properties

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

### Creating Zones

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
