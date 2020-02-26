import requests
import re
from bs4 import BeautifulSoup


class Scanner(object):
    def __init__(self, top_level_element, top_level_attribute,
                 key_element, key_attribute,
                 qualifier_el, qualifier_val,
                 starting_page, pagination_string,
                 url):
        # Params
        self.top_level_element = top_level_element
        self.top_level_attribute = top_level_attribute
        self.key_element = key_element
        self.key_attribute = key_attribute
        self.qualifier_attr = qualifier_el
        self.qualifier_val = qualifier_val
        self.base_url = url
        self.url = self.base_url

        # Pagination
        # If pagination_enabled is set to false, you still have to provide the starting page and pagination string vars
        self.pagination_enabled = True
        self.starting_page = starting_page
        self.current_page = starting_page
        self.pagination_string = pagination_string
        self.yielded_results = True

        # Output
        self.html_contents = ""
        self.soup = BeautifulSoup
        self.results_list = []

    def scrape(self):
        self.html_contents = requests.get(self.url).text

        self.soup = BeautifulSoup(self.html_contents, "html5lib")

        local_results_list = []

        for found in self.soup.findAll(self.top_level_element, self.top_level_attribute):
            for link in found.find_all(self.key_element, self.key_attribute, href=True):
                # What you don't want to take, if you want all of the elements selected above,
                # provide class as the qualifier_el and hidden as the qualifier_val
                # if it is the case that the class is hidden, you don't want that link anyways
                match_pattern = re.compile(self.qualifier_val)
                url_pattern = re.compile(
                        r'^(https?:\/\/)?(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+[\w]{2,}(?=\/[a-zA-Z0-9/\-])'
                )
                url_root = re.match(url_pattern, self.url).group()

                if isinstance(link[self.qualifier_attr], list):
                    if not re.match(match_pattern, link[self.qualifier_attr][0]):
                        if not re.match(r'https?:\/\/', link['href']):
                            local_url = url_root + link['href']
                        else:
                            local_url = link['href']
                        if local_url not in local_results_list:
                            local_results_list.append(local_url)
                else:
                    if not re.match(match_pattern, link[self.qualifier_attr]):
                        if not re.match(r'https?:\/\/', link['href']):
                            local_url = url_root + link['href']
                        else:
                            local_url = link['href']
                        if local_url not in local_results_list:
                            local_results_list.append(local_url)

        if len(local_results_list) > 0:
            self.results_list.extend(local_results_list)
        else:
            self.yielded_results = False

    def dump(self):
        print(len(self.results_list))
        for link in self.results_list:
            print(link)
        return self.results_list

    def run(self):
        print(self.pagination_enabled)
        if self.pagination_enabled:
            while self.yielded_results:
                url_page = self.base_url + self.pagination_string + str(self.current_page)
                self.url = url_page
                self.scrape()
                self.current_page += 1
            return self.dump()
        else:
            self.scrape()
            return self.dump()
