"""
    Goes from raw html to raw json, simply using BeautifulSoup
"""

from bs4 import BeautifulSoup
from names import html_dir, archive_json_dir, html_filenos, archive_json_filenos
import simplejson
from collections import defaultdict
from corp_schema import all_properties, corp_properties, corp_properties_set
import os
import sys

def parse_html(fileno):
    with open(os.path.join(html_dir, fileno + ".html"), "r") as f:
        soup = BeautifulSoup(f.read())
    tags = [(tag["id"].strip("lbl"), tag.text) for tag in soup.body.form.find_all('span')]
    tmp = {}
    for tag_id, tag_text in tags:
        try:
            assert tag_id in all_properties
        except: 
            raise AssertionError("New HTML tag {} encountered, information presumably lost".format(tag_id))
        if tag_id in corp_properties_set:
            tmp[tag_id] = tag_text
    tmp["asp_index"] = fileno
    return tmp

def html_2_json(cli_filenos = None):
    print "Converting raw HTML files to raw JSON, simply though BeautifulSoup, and only where needed"
    if cli_filenos:
       filenos = cli_filenos
    else:
       filenos = html_filenos()
    for fileno in filenos:
        if not fileno in archive_json_filenos():
            print "Doing", fileno
            corp = parse_html(fileno)
            with open(os.path.join(archive_json_dir, fileno + ".json"), "w") as f:
                f.write(simplejson.dumps(corp, sort_keys=True, indent=4 * ' ').encode("utf-8"))
    print "Done converting"

if __name__ == "__main__":
    import sys
    print sys.argv[1:]
    html_2_json(cli_filenos = [filename.strip(".html") for filename in sys.argv[1:] if ".html" in filename])
