# Inception Management Notes

These notes are just so that we can remember what we were doing to get things working.

## Manual Ontology Settings

For the imported ontology, we had to manually set root concepts:

![manual root concept settings](./Images/manual_concepts_settings.png "Inception Menu")

These were:

+ [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)
+ [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)
+ [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

## Layers

Before we got the system working, we had to create a new annotation layer. This followed the instructions from the Google group:



## CAS Doctor

Before the annotations started working we ran the "CAS Doctor" under project administration. It is not clear that that step is what made the annotations start working, but it is what we did. This was done after fixing the root concepts in the KB, and creating the layer in the annotations.
