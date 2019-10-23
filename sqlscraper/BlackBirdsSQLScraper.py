#!/usr/bin/python3
# Author: Black Birds
# Made for Python3


"""THIS TOOL IS STILL IN DEVELOPMENT BY BLACKBIRDS"""


from bs4 import BeautifulSoup
from lib.banner import banner, __version__
import requests



class bcolors:
      HEADER = '\033[95m'
      OKBLUE  = '\033[94m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'

module_name = "SQLScraper: Find php?id Webpages across the Web"

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


print(bcolors.FAIL + "(!)The Developer take no responsiblity for damage caused by this Program" + bcolors.ENDC)


print("")


print(bcolors.FAIL + "(!)Also they don't take any responsibility for any missuse of this Program" + bcolors.ENDC)

print("")
print("")
print("")



banner()

print("")

print(bcolors.OKGREEN + "(INFO)Enter php?id to search for php?id Webpages across the Web" + bcolors.ENDC)

print("")

print(bcolors.OKGREEN + "(INFO)Enter php?id inurl:http to mostly get http-Webpages responses" + bcolors.ENDC)

print("")
print("")
print("")

search  = input("[Enter php?id to search for php?id Webpages across the Web]: ")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
       print("")
       print(bcolors.OKGREEN + item_text + bcolors.ENDC)
       print(bcolors.OKBLUE + item_href + bcolors.ENDC)
       




