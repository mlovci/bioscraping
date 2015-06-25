from __future__ import print_function
__author__ = 'lovci'
"""* [Uniprot](http://uniprot.org) by uniprot protein ID. (e.g. 'Q8BP71')
* [PubMed](www.ncbi.nlm.nih.gov/pubmed/) by PMID (e.g. '24213538')
"""
from bioscraping import PubMedClient

pubmed = PubMedClient()

print(pubmed.fetch('24213538'))

from bioscraping import UniprotClient

uniprot = UniprotClient()


print(uniprot.fetch('Q8BP71'))