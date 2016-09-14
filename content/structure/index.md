---
date: 2016-09-08T15:15:41-07:00
menu: main
title: Brick Structure
weight: 2
---

`Brick` adheres to the RDF data model ([Resource Description Framework](https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140225/)), which
represents knowledge as a graph expressed as tuples of `(subject, predicate, object)` known as triples.

The `Brick` examples and most of our development has used the Python
[rdflib](https://rdflib.readthedocs.io/en/stable/) library.

Applications and services can query the RDF representation of a building using
SPARQL ([SPARQL Protocol and RDF Query Language](https://www.w3.org/TR/rdf-sparql-query/)).

More detail and some examples will follow soon.

See [Getting Brick](/source) for how to get these files


## Viewing Brick Files

[http://viewer.brickschema.org/](http://viewer.brickschema.org/) has a simple `.ttl` file viewer that allows you to see the structure of Brick building files.
[Here](http://viewer.brickschema.org/static/soda.pdf) is an example output for Soda Hall at UC Berkeley.
