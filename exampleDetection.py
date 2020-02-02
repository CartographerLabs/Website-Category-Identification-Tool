from CategoryIdentifier import Identifier
from Website import Website

my_website = Website("https://www.bbc.co.uk/news/health-51345279")
my_detector = Identifier(my_website, "newsDetector.json")

if my_detector.is_match():
    print("The website {} is a news website.".format(my_website.website_url))
else:
    print("The website {} is not a news website.".format(my_website.website_url))