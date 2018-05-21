---
date: 2018-05-21T21:42:54Z
title: Schema version 1.0.2
menu: Schema
---

### Schema Files (Turtle format)

- [Brick TagSets](/schema/1.0.2/Brick.ttl): Entity classes with a hierarchy. Major component of Brick.
  - E.g., ``Temperature_Sensor`` is a subclass of ``Sensor``
- [Brick Relationships](/schema/1.0.2/BrickFrame.ttl): Brick relationships and meta-structure constructing TagSets with Tags.
  - E.g., ``sensor1`` is a point of ``vav1``.
- [Brick Tags](/schema/1.0.2/BrickTag.ttl): Tags are subcomponents of all TagSets.
  - E.g., ``Temperature_Sensor`` consists of ``Tempearture`` and ``Sensor``.
- [Brick Dimensions](/schema/1.0.2/BrickUse.ttl): Information dimensions of TagSets.
