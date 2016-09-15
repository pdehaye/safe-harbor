""" Scrape utilities 
    To run: 
         python scrape.py 25000        (starts loading at index 25000)
    or 
         python scrape.py              (guesses where to start)
"""

import requests, os, sys, time
address = "https://safeharbor.export.gov/companyinfo.aspx?loc=eu&id="
from os import path
from names import html_dir, archive_json_dir

def adjust(n): return str(n).rjust(5, "0")

def download(n):
    """ Downloads the file with index n and writes it to disk {n}.json
    """
    output = requests.get(address + str(n))
    length = len(output.text)
    if  length < 60000 and length > 1:
        # length of more than 60k indicates redirect to main site
        with open(os.path.join(html_dir, adjust(n) + ".html"),  "w") as f:
            f.write(output.text.encode('utf8'))
        print "Successfully downloaded", n
        return True
    else:
        with open(os.path.join(html_dir,  adjust(n) + ".fail"),  "w") as f:
            f.write("".encode('utf8'))
        print "Index ", n, " leads to a redirect"
        return False

def starting_point(): 
    """
        Looks at last html and json files and decides accordingly
    """
    print "Figuring out where to start"
    try:
        tmp1 = int(sorted(filter(lambda _ : "html" in _, os.listdir(html_dir)))[-1].split(".")[0]) + 1 
    except:
        tmp1 = 0
    try:
        tmp2 = int(sorted(os.listdir(archive_json_dir))[-1].split(".")[0]) + 1
    except:
        tmp2 = 0
    print "Latest html:", tmp1
    print "Latest json:", tmp2
    tmp = max(tmp1, tmp2)
    print "Will start scraping at ", tmp
    return tmp


def scrape(start = None, delay = 10000):
    if not start:
        start = starting_point()
    i = start
    last_added = start   # Go for at most 50 on top
    while i < last_added + delay:
        try:
            if download(i):
                last_added = i
            i += 1
        except Exception as e:
            print "Encountered error ", str(e), "Downloading ", i, "seems to have stalled, sleeping now for 100 seconds, will restart afterwards"
            time.sleep(100)
            # delay so hopefully we stop hammering on the site

if __name__ == "__main__":
    import sys
    try:
        # argument specified
        start = int(sys.argv[1])
        print "Starting from ", start
        scrape(start = start)
    except IndexError:
        scrape()


