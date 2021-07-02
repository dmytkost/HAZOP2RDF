# Problem Analysis

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

Thanks to RDF, a HAZOP study can be easily exchanged, edited and combined with other HAZOP studies. Through the usage
of a DB Server like Fuseki, the transformed file can be shared and stored very conveniently.

One of the biggest problem we faced was to verify and define a well-formed excel spreadsheet so that our importer
was able to generate a correct RDF file. Now the verification process uses a user defined configuration to analyse 
the excel spreadsheet and import it. The importer had to be able to distinguish between meaningful and useless 
Hazop-Cases inside the spreadsheet.