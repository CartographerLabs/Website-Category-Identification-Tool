# Website Category Identification Tool
This is a quick script created in Python that can be provided with a JSON configuration to identify websites that fit a specific criteria. Currently this criteria is broken down into several categories:
- The URL is in a whitelist
- The URL is not in a blacklist
- The URL's content includes a keyword (e.g. 'news','cooking' or 'sport') more than a given threshold of times. 
- The website's body length if over a given character length.

## Requirements
All requirements are stored in the requirements.txt file. 
```bash
pip install -r requirements.txt
```

## Usage 
The below example details how the website ``http://www.bbc.com`` is compared against a configuration used to identify news websites. 
```python
from TextInWebsiteDetector import BaseDetector
from Website import Website

my_website = Website("http://www.bbc.com")
my_detector = BaseDetector(my_website,"newsDetector.json")
print(my_website.website_url + " " + str(my_detector.has_detected()))
```
Example configuration:

```json
{
  "keyword_and_threshold": {
    "news": 7
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
    "bristol.ac.uk"
  ],
  "max_body_length_threshold": 7000
}
```