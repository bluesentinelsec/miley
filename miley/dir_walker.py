import logging
import os

def walk_dir(path: str):
    logging.info(f"inventorying directory: {path}")
    found_files = []
    for path, subdirs, files in os.walk(path):
        for name in files:
            f = os.path.join(path, name)
            found_files.append(f)

    return found_files
