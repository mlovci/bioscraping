#Bioscraping

Web scrapers to interact with remote databases programatically in Python 
that makes a local cache of web data with sqlite3 to prevent excessive web 
traffic.

So far, implemented:

* [Uniprot](http://uniprot.org) by uniprot protein ID. (e.g. 'Q8BP71')
* [PubMed](www.ncbi.nlm.nih.gov/pubmed/) by PMID (e.g. '24213538')
  
#Install

##Python 2.7.x and 3.x
`pip install .`

#Test

Real unit tests are absent, but you can test basic functionality with 
`python test/not_a_real_test.py`.

#Usage

##PubMed
    from bioscraping import PubMedClient
    
    pubmed = PubMedClient()

defaults to writing a file called `.bioscraping.pubmed.sqlite.db`

    pubmed.fetch(<PMID>)
    
Returns text with author and abstract for PMID. 

##Uniprot

    from bioscraping import UniprotClient
    
    uniprot = UniprotClient()

defaults to writing a file called `.bioscraping.uniprot.sqlite.db`

    uniprot.fetch(<Uniprot ID>)

Returns a dictionary of data parsed from xml.

#Buyer beware

UniprotClient has a potential race condition and tempfile needs to be 
implemented before it is safe for concurrent processes. (see TODO)
