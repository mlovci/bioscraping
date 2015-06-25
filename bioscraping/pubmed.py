__author__ = 'lovci'
from ._base import *
class PubMedClient(Scraper):
    """Get paper abstracts by PMID
    >>> pclient = PubMedClient()
    >>> pclient.fetch('24213538')
    '\n1. Nat Struct Mol Biol. 2013 Dec;20(12):1434-42. doi: 10.1038/nsmb.2699. Epub 2013\nNov 10.\n\nRbfox proteins regulate alternative mRNA splicing through evolutionarily\nconserved RNA bridges.\n\nLovci MT(1), Ghanem D, Marr H, Arnold J, Gee S, Parra M, Liang TY, Stark TJ,\nGehman LT, Hoon S, Massirer KB, Pratt GA, Black DL, Gray JW, Conboy JG, Yeo GW.\n\nAuthor information: \n(1)1] Department of Cellular and Molecular Medicine, University of California,\nSan Diego, La Jolla, California, USA. [2] Stem Cell Program, University of\nCalifornia, San Diego, La Jolla, California, USA. [3] Institute for Genomic\nMedicine, University of California, San Diego, La Jolla, California, USA.\n\nAlternative splicing (AS) enables programmed diversity of gene expression across \ntissues and development. We show here that binding in distal intronic regions\n(>500 nucleotides (nt) from any exon) by Rbfox splicing factors important in\ndevelopment is extensive and is an active mode of splicing regulation. Similarly \nto exon-proximal sites, distal sites contain evolutionarily conserved GCATG\nsequences and are associated with AS activation and repression upon modulation of\nRbfox abundance in human and mouse experimental systems. As a proof of principle,\nwe validated the activity of two specific Rbfox enhancers in KIF21A and ENAH\ndistal introns and showed that a conserved long-range RNA-RNA base-pairing\ninteraction (an RNA bridge) is necessary for Rbfox-mediated exon inclusion in the\nENAH gene. Thus we demonstrate a previously unknown RNA-mediated mechanism for AS\ncontrol by distally bound RNA-binding proteins.\n\nPMCID: PMC3918504\nPMID: 24213538  [PubMed - indexed for MEDLINE]\n\n
    """
    base_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"

    @staticmethod
    def _download(pmid):
        url = PubMedClient.base_url

        params = {
            'id':pmid,
            'retmode':'text',
            'rettype':'abstract',
            'db':'pubmed'
            }
        data = urllib.parse.urlencode(params)
        request = urllib.request.Request(url, data)
        full_url = "&".join([url, data])
        print(full_url)
        response = urllib.request.urlopen(request)
        page = response.read(200000).decode("utf-8")

        return full_url, page

    def __init__(self, local_database=".bioscraping.pubmed.sqlite.db", *args,
                 **kwargs):
        super(PubMedClient, self).__init__(local_database=local_database,
                                            *args, **kwargs)