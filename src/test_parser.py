import os
import json
import unittest
from parser import get_json, get_sorted_genres, get_hiphop_packs, HIP_HOP


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
print(DATA_DIR)


class ParseTests(unittest.TestCase):

    def test_fetch_data(self):
        fetched_data = get_json()
        self.assertIsNotNone(fetched_data)

    def test_get_sorted_genres(self):
        file_path = os.path.join(DATA_DIR, "data.json")

        with open(file_path, "r") as f:
            data = json.loads(f.read())

        genre_names = get_sorted_genres(data)
        self.assertTrue(len(genre_names) == 47)

        for i in range(len(genre_names) - 2):
            self.assertTrue(genre_names[i] < genre_names[i + 1])

    def test_get_hiphop_pack_name(self):
        file_path = os.path.join(DATA_DIR, "data.json")

        with open(file_path, "r") as f:
            data = json.loads(f.read())

        hiphop_packs = get_hiphop_packs(data)
        self.assertTrue(len(hiphop_packs) == 3)

        for pack in hiphop_packs:
            self.assertTrue(HIP_HOP in pack["genres"])



