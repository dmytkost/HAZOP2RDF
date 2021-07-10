# Problem Analysis

here, an analysis section would be nice. from your motivation and state of the art, you should derive a list 
of requirements that your concept later on should solve. e.g.:
- HAZOPs need to be stored
- HAZOPs need to be machinereadable
- HAZOPs need to be reusable
- HAZOPs need to have a clear onthology that allows for interfacing and combining multiple modul HAZOPs into a full plant HAZOP

The classic HAZOP risk analysis was developed in the 1970s by (insert citation) with the processes and tools available at the time. Today this analysis is widely done manually in Excel spreadsheets. While those are easy to work in and readable for humans, they present a barrier to our vision of a truly modular plant. Excel sheets do not provide structures that are are machine readable.  Since the results are stored in large packed tables for each individual plant, they also do not allow an accessible way of storing and reading them that would allow for an opportunity to reuse the work that was put into them, making them essentially one time use. Furthermore, the onthology used, in human readable form, is not rigid enough to apply semantic to it, hindering any automatic processing.

These inefficiencies can be remedied by converting the large HAZOP excel tables into an easier and better to handle format. We propose the use of a Resource Description Framework onthologie, short RDF, instead of the classic Excel approach. RDF othologies give themselves to easy storage, local or on designated servers. They are machine readable and combined with it's wide level of adaption and easy to handle language, RDF HAZOPs solve the problem of reusability, saving both work and time in the plant building process. The queriable nature of RDF databases creates the possiblity for automatic interfacing between individual module HAZOPs, analogous to the mechanical and electrical interfacing they already possess.

We recognize the advantages of Excel spreadsheets in the process of creating HAZOP safety studies and further believe in giving the safety engineers the maximum amount of freedom to conduct their primary work in a way that suits their personal workflow best. Thus we believe the best way to impliment this solution is to create an Importer/Exporter and database that converts Excel sheets, which are easy to read for humans, to RDF onthologies and vise-versa.
