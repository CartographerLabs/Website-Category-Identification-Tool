from TextInWebsiteDetector import BaseDetector
from Website import Website

my_website = Website("http://www.bbc.com")
my_detector = BaseDetector(my_website,"newsDetector.json")
print(my_website.website_url + " " + str(my_detector.has_detected()))