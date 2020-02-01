import json
import re
import Website


class BaseDetector:
    '''
    This class reads in a valid json config and takes a website object, it then compares the config
    with the website to identify if the specified website meets the criteria of the config.
    '''

    website = Website
    blacklisted = []
    whitelisted = []
    keyword_and_threshold = {}
    threshold_for_length = 0

    def __init__(self, website, config_file_location):
        '''
        Constructor
        :param website:
        :param config_file_location:
        '''

        self.blacklisted = []
        self.whitelisted = []
        self.keyword_and_threshold = {}
        self.threshold_for_length = 0

        self.website = website
        self._read_json(config_file_location)

    def _get_count_of_word_in_website(self, keyword):
        '''
        Uses regex to find all occurances of the proivided keyword in the website url and content.
        :param keyword:
        :return: amount of times the keyword is found in the website url and content.
        '''
        occurances_in_url = len(re.findall(keyword, self.website.website_url))
        occurances_in_website = self._count_occurances(keyword,self.website.website_content)

        return occurances_in_url + occurances_in_website

    def _get_length_of_body(self):
        '''
        Gets the total length of the website's body.
        :return: the length of the website's body.
        '''
        total_length = 0
        for item in self.website.body_text:
            total_length =  total_length + len(item)

        return total_length

    def _count_occurances(self, regex_string_to_count, website_content):
        '''
        uses regex to count how often a string regex string occurs in a provided string.
        :param regex_string_to_count:
        :param website_content:
        :return: number of occurances
        '''
        regex_string_to_count = regex_string_to_count.lower()
        amount_counted = 0

        website_content = str(website_content).lower()
        amount_counted = amount_counted + len(re.findall(regex_string_to_count, website_content))
        return  amount_counted

    def _is_website_in_hardcoded_whitelist(self):
        '''
        Checks if the website is in the list of specified whitelisted websites
        :return: boolean on if in whitelist
        '''

        for website in self.whitelisted:
            if re.search(website, self.website.website_url):
                return True

            return False

    def _is_website_in_hardcoded_blacklist(self):
        '''
        Checks if the website is in the list of specified blacklist websites
        :return: boolean on if in blacklist
        '''

        for website in self.blacklisted:
            if re.search(website, self.website.website_url):
                return True

            return False

    def _read_json(self, config_location):
        '''
        Reads in a json config and sets the appropriate member variables
        :param config_location:
        '''
        with open(config_location) as json_file:
            data = json.load(json_file)

            self.whitelisted = data['white_listed_websites']
            self.blacklisted = data['black_listed_websites']
            self.threshold_for_length = data['max_body_length_threshold']
            self.keyword_and_threshold = data['keyword_and_threshold']

    def has_detected(self):
        '''
        Is used to identify if the provided website meets the specification of the provided config.
        :return: boolean on if website identified with config.
        '''
        is_blacklisted = self._is_website_in_hardcoded_blacklist()
        is_whitelisted = self._is_website_in_hardcoded_whitelist()

        length_of_body = self._get_length_of_body()

        if length_of_body >= self.threshold_for_length:
            is_higher_than_length_threshold = True
        else:
            is_higher_than_length_threshold = False

        # Loops through all items in the dictionary and if the amount of times any of the keywords shows up
        # in the website is higher than their threshold it breaks the loop and returns true.
        is_higher_than_keyword_threshold = False
        for key_word in self.keyword_and_threshold:
            threshold = self.keyword_and_threshold[key_word]
            count_of_keyword = self._get_count_of_word_in_website(key_word)

            if count_of_keyword > threshold:
                is_higher_than_keyword_threshold = True
                break

        # Returns on if the website has been identified with the descriptors in the config
        has_this_website_been_detected = False
        if is_whitelisted:
            has_this_website_been_detected = True
        elif is_blacklisted:
            has_this_website_been_detected = False
        elif is_higher_than_keyword_threshold or is_higher_than_length_threshold:
            has_this_website_been_detected = True

        return has_this_website_been_detected
