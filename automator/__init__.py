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
               "Telephone": os.environ.get('PHONE')}

# For testing new sites, locally, without headless browser
else:
    contests = glob.glob("/home/cam/Projects/contest_automator/contests_still_testing/*.json")
    account = {"FirstName": "Cameron",
               "LastName": "Ratchford",
               "FullName": str(os.environ.get('FIRST_NAME')) + " " + str(os.environ.get('LAST_NAME')),
               "Email": "cjratchford@hotmail.com",
               "Telephone": "4033899337"}

# Method that will run the different pages with the env variables
def enter_contests():
    for contest in contests:
        print(contest)
        coord = coordinator.Coordinator(testing_mode)
        coord.load_json(contest, account)
        coord.run()


