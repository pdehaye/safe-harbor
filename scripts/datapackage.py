"""
    Starting with json files, produces the csv. Makes sure ordering of properties is ok
"""

from names import read_in_json, datapackage_dir, json_dir
from os import path
from corp_schema import corp_properties
from csv import QUOTE_ALL

import csvkit

def datapackage():
    corps = read_in_json(json_dir)
    corps.sort(key = lambda _: _["asp_index"])

    full_properties = corp_properties[:2] + ["latest", "previous"] + corp_properties[2:] + ["eucountries_parsed", "industrysector_parsed"]

    assert  set(corps[0])  == set(full_properties) # Good handle on fiels to write

    print "Dumping the new datapackage csv"
    with open(path.join(datapackage_dir, "safe_harbor.csv"), 'wb') as csvfile:
        csvwriter = csvkit.py2.CSVKitDictWriter(csvfile, full_properties, delimiter=',', quoting=QUOTE_ALL)
        csvwriter.writeheader()
        for corp in corps:
            csvwriter.writerow(corp)
