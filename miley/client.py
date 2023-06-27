import logging
import time

import requests

md5_length = 32
sha1_length = 40
sha256_length = 64


class Client:
    def __init__(self):
        self.url = "https://mb-api.abuse.ch/api/v1/"
        self.malware_found = False
        self.samples_scanned = 0
        # TODO: add virus total

    def query_hashes(self, hashes=None):
        if not self.is_valid_hash(hashes):
            return

        num_hashes_to_scan = len(hashes)
        for each_hash in hashes:
            if each_hash == "":
                continue

            logging.info(f"querying {self.samples_scanned} / {num_hashes_to_scan} hashes against malware database")

            data = {"query": "get_info", "hash": each_hash}
            try:
                response = requests.post(self.url, data=data)
                j = response.json()
            except Exception as e:
                logging.error(e)
                time.sleep(1)
                continue

            self.samples_scanned += 1

            self.is_malware_detected(result_in_json=j)

        if self.malware_found == False:
            logging.info(f"no malware was detected")

        return self.malware_found

    def is_malware_detected(self, result_in_json) -> bool:
        r = result_in_json["query_status"]

        if r == "ok":  # query status of 'ok' means malware was detected
            logging.warning("[!] MALWARE DETECTED!")
            self.malware_found = True
            print(result_in_json)
            return True

        elif r == "hash_not_found":
            return False

        elif r == "http_post_expected" or r == "illegal_hash" or r == "no_hash_provided":
            logging.error(result_in_json)
            return False

        else:
            logging.error("unexpected response from endpoint:")
            print(result_in_json)
            return False

    def is_valid_hash(self, hashes):
        if hashes == [None] or hashes == ['']:
            logging.error("empty hash provided to query_hashes function")
            return False

        return True
