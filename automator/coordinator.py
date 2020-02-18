
class Coordinator(object):
    def __init__(self):
        self.scanner_url = ""
        self.scanner_top_level_element = ""
        self.scanner_top_level_attribute = {}
        self.scanner_key_element = ""
        self.scanner_key_attribute = {}
        self.scanner_qualifier_el = ""
        self.scanner_qualifier_val = ""
        self.scanner_pagination_enabled = bool
        self.scanner_starting_page = int
        self.scanner_pagination_string = ""

        self.filler_key_pairs = {}
        self.filler_submit_element = ""
        self.filler_first_click = bool
        self.filler_first_click_el = ""
        self.filler_popups = bool
        self.filler_popup_el = ""

    def load_json(self, path):
        import json
        with open(path) as f:
            json_data = json.load(f)

        self.scanner_url = json_data["scanner_url"]
        self.scanner_top_level_element = json_data["scanner_top_level_element"]
        self.scanner_top_level_attribute = json_data["scanner_top_level_attribute"]
        self.scanner_key_element = json_data["scanner_key_element"]
        self.scanner_key_attribute = json_data["scanner_key_attribute"]
        self.scanner_qualifier_el = json_data["scanner_qualifier_el"]
        self.scanner_qualifier_val = json_data["scanner_qualifier_val"]
        self.scanner_pagination_enabled = json_data["scanner_pagination_enabled"]
        self.scanner_starting_page = json_data["scanner_starting_page"]
        self.scanner_pagination_string = json_data["scanner_pagination_string"]

        self.filler_key_pairs = json_data["filler_key_pairs"]
        self.filler_submit_element = json_data["filler_submit_element"]
        self.filler_first_click = json_data["filler_first_click"]
        self.filler_first_click_el = json_data["filler_first_click_el"]
        self.filler_popups = json_data["filler_popups"]
        self.filler_popup_el = json_data["filler_popup_el"]
        
    def run(self):
        from automator.scanner import Scanner
        from automator.filler import Filler

        scanny = Scanner(self.scanner_top_level_element, self.scanner_top_level_attribute,
                         self.scanner_key_element, self.scanner_key_attribute,
                         self.scanner_qualifier_el, self.scanner_qualifier_val,
                         self.scanner_starting_page, self.scanner_pagination_string, self.scanner_url)

        scanny.pagination_enabled = self.scanner_pagination_enabled
        scanny.starting_page = self.scanner_starting_page
        scanny.pagination_string = self.scanner_pagination_string

        contest_list = scanny.run()

        filly = Filler(self.filler_key_pairs, self.filler_submit_element, contest_list)
        filly.first_click = self.filler_first_click
        filly.first_click_el = self.filler_first_click_el
        filly.popups = self.filler_popups
        filly.popup_el = self.filler_popup_el

        filly.fill()



def leitesculinaria():
    top_level_el = "header"
    top_level_attribute = {"class": "entry-header"}
    key_el = "a"
    key_attribute = {"href": ""}
    qualifier_el = "rel"
    qualifier_val = "author"
    page = 1
    pagination_string = "/page/"
    url = "https://leitesculinaria.com/category/giveaways"

    scanny = Scanner(top_level_el, top_level_attribute,
                     key_el, key_attribute,
                     qualifier_el, qualifier_val,
                     page, pagination_string, url)

    contest_list = scanny.run()

    keypairs = {"//input[@id='giveaway_entry_name']": "Cameron Ratchford",
                "//input[@id='giveaway_entry_email']": "cjratchford@hotmail.com"}

    submit = "//input[@value='Enter']"

    filly = Filler(keypairs, submit, contest_list)
    filly.fill()


def steamkitchen():
    top_level_el = "div"
    top_level_attribute = {"class": "archives"}
    key_el = "a"
    key_attribute = {"href": ""}
    qualifier_el = "title"
    qualifier_val = "Past Winners"
    url = "https://steamykitchen.com/current-giveaways"
    pagination = ""
    page = 0
    scanny = Scanner(top_level_el, top_level_attribute,
                     key_el, key_attribute,
                     qualifier_el, qualifier_val,
                     page, pagination,
                     url)

    scanny.pagination_enabled = False

    contest_list = scanny.run()

    keypairs = {"//input[@id='skg_first_name']": "Cameron",
                "//input[@id='skg_last_name']": "Ratchford",
                "//input[@id='skg_email']": "cjratchford@hotmail.com"}

    submit = "//input[@id='skg_submit_button']"

    filly = Filler(keypairs, submit, contest_list)
    filly.fill()


def idropnews():
    top_level_el = "article"
    top_level_attribute = {"class": "giveaway-container box-shadow-nohover gac-hide"}
    key_el = "a"
    key_attribute = {"href": ""}
    qualifier_el = "class"
    qualifier_val = "hidden"
    url = "https://www.idropnews.com/giveaways/"
    pagination = ""
    page = 0
    scanny = Scanner(top_level_el, top_level_attribute,
                     key_el, key_attribute,
                     qualifier_el, qualifier_val,
                     page, pagination,
                     url)

    scanny.pagination_enabled = False

    contest_list = scanny.run()
    print(contest_list)

    keypairs = {"//input[@name='name']": "Cameron Ratchford",
                "//input[@name='email']": "cjratchford@hotmail.com"}

    submit = ["//span[text()='I am at least 18 years of age (required)']",
              "//input[@uib-tooltip'Please complete your details to continue']"]

    filly = Filler(keypairs, submit, contest_list)
    filly.popups = True
    filly.popup_el = ["//button[text()='Allow']"]
    filly.first_click = True
    filly.first_click_el = "//a[@href='https://gleam.io/cookiefix?sa=https://gleam.io/wB4Ag/idrop-news-apple-iphone-11-pro-max-giveaway%3Fl%3Dhttps%253A%252F%252Fwww.idropnews.com%252Fgiveaways%252Fapple-iphone-11-pro-max-giveaway%252F117362%252F%26r%3D%26xdga%3D424950440.1581364605%26xdga_referrer%3D']"
    filly.fill()

