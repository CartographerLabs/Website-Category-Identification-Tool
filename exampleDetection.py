from CategoryIdentifier import Identifier

website_url = "https://www.bbc.co.uk/news/health-51345279"
my_identifier = Identifier(website_url, "newsDetector.json")

if my_identifier.is_match():
    print("The website {} is a news website.".format(website_url))
else:
    print("The website {} is not a news website.".format(website_url))