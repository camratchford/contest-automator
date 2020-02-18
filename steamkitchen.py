from scanner import Scanner
from filler import Filler


def main():
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


if __name__ == "__main__":
    main()
