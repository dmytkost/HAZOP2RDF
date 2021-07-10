# Introduction

Hazard  and  Operability  (HAZOP)  studies  are  conducted  to  identify and assess hazards and malfunctions that 
arise from processes and process plants. The  HAZOP  methodology  is  a  human-centered  and  moderated  technique,  
and  it  is  conducted  by  an  interdisciplinary  team  of  experts. (@Single2020_Computer_Aided_Hazop)

For over 30 years, different research groups proposed rule-based expert  systems  or  graph-based  approaches  in  
order  to  automate  HAZOP  studies,  see  (@Single2019_State_of_research).  Like (@Rodriguez2019_An_Ontology) our 
software makes  use  of  a promising ontology-based technology.

Being able to convert excel spreadsheets to the RDF format is a huge time saver for engineers working with HAZOP 
studies. By analyzing the structure of the HAZOP files, we can draw conclusions about the risks of a plant. To do 
so we started by writing sophisticated code to develop an engine that transforms the lines of HAZOP study excel 
spreadsheet into an RDF turtle formatted code.

In the following parts of this paper, it is shown what our software is capable of, how we solved our problem and 
how the different commands of our command line interface can be used to ease the process of handling HAZOP studies.

It can be noted that our software can be especially useful when designing a modular plant with multiple HAZOP 
studies for each part of the plant.

## Motivation

In the ever more connected world of the twenty-first century consumer and supplying industry trends are changing 
faster than ever. Digital ordering of products from all over the world with the click of a button and one-click 
setups of internet store fronts that offer these products are creating a new set of demands for the global supply 
chain and the plants that form that chain. Gone are the days of large scale, single purpose plants and factories 
that can only create one product, no matter the market conditions. This realizing has become undeniable in the 
face of the global Covid-19 pandemic that tore apart global supply chains and brutally exposed the inflexibility 
of modern industrial production. First world countries in Europe and the USA faced long lasting and critical 
shortages of trivial items like cotton-swaps and surgical masks, along with simple chemicals like Isopropyl Alcohol. 
While no one would state that the actual production process for these items or compounds are overly complex, the 
setup of traditional single purpose, stationary plants is far too big an undertaking to simply solve a temporary 
shortage or to create a single large batch order from an oversea internet store front company. Not only is the 
planning period too long to solve the temporary but pressing shortage, or supply a onetime order, but the fully 
assembled plant will be underused and uneconomical once the crisis or consumer trend has passed.

The concept of the modular plant attempts to overcome all these limitations, allowing flexible production in small 
or large quantities over variable periods of time. The setup process is far quicker, and therefore more reactive to 
market demands, than that of a traditional plant. All modules are functionally tested and verified on an individual 
basis and are equipped with standardized mechanical and electronic interfaces, thus allowing for much simpler 
planning, construction, and operationality. Safety, however, must always be a top priority, both ethically and from 
a cost, cleanup, and downtime perspective. In order to  meet those high safety standards, a hazard and operability 
study, short HAZOP, must be conducted on all parts of every plant. This study is vital and costly engineering work 
that must be done meticulously. Errors and oversights cost lives and damages that can range into the billions of Euros. 

HAZOP studies today are still created analogous to the stationary plants they are covering. They are single 
purpose and offer no reusability despite the great efforts that go into creating them. Creating HAZOP studies in 
this fashion runs counterintuitive to the idea of the modular plant. Many of the advantages of modularity are lost, 
when a plant can be put together quicker, by less specialized personal, and in the end the ready-to-operate plant 
must stand idle until a classic, from the ground up, HAZOP study is finished. To meet the modern global demands of 
industry the modular plant needs a modular HAZOP. A HAZOP that, just like the module it covers has standardized 
mechanical and electronic interfaces, also has standardized HAZOP interfaces. An interface that allows for a module 
specific HAZOP to be done at the module factory and reused for other modules of the same series, thus creating 
reusability of manual engineering work and allowing for a safety study of a full plant that is just as easy and 
quick to assemble as the modular plant itself.



