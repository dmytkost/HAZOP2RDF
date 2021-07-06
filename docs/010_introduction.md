# Introduction

Being able to convert excel spreadsheets to the RDF format is a huge time saver for engineers working with
HAZOP studies. By analysing the structure of the HAZOP files we can draw conclusions about the risks of a plant.

In order to do so we started by writing sophisticated code to develop an engine that transforms the lines
of HAZOP study excel spreadsheet into an RDF turtle formatted code.

In the following parts of this paper it is shown what our software is capable of, how we solved our problem and
how the different commands of our command line interface can be used to ease the process of handling
HAZOP studies.

It can be noted that our software can be especially useful when designing a modular plant with multiple HAZOP
studies for each part of the plant.