import re
import json

class Paper:
    def __init__(self, pmcid, doi, pub_date, references):
        self.pmcid = pmcid
        self.doi = doi
        self.pub_date = pub_date
        self.references = references


def get_pmcids(matching_papers):
    """
    Return a list of pmcids (also subdirectory names) returned by getpapers
    For each line in the index file of matching_papers, strip the
    start of the line (http://europepmc.org/articles/)
    """

    eupmc_header = "http://europepmc.org/articles/"
    pmcids = []

    with open(matching_papers, 'r') as f:
        for line in f:
            if line.startswith(eupmc_header):
                terms = line.split("/")
                pmcids.append(terms[-1].rstrip())

    return pmcids

def get_doi(paper_json):
    paper_doi = paper_json['doi'][0]
    return paper_doi

def get_pub_date(paper_json):
    paper_pub_date = paper_json['journalInfo'][0]['printPublicationDate'][0]
    return paper_pub_date

def get_references(fulltext_xml):

    github_urls = []
    zenodo_urls = []

    urls = re.findall(r'(https?://\S+)(?=\")', fulltext_xml)
    for url in urls:
        if re.match(r'https?://github.com', url) and url not in github_urls:            
            github_urls.append(url)
        elif re.match(r'https?://zenodo.org', url) and url not in zenodo_urls:
            zenodo_urls.append(url)

    references = dict(github=github_urls, zenodo=zenodo_urls)

    return references

def process_paper(pmcid, data_dir):

    doi = ''
    pub_date = ''
    references = {}

    # Name of the Content Mine results file in each paper subdirectory
    filename = data_dir + '/' + pmcid + '/' + 'eupmc_result.json'

    # Process the metadata file
    try:
        with open(filename, 'r') as f:
            paper_json = json.load(f)
            # Get the DOI
            doi = get_doi(paper_json)
            pub_date = get_pub_date(paper_json)
    except IOError:
        print("Error: JSON file does not appear to exist.")

    # Read in the XML full text and mine for the github URLs
    fulltext_file = data_dir + '/' + pmcid + '/' + 'fulltext.xml'

    try:
        with open(fulltext_file, 'r') as f:
            fulltext_xml = f.read()
            references = get_references(fulltext_xml)
    except IOError:
        print("Error: XML file does not appear to exist.")

    paper_info = Paper(pmcid, doi, pub_date, references)

    return paper_info

def process_papers(list_of_pmcids, data_dir):
    '''
    Process a list of papers returned by eupmc

    list_of_pmcids - list of the PMCIDs
    data_dir -  assumed that each paper is in a subdirectory named by
                pmcid in the data_dir
    '''

    papers = []

    for pmcid in list_of_pmcids:
        papers.append(process_paper(pmcid, data_dir))

    return papers
