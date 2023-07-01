#!/usr/bin/env python3

import argparse
import logging
import os

from miley.client import *
from miley.container_handler import *
from miley.dir_walker import *
from miley.hasher import *



def main():
    parser = argparse.ArgumentParser(prog="miley", description="A light weight malware scanner")
    parser.add_argument("--hash", help="An MD5, SHA1, or SHA256 hash to scan")
    parser.add_argument("--path", help="Path to a directory or file to scan")
    parser.add_argument("--img", help="A container image of the form 'NAME[:TAG|@DIGEST]'")
    parser.add_argument("--tar", help="A container image exported as tarball via 'docker save' command or similar")
    args = parser.parse_args()

    hashes_to_scan = []

    if args.hash is not None:
        hashes_to_scan.append(args.hash)

    elif args.path is not None:
        files = walk_dir(args.path)
        hashes_to_scan = hash_files(files)

    elif args.img is not None:
        c = Container()
        c.get(args.img)
        c.unpack_container_archive()
        files = walk_dir(c.extracted_path)
        hashes_to_scan = hash_files(files)

    elif args.tar is not None:
        logging.error("sorry, not implemented yet")
        return

    else:
        parser.print_help()
        return

    c = Client()
    c.query_hashes(hashes=hashes_to_scan)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()


