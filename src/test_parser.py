import os
import json
import unittest
from parser import get_json, get_sorted_genres, get_hiphop_packs, HIP_HOP


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
print(DATA_DIR)


class ParseTests(unittest.TestCase):

    def test_fetch_data(self):
        fetched_data = get_json()
        # test to see if some data is fetched & returned
        self.assertIsNotNone(fetched_data)

    def test_get_sorted_genres(self):
        file_path = os.path.join(DATA_DIR, "data.json")

        with open(file_path, "r") as f:
            data = json.loads(f.read())

        genre_names = get_sorted_genres(data)
        
        # Check that 47 different genres are returned from the locally saved JSON
        self.assertTrue(len(genre_names) == 47)

        for i in range(len(genre_names) - 2):
            self.assertTrue(genre_names[i] < genre_names[i + 1])

    def test_get_hiphop_pack_name(self):
        file_path = os.path.join(DATA_DIR, "data.json")

        with open(file_path, "r") as f:
            data = json.loads(f.read())

        hiphop_packs = get_hiphop_packs(data)
        # Test that 3 different packs are returned
        self.assertTrue(len(hiphop_packs) == 3)

        for pack in hiphop_packs:
            # Test to see if these packs are contain the genre 'hip-hop'
            self.assertTrue(HIP_HOP in pack["genres"])



