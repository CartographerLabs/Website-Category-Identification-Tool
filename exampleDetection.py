from CategoryIdentifier import Identifier
from Website import Website

my_website = Website("https://www.bbc.co.uk/news/health-51345279")
my_detector = Identifier(my_website, "newsDetector.json")
print(my_website.website_url + " " + str(my_detector.has_met_criteria()))