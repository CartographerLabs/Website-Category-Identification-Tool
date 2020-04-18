# Website Category Identification Tool
This is a quick script created in Python that can be provided with a JSON configuration to identify websites that fit a specific criteria. Currently this criteria is broken down into several categories:
- The URL is in a whitelist
- The URL is not in a blacklist
- The URL's content includes a keyword (e.g. 'news','cooking' or 'sport') more than a given threshold of times and the website's body length is within a given character length range (e.g. between 0 and 1000, or above 7000)

## Installation
All requirements are stored in the requirements.txt file or in the virtual environment provided. 
```bash
pip install -r requirements.txt
```

## Usage 
The below example details how the website ``http://www.bbc.com`` is compared against a configuration used to identify news websites. 

Two objects are required: a ```Website``` object - which is used to store information about a given website (e.g. URL, body text, titles, etc), and an ```Identifier``` object - which is provided with a ```Website``` and a criteria (taking the form of a JSON configuration) and has an ```.is_match()``` method which returns ```True``` if the website meets the criteria of the config or ```False``` if it does not. If any of the above criteria match (Whietlist, Blacklist, or keyword amount **and** length range) then a match will be True.

```python
from CategoryIdentifier import Identifier
from Website import Website

my_website = Website("https://www.bbc.co.uk/news/health-51345279")
my_identifier = Identifier(my_website, "newsDetector.json")

if my_identifier.is_match():
    print("The website {} is a news website.".format(my_website.website_url))
else:
    print("The website {} is not a news website.".format(my_website.website_url))
```
Example configuration:

```json
{
  "keywords_and_thresholds": {
    "news": 8
  },
  "white_listed_websites": [
    "news.yahoo.com",
    "hindustantimes.com",
    "thehindu.com",
    "theverge.com",
    "cnn.com",
    "nytimes.com",
    "foxnews.com",
    "dailymail.co.uk",
    "washingtonpost.com",
    "theguardian.com",
    "abcnews.go.com",
    "usatoday.com",
    "thedailybeast.com",
    "nationalgeographic.com",
    "euronews.com",
    "reuters.com",
    "bbc.com",
    "independent.co.uk",
    "news.sky.com",
    "express.co.uk"
  ],
  "black_listed_websites": [
    "github.com",
    "bristol.ac.uk",
    "twitter.com",
    "t.co",
    "facebook.com"
  ],
  "body_length_threshold": {
    "min": 1000,
    "max": "n/a"
  }
}
```
