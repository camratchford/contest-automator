# Import other modules
from . import coordinator
import os
import glob

testing_mode = True

# For prod, in docker
if not testing_mode:
    # Location of configuration files
    contests = glob.glob("/app/contests/*.json")
    # Account details fetched from ENV tags in docker run
    account = {"FirstName": os.environ.get('FIRST_NAME'),
               "LastName": os.environ.get('LAST_NAME'),
               "FullName": str(os.environ.get('FIRST_NAME')) + " " + str(os.environ.get('LAST_NAME')),
               "Email": os.environ.get('EMAIL'),
               "Country": os.environ.get('COUNTRY'),
               "BirthMonth": os.environ.get('BIRTH_MONTH'),
               'BirthDay': os.environ.get('BIRTH_DAY'),
               "BirthYear": os.environ.get('BIRTH_YEAR'),
               "Gender": os.environ.get('GENDER'),
               "Address": os.environ.get('ADDRESS'),
               "PostalCode": os.environ.get('POSTAL_CODE'),
               "City": os.environ.get('CITY'),
               "Province": os.environ.get('PROVINCE'),
               "Telephone": os.environ.get('PHONE')}

# For testing new sites, locally, without headless browser
else:
    contests = glob.glob("/home/cam/PycharmProjects/contest_automator/contests_still_testing/*.json")
    # account = {"FirstName": "Cameron",
    #            "LastName": "Ratchford",
    #            "FullName": "Cameron Ratchford",
    #            "Email": "cjratchford@hotmail.com",
    #            "Country": "Canada",
    #            "BirthMonth": "May",
    #            'BirthDay': "5",
    #            "BirthYear": "1991",
    #            "Gender": "Male",
    #            "Address": "A-2409 28 Street SW",
    #            "PostalCode": "T3E 2H7",
    #            "City": "Calgary",
    #            "Province": "Alberta",
    #            "Telephone": "4033899337"}

    # Phony Account Info for testing
    account = {"FirstName": "Jay",
               "LastName": "McMasterson",
               "FullName": "Jay McMasterson",
               "Email": "jmcmasterson@yahoo.com",
               "Country": "Canada",
               "BirthMonth": "July",
               'BirthDay': "7",
               "BirthYear": "1982",
               "Gender": "Male",
               "Address": "406 Bay Street",
               "PostalCode": "P0X 1C0",
               "City": "Keewatin",
               "Province": "Ontario",
               "Telephone": "8075473131"}


# Method that will run the different pages with the env variables
def enter_contests():
    for contest in contests:
        print(contest)
        coord = coordinator.Coordinator(testing_mode)
        coord.load_json(contest, account)
        coord.run()


