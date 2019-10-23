# Author: BlackBirds 

class bcolors:
      HEADER = '\033[95m'
      OKBLUE  = '\033[94m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'


__version__ = 'v1.0'

def banner():
    print(bcolors.OKGREEN + "             ____  _____    ___   Build                      " + bcolors.ENDC)
    print(bcolors.OKGREEN + "           _/    \/  __  \ |   \   By                        " + bcolors.ENDC)
    print(bcolors.OKGREEN + "          /      |  /  \ | |   _\   Black                    " + bcolors.ENDC)
    print(bcolors.OKGREEN + "         /    /|_| |    || |  |      Birds                   " + bcolors.ENDC)
    print(bcolors.OKGREEN + "        |    |   | |    || |  |                              " + bcolors.ENDC)
    print(bcolors.OKGREEN + "         \    \  | |    || |  |                              " + bcolors.ENDC)
    print(bcolors.OKGREEN + "     ___  \    | | |    || |  |    ________                  " + bcolors.ENDC)
    print(bcolors.OKGREEN + "     \  \ /    | | |_\  \| |  |___/       /                  " + bcolors.ENDC)
    print(bcolors.OKGREEN + "      \_______/   \___\  \  \____________/                   " + bcolors.ENDC)
    print(bcolors.OKGREEN + "                       \__\     SCRAPER                      " + bcolors.ENDC)
    print(bcolors.OKGREEN + "                                                             " + bcolors.ENDC)
    print(bcolors.OKGREEN + "      SQL-Scraper Ver. {}".format(__version__) + bcolors.ENDC)
    print("\n")
