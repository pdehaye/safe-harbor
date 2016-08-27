"""
    Goes from raw json to more polished json: fixes some fields, parses some others
"""

from names import archive_json_dir, json_dir, read_in_json
import simplejson
from collections import defaultdict
from corp_schema import all_properties, corp_properties, corp_properties_set
from industry_sectors import parse_sectors
from countries import parse_countries
import os
import sys

OrgName_records = defaultdict(list)

############
def extract_extension(string_email):
    return string_email.split("@")[1]

def extract_http(string_http):
    return ".".join(string_http.split("/")[2].split(".")[-2:0])

def extract_domain(string_domain):
    if "http" in string_domain:
        return extract_http(string_domain)
    else:
        return extract_extension(string_domain)

def assert_all_equal(items):
    assert len(set(items)) == 1

def standard_name(corp):
    """ Creates a standard name, based on a corp record """
    officer_email = corp.corpoffemail1.split(",")
    contact_email = corp.contactemail1.split(",")
    addresses = []
    for email in officer_email + contact_email:
        try:
            addresses.append(extract_domain(email).lower())
        except:
            print email, "does not contain a domain name"
    try:
        assert_all_equal(addresses)
        assert len(addresses) > 1
    except:
        print addresses
    return addresses
    
    if string.count("@") == 1:
        return extract_extension(string)
    elif string.count("@") == 0:
        raise Exception("no email in {0}".format(string))
    else:
        string2 = string.split(",")
        a, b = map(extract_extension, string2)
        try:
            assert a == b
        except AssertionError as e:
            raise Exception("Adresses {0} and {1} do not have the same domain".format(a, b))
        return a
        
##################


def is_latest(OrgName, asp_index):
    daisy_chain = sorted(OrgName_records[OrgName])
    latest = (asp_index == daisy_chain[-1]) 
    if daisy_chain.index(asp_index) == 0:
        previous = ""
    else:
        previous = daisy_chain[daisy_chain.index(asp_index) - 1]
    return latest, previous

def date_parse(date):
    if not date:
        return ""
    month, day, year = date.split("/")
    return "-".join([year, month.rjust(2,"0"), day.rjust(2,"0")])

def empty(string):
    if string in ["None", "none", "N\A", "None.", "none.", "NA", "NO", "NONE", "NONE."]:
        return "None"
    else:
        return string

boolean = {"Yes": "true", "No": "false", "No ": "false", "Sel": ""}

tag_maps = {
                     "hrdata": boolean,
                     "statutorybody" : {"Federal Trade Commission" : "FTC", "Department of Transportation": "DoT"},
                     # "CertificationStatus": {"Current": "true", "Not Current": "false"},
                     "euprotection": boolean
                 }

tag_transforms = {
                    "nextcertification": date_parse,
                    "ppdate": date_parse,
                    "signupdate": date_parse,
                    "privacyprograms": empty
}

def transform_corp(corp):
    new_corp = {}
    for tag_id in corp_properties:
        if tag_id in tag_maps:
            new_corp[tag_id] = tag_maps[tag_id][corp[tag_id]]
        elif tag_id in tag_transforms:
            new_corp[tag_id] = tag_transforms[tag_id](corp[tag_id])
        else:
            new_corp[tag_id] = corp[tag_id]
    latest, previous = is_latest(corp["OrgName"], corp["asp_index"])
    if latest:
        new_corp["latest"] = "true"
    else:
        new_corp["latest"] = "false"
    new_corp["previous"] = previous
    new_corp["industrysector_parsed"] = parse_sectors(corp["industrysector"])
    new_corp["eucountries_parsed"] = parse_countries(corp["eucountries"])
    return new_corp

def polish_json():
    print "Reading in raw json"
    corp_records = read_in_json(archive_json_dir)
    print "Done"
    print "Matching up entries and their updates"
    # Computes matches based on OrgName
    for corp in corp_records:
        OrgName_records[corp["OrgName"]].append(corp["asp_index"])
    print "Done"
    print "Processing new json"
    new_records = map(transform_corp, corp_records)
    print "Done"
    import simplejson
    print "Dumping the new json"
    for record in new_records:
        with open(os.path.join(json_dir, record["asp_index"] + ".json"), "w") as f:
            f.write(simplejson.dumps(record, sort_keys=True, indent=4 * ' ').encode("utf-8"))
    print "Done"

if __name__ == "__main__":
    polish_json()
