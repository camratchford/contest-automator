# Import other modules
from . import coordinator
import os
import glob

# account = {"FirstName": os.environ.get('FIRST_NAME'),
#            "LastName": os.environ.get('LAST_NAME'),
#            "FullName": str(os.environ.get('FIRST_NAME')) + " " + str(os.environ.get('LAST_NAME')),
#            "Email": os.environ.get('EMAIL'),
#            "Telephone": os.environ.get('PHONE')}

account = {"FirstName": "Cameron",
           "LastName": "Ratchford",
           "FullName": "Cameron Ratchford",
           "Email": "cjratchford@hotmail.com",
           "Telephone": "4033899337"}

contests = glob.glob("/home/cam/PycharmProjects/contest_automator/contests/*.json")


# Method that will run the different pages with the env variables
def enter_contests():
    for contest in contests:
        coord = coordinator.Coordinator()
        coord.load_json(contest, account)
        coord.run()


