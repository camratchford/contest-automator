
class Coordinator(object):
    def __init__(self, testing_mode):
        self.testing_mode = testing_mode

        self.scanner_url = ""
        self.scanner_top_level_element = ""
        self.scanner_top_level_attribute = {}
        self.scanner_key_element = ""
        self.scanner_key_attribute = {}
        self.scanner_qualifier_attr = ""
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

    def load_json(self, config, account):
        import json
        print(config)

        with open(config) as c:
            json_data = json.load(c)

        # Get list of keys from json config "filler_key_pairs" so we can pull the values
        filler_keys = list(json_data["filler_key_pairs"].keys())

        # Make empty list to store the values in
        # (These are the keys that we need to fetch the corresponding account data)
        account_keys = []

        # Loop through the "filler_key_pairs" dict and return the account_keys
        for key in list(json_data["filler_key_pairs"].keys()):
            account_keys.append(json_data["filler_key_pairs"][key])

        # Make empty list to store the values in
        filler_values = []
        # Loop through the account_keys
        # fetch the values from account needed to fill the self.filler_key_pairs values
        for key in account_keys:
            filler_values.append(account[key])

        # Populate the self.filler_key_pairs dict with your key:value pairs
        for key, value in zip(filler_keys, filler_values):
            self.filler_key_pairs[key] = value

        self.scanner_url = json_data["scanner_url"]
        self.scanner_top_level_element = json_data["scanner_top_level_element"]
        self.scanner_top_level_attribute = json_data["scanner_top_level_attribute"]
        self.scanner_key_element = json_data["scanner_key_element"]
        self.scanner_key_attribute = json_data["scanner_key_attribute"]
        self.scanner_qualifier_attr = json_data["scanner_qualifier_attr"]
        self.scanner_qualifier_val = json_data["scanner_qualifier_val"]
        self.scanner_pagination_enabled = bool(json_data["scanner_pagination_enabled"])
        self.scanner_starting_page = json_data["scanner_starting_page"]
        self.scanner_pagination_string = json_data["scanner_pagination_string"]

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
                         self.scanner_qualifier_attr, self.scanner_qualifier_val,
                         self.scanner_starting_page, self.scanner_pagination_string, self.scanner_url)

        scanny.pagination_enabled = self.scanner_pagination_enabled
        scanny.pagination_string = self.scanner_pagination_string

        contest_list = scanny.run()

        filly = Filler(self.filler_key_pairs, self.filler_submit_element, contest_list, testing_mode=self.testing_mode)
        filly.first_click = self.filler_first_click
        filly.first_click_el = self.filler_first_click_el
        filly.popups = self.filler_popups
        filly.popup_el = self.filler_popup_el

        filly.fill()




