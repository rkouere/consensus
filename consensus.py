#python

import urllib.request
import argparse
import sys
from bs4 import BeautifulSoup, NavigableString, Tag



#print(actions)

class getActions():
    def getActionsFromUrl(self, url):
        '''
        Get a list of actions from a url
        '''
        self.listOfAction = []
        
        with urllib.request.urlopen(url) as response:
               html = response.read()
        
        soup = BeautifulSoup(html, "lxml")
        
        actions = soup.findAll("td", {"class": "tdv-libelle"})

        for x in actions:
            self.listOfAction.append(action(x.a['title']))

        print(self.listOfAction)
        
        for x in self.listOfAction:
            x.printName()

class action():
    def __init__(self, name):
        '''
        Une action
        '''
        self.name = name;

    def printName(self):
        print(self.name)

        

def main():
    #dealing with the logging level
    # Install the argument parser. Initiate the description with the docstring
    argparser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__)
    # this is a option which need one extra argument
    argparser.add_argument("-u",
                           '--url',
                           required=True,
                           help="The url of the boursorama page")
    arguments = argparser.parse_args()

    prgStart = getActions()
    prgStart.getActionsFromUrl(arguments.url)
#
#    prog = picutre_tidy(arguments.folder_in)
#    if arguments.folder_out is not None:
#        prog.add_out_folder(arguments.folder_out)


# This is a Python's special:
# The only way to tell wether we are running the program as a binary,
# or if it was imported as a module is to check the content of
# __name__.
# If it is `__main__`, then we are running the program
# standalone, and we run the main() function.
if __name__ == "__main__":
        main()
        
