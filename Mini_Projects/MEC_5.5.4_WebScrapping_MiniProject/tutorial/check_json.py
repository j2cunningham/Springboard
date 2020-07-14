import json

# Load the output json files
css_json   = json.load(open('./css-scraper-results.json'))
xpath_json = json.load(open('./xpath-scraper-results.json'))

# Nice way to do this via
# https://stackoverflow.com/questions/56006585/find-difference-between-two-json-files-in-python

a = json.dumps(css_json, sort_keys=True)
b = json.dumps(xpath_json, sort_keys=True)

if a == b:
	print('JSON files are identical')
else:
	print('JSON files are NOT identical')