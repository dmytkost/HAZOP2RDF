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

## Motivation

Modular plants are getting more and more important in today's industry. They enable flexible production in 
small quantities and over variable time periods. A modular plant can be built very quickly, because all 
interfaces are compatible, but a HAZOP analysis of the entire plant is still necessary, which strongly 
limits the advantages of modularity. 

In order to meet high safety standards a hazard and operability study, 
short HAZOP has to be conducted on all parts of the modular plant.

The HAZOP risk analysis is an important part of every safety concept of industrial plants.
This analysis is done manually and individually in Excel. Since it is done in large packed tables it can not
be automated or reused. This inefficiency can be remedied by converting the large HAZOP excel tables into an
easier and better to handle format. 

The Resource Description Framework, short RDF can be such a format. Because of its easy to handle language, 
reusability and automatability we choose this widely spread format. 

Through the usage of a DB Server like Fuseki, the transformed file can be shared and stored very conveniently.

One of the biggest problem we faced was to verify and define a well-formed excel spreadsheet so that our importer
was able to generate a correct RDF file. Now the verification process uses a user defined configuration to analyse 
the excel spreadsheet and import it. The importer had to be able to distinguish between meaningful and useless 
Hazop-Cases inside the spreadsheet.