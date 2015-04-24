import os
from os import path
html_dir = os.path.join("..", "archive", "html")
archive_json_dir = os.path.join("..", "archive", "json")
json_dir = os.path.join("..", "json")
datapackage_dir = os.path.join("..", "data")


html_filenos = [filename.strip(".html") for filename in os.listdir(html_dir) if "html" in filename]
archive_json_filenos = [filename.strip(".json") for filename in os.listdir(archive_json_dir) if "json" in filename]

def read_in_json(dir):
    records = []
    import simplejson
    for filename in os.listdir(dir):
        if "json" in filename:
            records.append(simplejson.loads(open(os.path.join(dir, filename), "r").read()))
    return records
