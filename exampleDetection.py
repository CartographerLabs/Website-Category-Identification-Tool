from Identifier.CategoryIdentifier import Identifier

website_url = "bbc.co.uk/news/health-51345279"
my_identifier = Identifier(website_url, "Identifier/newsDetector.json")

if my_identifier.is_match():
    print("The website {} is a news website.".format(website_url))
else:
    print("The website {} is not a news website.".format(website_url))