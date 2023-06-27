import hashlib
import logging


def hash_file(file):
    content_hash = ""
    try:
        with open(file, "rb") as f:
            contents = f.read()
            content_hash = hashlib.sha256(contents).hexdigest()
    except Exception as e:
        logging.error(e)

    return content_hash

def hash_files(file_list):
    hash_list = []
    for file in file_list:
        h = hash_file(file)
        hash_list.append(h)
    return hash_list