import json

with open('dmoz.json') as urls_json:

	urls = json.load(urls_json)

	for url in urls:
		print url['link']