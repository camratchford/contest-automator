from selenium import webdriver
from time import sleep


class Filler(object):
    def __init__(self, key_pairs, submit_element, url_list):
        self.key_pairs = key_pairs
        self.submit_element = submit_element
        self.url_list = url_list
        self.first_click = False
        self.first_click_el = ""
        self.popups = False
        self.popup_el = ""

    def fill(self):
        options = webdriver.ChromeOptions()
        options.accept_insecure_certs = True
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=r'/app/automator/chromedriver', chrome_options=options)
        driver.set_window_size(1920, 1080)

        driver.set_script_timeout(30)
        driver.set_page_load_timeout(30)

        for url in self.url_list:
            driver.get(url)
            driver.get_cookies()
            sleep(5)
            if self.popups:
                if isinstance(self.popup_el, list):
                    for popup in self.popup_el:
                        select = driver.find_element_by_xpath(popup)
                        select.click()
                        sleep(1)
                        driver.switch_to.default_content()

            if self.first_click:
                if isinstance(self.first_click_el, list):
                    for click in self.first_click_el:
                        driver.get_cookies()
                        sleep(5)
                        clicking_first = driver.find_element_by_xpath(click)
                        clicking_first.click()
                else:
                    print(type(self.first_click_el))
                    driver.get_cookies()
                    sleep(5)
                    clicking_first = driver.find_element_by_xpath(self.first_click_el)
                    clicking_first.click()

            for key in list(self.key_pairs.keys()):
                element = driver.find_element_by_xpath(key)
                element.send_keys(self.key_pairs[key])
                sleep(0.3)
            if isinstance(self.submit_element, list):
                for el in self.submit_element:
                    submit = driver.find_element_by_xpath(el)
                    submit.click()
                    sleep(0.3)
                sleep(5)
            else:
                submit = driver.find_element_by_xpath(self.submit_element)
                submit.click()
                sleep(5)
            print("Submitted {} out of {} contests".format(str(self.url_list.index(url)+1), str(len(self.url_list))))

