from scrape import scrape
from html_2_json import html_2_json
from polish_json import polish_json
from datapackage import datapackage
import sys

delay = 10
if len(sys.argv) == 2:
    delay = int(sys.argv[1])

scrape(delay = delay)
html_2_json()
polish_json()
datapackage()
