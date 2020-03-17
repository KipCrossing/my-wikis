# Soiltech

## Project structure (Kip's guide)

This is a guide the will hopefully help contributors understand the project structure.

General usage may be done via the command line interface `CLI.scala`. eg:


```bash
sbt "runMain org.soiltech.helpers.CLI --in ./sample/input --out ./sample/output"
```



### Map - dict opject

### map - method for converting to another object

Can be used on:

- Collection - iterate
- Option - run once
- Future - run once


good methods:

`.filter(bool)`

### Option

For when it can be null

can be either some or None

```scala

```

A good method to use on it is `.getOrElse()`


### Either

can be either right of left
