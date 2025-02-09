"""
Merge two smilecdr Java .properties files into 1.

This is used when we upgrade to a new version of the server and need migrate
our old server settings to the new server
"""

import argparse
from pprint import pprint
import os

from utils import properties_to_dict, dict_to_properties


def merge(old, new):
    """
    Merge two .properties files into 1

    For properties that are common between old and new, find the values that
    changed, then overwrite values in new file with those from old file

    For properties that differ between the two files, just print them out

    Write the new properties file to the current working directory
    """

    old = os.path.abspath(os.path.expanduser(old))
    new = os.path.abspath(os.path.expanduser(new))

    print(f'Comparing old properties file with new one:')
    contents = {}
    for i, f in enumerate([old, new]):
        if os.path.splitext(f)[-1] != '.properties':
            # print(f'{f} must be a .properties file. Exiting!')
            exit(1)
        print(f)
        contents[i] = {
            'filepath': f,
            'properties': properties_to_dict(f)
        }
    print()

    old_props = set(contents[0]['properties'].keys())
    new_props = set(contents[1]['properties'].keys())

    common = old_props.intersection(new_props)
    for key in common:
        old_val = contents[0]['properties'][key]
        new_val = contents[1]['properties'][key]
        if old_val != new_val:
            print(
                f'Overwriting property: {key} in new file with old value. '
                f'{new_val} --> {old_val}'
            )
            contents[1]['properties'][key] = old_val

    old_only = old_props.difference(new_props)
    new_only = new_props.difference(old_props)

    for i, prop_set in enumerate([old_only, new_only]):
        if i == 0:
            print('\nProperties in old file but not in new file: ')
            pprint(old_only)
        else:
            print('\nProperties in new file but not in old file: ')
            pprint(new_only)

    out_file = os.path.join(
        os.getcwd(), os.path.splitext(os.path.split(new)[-1])[0] +
        '-updated.properties'
    )
    print(f'Writing merged properties file to: {out_file}')
    dict_to_properties(contents[1]['properties'], out_file)


if __name__ == '__merge__':
    parser = argparse.ArgumentParser()
    parser.add_argument('old_file', help='Path to old properties file')
    parser.add_argument('new_file', help='Path to new properties file')
    args = parser.parse_args()

    merge(args.old_file, args.new_file)
