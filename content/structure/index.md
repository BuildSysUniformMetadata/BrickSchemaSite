---
date: 2016-09-08T15:15:41-07:00
menu: main
title: Documentation
weight: 3
---

`Brick` adheres to the RDF data model ([Resource Description Framework](https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140225/)), which
represents knowledge as a graph expressed as triples: `subject, predicate, object`

Applications and services can query the RDF representation of a building using
SPARQL ([SPARQL Protocol and RDF Query Language](https://www.w3.org/TR/rdf-sparql-query/)).

See [downloads](/source) to get the source files of Brick.


## Brick Concepts
Our research paper describes Brick design and development in depth ([link to paper](/papers/Brick-BuildSys2016.pdf)). Here we highlight the essential concepts of Brick.

### Tagset
Every entity in the buildings is represented by a Tagset, which is decomposed to multiple Tags. 
We model Point, Equipment, Location, and MeasurementProperty as entities in buildings. These are organized into a hierarchy.
![Class hierarchy of Brick][hierarchy_image]

[hierarchy_image]: /images/class_hierarchy.png 

As an example, *Room Temperature Sensor* is a Tagset that consists of Tags, *Room*, *Temperature*, and *Sensor*.
Tagsets have a hierarchy depending on the granularity of entity definitions. *Room Temperature Sensor* is a type of *Temperature Sensor*. For example, one can find a collection of temperature sensors easily with this hierarchy.
One can also add new Tagsets with Tags if it is not defined in our schema. (We encourage you to share your custom Tagsets with us to make `Brick` more comprehensive ([Issues](https://github.com/BuildSysUniformMetadata/GroundTruth/issues)).)
 

### Tags
Tags represent unit concept in buildings and constitute Tagsets. Tags are used to ifer Tagsets' meaning especially for custom Tagsets.
One can easily know *Room Temperature Sensor* is related to *Room*, *Temperature*, and *Sensor* programatically.
This moderates tag-based representation mechanisms to have more coverage.
 

### Properties
Properties represent relationships among entities. An entity, which is an instance of Tagset, may have properties to explain relationships with others.
`Brick` has following properties. We contrain subjects and objects that properties can have. We will support tool chains to validate the constraints.

| Property Name |               Definition              | Subject | Object |
|:-------------:|:-------------------------------------:|:-------:|:------:|
|  isLocatedIn  |           A is located in B.          |         |Location|
|    controls   | A determines the internal state of B. |         |        |
|    isPartOf   |      A is a component/part of B.      |         |        |
|    hasPoint   | A has a point B that functions for A. |Equipment| Point  |
|     feeds     |      Something flows from A to B.     |         |        |


## Viewing Brick Files

[http://viewer.brickschema.org/](http://viewer.brickschema.org/) has a simple `.ttl` file viewer that allows you to see the structure of Brick building files.
[Here](http://viewer.brickschema.org/static/soda.pdf) is an example output for Soda Hall at UC Berkeley.
