---
date: 2016-04-23T15:21:22+02:00
title: BuildSys 2017
menu: main
weight: 50
---

## Tutorial

A unified metadata schema has an important role in building operation and application interoperability. Brick is a unified metadata schema born from a BuildSys community’s effort on advancing technologies for the built environment. We propose a tutorial session for BuildSys attendants to learn about how to use Brick in their real systems and promote more involvement in Brick development. Interest in Brick from both academia and industry has steadily grown, and a tutorial would be a welcome opportunity to encourage collaboration and discussion.

### Why a new metadata schema?
In existing Building Management Systems (BMS), contextual information (metadata) of sensors, systems and building structures is either absent or not consistently structured. What metadata does exist fails to capture the information needed by modern building applications such as fault detection, energy analysis, and model predictive control. The design of the Brick schema leverages a systematic study of the published literature to identify which things and relationships an effective metadata schema needs to represent.

### Brick Schema
Brick has two main components: a class hierarchy describing the family of building subsystems and the entities and equipment therein, and a minimal, principled set of relationships for describing the associations and connections between those entities. Brick uses these vocabularies to realize a building as a directed, labeled graph. The representation of this graph leverages the standard RDF data model, which means that Brick usage and development can use existing tooling. 

### Agenda
We have planned a two hour tutorial with a focus on hands-on practice by participants. Below we highlight the major sections of the tutorial, their purpose and what we will cover in them.

- Introduction to Brick [15 mins]: Outlining the benefits of a standard metadata such as Brick, and what Brick captures that other schemata do not. We want to clarify the role of Brick and give specific examples of the applications that Brick enables. This would also include examples of how Brick has been integrated with existing building systems. 

    In summary, we will cover: 
    - Basics of Brick schema (RDF, TagSets, relationships)
    - A model system architecture with an existing BMS.

- Brick usage and querying [45 mins]: We introduce the RDF data model and standard SPARQL query language. We will demonstrate how Brick leverages these technologies to represent a real-world building. Using interactive queries, attendees will be able to explore the Brick model for the building. We will walk through a methodology for converting existing building metadata to Brick. Attendees will have the opportunity to implement this methodology on real building metadata including unstructured BMS tags and a simple Haystack model.

    In summary, we will cover:
    - The formal syntax of RDF
    - How to write an RDF of a simplified building
    - How to convert existing BMS points into Brick
    - Introduction to SPARQL with examples

- Writing a real Brick application [45 mins]: We demonstrate the use of Brick in a basic analytics application using timeseries data from a real building. We will address points of how to store Brick instances, how a system exploits Brick instances, and how to query needed information from Brick instances for applications. We will progressively build up a portable building application that queries a Brick model in order to discover the building components  it needs to operate.

    In summary, we will cover:
    - Role of Brick between an existing system and applications
    - How to store a Brick instance and interact with it
    - Find necessary queries for applications
    - How to write queries and write applications on top of them

- Feedback [15 mins]: We would like to communicate with various researchers and practitioners at BuildSys to get feedback on the features they want and possible usability improvements to Brick. Since Brick is open-source and follows a community development process where any contribution is open to public. We would like to promote public contributions to Brick so that it covers every aspect that the real world requires.

     In summary, we will cover:
     - How to contribute to Brick using GitHub and developer Google Group
     - How to add extensions to Brick with request for comments (RFC)
     - Ask for feedback on how to improve Brick

### Logistics

Expected number of participants: 20 - 30

Our tutorial with hands-on practices would attract people who want to have their buildings with normalized metadata.

Participants preparation:

- Registration for guaranteed participation.
- A laptop for hands-on tutorial.
- Facilities:
- Projector and large screen for presenting the tutorial
- Wifi access for all attendees 
- Tables/chairs for all attendees with a clear view of the projector screen

Organizing Team:

- Jason Koh (University of California, San Diego)
- Gabe Fierro (University of California, Berkeley)
- Aslak Johansen (Southern Denmark University)
- Bharathan Balaji (University of California, Los Angeles)
- David Culler (University of California, Berkeley)
- Mani Srivastava (University of California, Los Angeles)
- Rajesh Gupta (University of California, San Diego)
- Yuvraj Agarwal (Carnegie Mellon University)
- Mikkel Kjærgaard (Southern Denmark University)
- Mario Bergés (Carnegie Mellon University)
