from scanner import Scanner
from filler import Filler


def main():
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

    keypairs = {"//input[@name='name']": "Cameron",
                "//input[@name='email']": "Ratchford"}

    submit = ["//span[text()='I am at least 18 years of age (required)']",
              "//input[@uib-tooltip'Please complete your details to continue']"]

    filly = Filler(keypairs, submit, contest_list)
    filly.popups = True
    filly.popup_el = ["//button[text()='Allow']"]
    filly.first_click = True
    filly.first_click_el = "//a[@href='https://gleam.io/cookiefix?sa=https://gleam.io/wB4Ag/idrop-news-apple-iphone-11-pro-max-giveaway%3Fl%3Dhttps%253A%252F%252Fwww.idropnews.com%252Fgiveaways%252Fapple-iphone-11-pro-max-giveaway%252F117362%252F%26r%3D%26xdga%3D424950440.1581364605%26xdga_referrer%3D']"
    filly.fill()


if __name__ == "__main__":
    main()
