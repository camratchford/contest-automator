from selenium import webdriver


class Filler(object):
    def __init__(self, key_pairs, submit_element, url_list):
        self.key_pairs = key_pairs
        self.submit_element = submit_element
        self.url_list = url_list

    def fill(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium"
        driver = webdriver.Chrome(chrome_options=options)
        for url in self.url_list:
            driver.get(url)
            for key in list(self.key_pairs.keys()):
                element = driver.find_element_by_id(key)
                element.send_keys(self.key_pairs[key])
            submit = driver.find_element_by_id(self.submit_element)
            submit.click()




