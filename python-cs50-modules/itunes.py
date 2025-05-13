import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Term name required")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])

o = response.json()

for val in o["results"]:
    print(val["trackName"])
