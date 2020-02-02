from CategoryIdentifier import Identifier
from Website import Website

my_website = Website("https://www.bbc.co.uk/news/health-51345279")
my_identifier = Identifier(my_website, "newsDetector.json")

if my_identifier.is_match():
    print("The website {} is a news website.".format(my_website.website_url))
else:
    print("The website {} is not a news website.".format(my_website.website_url))