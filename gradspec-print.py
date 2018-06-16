import json
from pprint import pprint

json_data=open("cs-2015-16.json").read()

data = json.loads(json_data)
pprint(data)

print "Requirements name: %s" % data["name"]
print "Version: %s" % data["version"]
print "Magic: %s" % data["magic"]
print "---- Printing toplevel sections ----"

for toplevel_section in data["requirements"]:
    print "Toplevel section name: %s" % toplevel_section["title"]