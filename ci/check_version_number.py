"""
Before, pypi release, ensure that the release tag matches the inventree version number!
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import os
import re
import sys

if __name__ == '__main__':

    here = os.path.abspath(os.path.dirname(__file__))

    version_file = os.path.join(here, '..', 'inventree', 'base.py')

    with open(version_file, 'r') as f:

        results = re.findall(r'INVENTREE_PYTHON_VERSION = "(.*)"', f.read())

        if not len(results) == 1:
            print(f"Could not find INVENTREE_SW_VERSION in {version_file}")
            sys.exit(1)

        version = results[0]

    parser = argparse.ArgumentParser()
    parser.add_argument('tag', help='Version tag', action='store')

    args = parser.parse_args()

    if not args.tag == version:
        print(f"Release tag '{args.tag}' does not match INVENTREE_SW_VERSION '{version}'")
        sys.exit(1)

sys.exit(0)
