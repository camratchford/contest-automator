# Import other modules
from . import coordinator
import os
import glob

# Account details fetched from ENV tags in docker run
account = {"FirstName": os.environ.get('FIRST_NAME'),
           "LastName": os.environ.get('LAST_NAME'),
           "FullName": str(os.environ.get('FIRST_NAME')) + " " + str(os.environ.get('LAST_NAME')),
           "Email": os.environ.get('EMAIL'),
           "Telephone": os.environ.get('PHONE')}

# Location of configuration files
contests = glob.glob("/app/contests/*.json")


# Method that will run the different pages with the env variables
def enter_contests():
    for contest in contests:
        coord = coordinator.Coordinator()
        coord.load_json(contest, account)
        coord.run()


