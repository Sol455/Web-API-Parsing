#! Python3

import requests
import json

def get_json():
    r = requests.get('https://api.ampifymusic.com/packs')
    return r.json()


def sort(text):
    print(json.dumps(text, indent=4, sort_keys=True))


def run():
    data = get_json()
    sort(data)


run()