from scanner import Scanner
from filler import Filler


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
    scanny = Scanner(top_level_el, top_level_attribute,
                     key_el, key_attribute,
                     qualifier_el, qualifier_val,
                     pagination_string=pagination, starting_page=page, url=url)

    contest_list = scanny.run()

    keypairs = {"//input[@id='giveaway_entry_name']": "Cameron Ratchford",
                "//input[@id='giveaway_entry_email']": "cjratchford@hotmail.com"}

    submit = "//input[@value='Enter']"

    filly = Filler(keypairs, submit, contest_list)
    filly.fill()


if __name__ == "__main__":
    main()
