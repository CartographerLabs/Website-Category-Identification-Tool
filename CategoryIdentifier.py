import json
import re
import sys

import Website


class Identifier:
    '''
    This class reads in a valid json config and takes a website object, it then compares the config
    with the website to identify if the specified website meets the criteria of the config.
    '''

    _website = Website
    _blacklisted = []
    _whitelisted = []
    _keyword_and_threshold = {}
    _threshold_for_length = {}

    def __init__(self, website, config_file_location):
        '''
        Constructor.
        :param website:
        :param config_file_location:
        '''

        self._website = Website
        self._blacklisted = []
        self._whitelisted = []
        self._keyword_and_threshold = {}
        self._threshold_for_length = {}

        self._website = website
        self._read_json(config_file_location)

    def _get_count_of_word_in_website(self, keyword):
        '''
        Uses regex to find all occurances of the proivided keyword in the website url and content.
        :param keyword:
        :return: amount of times the keyword is found in the website url and content.
        '''
        occurances_in_url = len(re.findall(keyword, self._website.website_url))
        occurances_in_website = self._count_occurances(keyword, self._website.website_content)

        return occurances_in_url + occurances_in_website

    def _get_length_of_body(self):
        '''
        Gets the total length of the website's body.
        :return: the length of the website's body.
        '''
        total_length = 0
        for item in self._website.body_text:
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

        for website in self._whitelisted:
            if re.search(website, self._website.website_url):
                return True

        return False

    def _is_website_in_hardcoded_blacklist(self):
        '''
        Checks if the website is in the list of specified blacklist websites
        :return: boolean on if in blacklist
        '''

        for website in self._blacklisted:
            if re.search(website, self._website.website_url):
                return True

        return False

    def _read_json(self, config_location):
        '''
        Reads in a json config and sets the appropriate member variables
        :param config_location:
        '''
        with open(config_location) as json_file:
            data = json.load(json_file)

            self._whitelisted = data['white_listed_websites']
            self._blacklisted = data['black_listed_websites']
            self._threshold_for_length = data['body_length_threshold']
            self._keyword_and_threshold = data['keyword_and_threshold']

    def is_match(self):
        '''
        Is used to identify if the provided website meets the specification of the provided config.
        :return: boolean on if website identified with config.
        '''

        # Sets if the URL is in the whitelist o blacklist
        is_blacklisted = self._is_website_in_hardcoded_blacklist()
        is_whitelisted = self._is_website_in_hardcoded_whitelist()

        # Checks if the body length is in the threshold range
        length_of_body = self._get_length_of_body()

        min_body_length = self._threshold_for_length["min"]
        max_body_length = self._threshold_for_length["max"]

        # If N/A is provided then it should set the max value to the maximum size of
        # an int (Now there is an edge case here where the size of the body is bigger than this),
        # and the min value to 0.
        if max_body_length == "n/a":
            max_body_length = sys.maxsize

        if min_body_length == "n/a":
            min_body_length = 0

        if min_body_length < length_of_body < max_body_length:
            in_body_length_threshold = True
        else:
            in_body_length_threshold = False

        # Loops through all items in the dictionary and if the amount of times any of the keywords shows up
        # in the website is higher than their threshold it breaks the loop and returns true.
        is_higher_than_keyword_threshold = False
        for key_word in self._keyword_and_threshold:
            threshold = self._keyword_and_threshold[key_word]
            count_of_keyword = self._get_count_of_word_in_website(key_word)

            if count_of_keyword > threshold:
                is_higher_than_keyword_threshold = True
                break

        # Returns on if the website has been identified with the descriptors in the config
        is_a_match = False
        if is_whitelisted:
            is_a_match = True
        elif is_blacklisted:
            is_a_match = False
        elif is_higher_than_keyword_threshold and in_body_length_threshold:
            is_a_match = True

        return is_a_match
