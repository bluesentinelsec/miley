#!/usr/bin/env python3

import argparse
import logging
import os

from miley.client import *


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
        logging.error("sorry, not implemented yet")
        return

    elif args.img is not None:
        logging.error("sorry, not implemented yet")
        return

    elif args.tar is not None:
        logging.error("sorry, not implemented yet")
        return

    else:
        parser.print_help()
        return

    c = Client()
    c.query_hashes(hashes=[args.hash])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

"""
scratch pad:
Scan local directories / files:
    ./miley --path /tmp/whatever/
    ./miley --path /tmp/whatever/evil.exe

Scan containers - should work if the container is in a remote registry or local:
    ./miley --img alpine:latest

Scan a file hash - meant for testing, but still useful:
    ./miley --hash SHA256,SHA1,MD5
"""
