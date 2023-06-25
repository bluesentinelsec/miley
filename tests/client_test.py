import unittest

from miley.client import *

known_good = "c283d8a2688baef860c41c49b79a82db"  # taken from /usr/bin/bash
known_bad = "7de2c1bf58bce09eecc70476747d88a26163c3d6bb1d85235c24a558d1f16754"


class TestMalwareBazaar(unittest.TestCase):
    def test_query_hash(self):
        mb = Client()

        # scan known good hash
        self.assertEqual(False, mb.query_hashes(hashes=[known_good]))

        # scan known bad hash
        self.assertEqual(True, mb.query_hashes(hashes=[known_bad]))


if __name__ == '__main__':
    unittest.main()
