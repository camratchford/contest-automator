import requests
import csv
from bs4 import BeautifulSoup


class Scanner(object):
    def __init__(self, top_level_element, top_level_attribute,
                 key_element, key_attribute,
                 qualifier_el, qualifier_val, url):
        # Params
        self.top_level_element = top_level_element
        self.top_level_attribute = top_level_attribute
        # self.key_nth_child = key_nth_child
        self.key_element = key_element
        self.key_attribute = key_attribute
        self.qualifier_el = qualifier_el
        self.qualifier_val = qualifier_val
        self.url = url

        # Pagination
        self.yielded_results = True

        # Output
        self.html_contents = ""
        self.soup = BeautifulSoup
        self.results_list = []

    def scrape(self):
        self.html_contents = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_contents, "html5lib")

        print(self.url)
        local_results_list = []
        for found in self.soup.findAll(self.top_level_element, self.top_level_attribute):
            for link in found.find_all(self.key_element, self.key_attribute, href=True):
                if link[self.qualifier_el][0] != self.qualifier_val:
                    local_results_list.append(link["href"])
        if len(local_results_list) > 0:
            print(len(local_results_list))
            self.results_list.append(local_results_list)
        else:
            self.yielded_results = False

    def dump(self):
        print(self.results_list)
        # with open("test_output.csv", "w", newline='') as my_csv:
        #     writer = csv.writer(my_csv)
        #     for row in self.results_list:
        #         writer.writerow(row)
        return 0


def main():
    top_level_el = "header"
    top_level_attribute = {"class": "entry-header"}
    key_el = "a"
    key_attribute = {"href": ""}
    qualifier_el = "rel"
    qualifier_val = "author"
    url = "https://leitesculinaria.com/category/giveaways"
    pagination = "/page/"
    page = 1
    scanny = Scanner(top_level_el, top_level_attribute, key_el, key_attribute, qualifier_el, qualifier_val, url)
    while scanny.yielded_results:
        url_page = url + pagination + str(page)
        scanny.url = url_page
        scanny.scrape()
        page += 1
    scanny.dump()


if __name__ == "__main__":
    main()
