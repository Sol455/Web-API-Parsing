#! python3

import requests

HIP_HOP = "hip-hop"


def get_json():
    r = requests.get('https://api.ampifymusic.com/packs')
    return r.json()


def get_sorted_genres(data):
    genre_names = set()

    for pack in data["packs"]:
        for genre in pack["genres"]:
            genre_names.add(genre)
    sorted_genre_names = sorted(genre_names)
    return sorted_genre_names


def get_hiphop_packs(data):
    hiphop_packs = []

    for pack in data["packs"]:
        if HIP_HOP in pack["genres"]:
            hiphop_packs.append(pack)

    return hiphop_packs


def run():
    data = get_json()
    genre_names = get_sorted_genres(data)
    hiphop_packs = get_hiphop_packs(data)
    print("\n%s genres found in packs:" % len(genre_names))

    for genre in genre_names:
        print("\t%s" % genre)

    print("\n%s Hip-hop packs found:" % len(hiphop_packs))

    for pack in hiphop_packs:
        print("\t%s" % pack["name"])


if __name__ == "__main__":
    run()
