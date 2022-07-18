#!/usr/bin/env python3
"""
A simple pass to keepass export script.

This script creates a new keepass store containing parts of or a complete
PASS(1) storage.
To detect the path of the password storage, it relies on the environment
variable PASSWORD_STORE_DIR (if set).
"""

import datetime
import os
import subprocess
import sys

# from keepassdb.db import Database, Group
from pykeepass import PyKeePass

# the path of the keepass file
KEEPASS_PATH = os.path.join(os.getcwd(), 'out-{}.kdb'.format(
    datetime.datetime.now().strftime('%Y%m%d-%H%M%S')))

# the location of the password to encrypt the keepass file with in pass
KEEPASS_PW = 'keepass_pw'

# the path inside the pass to export (empty means export all)
EXPORT_PASSWORDS = (
    # 'example.org/bar',
    # 'test/xyz/foobar',
)


def export_passwords():
    """Export the passwords."""
    if os.path.isfile(KEEPASS_PATH) and '-f' not in sys.argv:
        print('Out file exists and -f not used.')
        sys.exit(1)

    pass_base_path = _get_pass_base_path()

    # db = Database()
    # known_groups = {
    #     '': db.create_group('PASS(1)'),
    # }

    for full_password_path in EXPORT_PASSWORDS:
        pass_path = full_password_path.replace(pass_base_path, '', 1)
        pass_path = _remove_leading_slash(pass_path)
        password = _get_password_from_pass(pass_path)
        # group = _get_group(db, known_groups, pass_path)
        # group.create_entry(
        #     title=pass_path, url=pass_path.split('/')[0], username=os.path.basename(pass_path),
        #     password=password)

    # db.save(KEEPASS_PATH, password=_get_password_from_pass(KEEPASS_PW))
    if '--print-output-only' not in sys.argv:
        print('Export successful. Output is:')
    print(KEEPASS_PATH)


def _get_group(db
               # : Database
               , known_groups: dict, pass_path: str):
               # -> Group:
    """Get or create a group by a pass path."""
    pass_paths = pass_path.split('/')[:-1]
    full_path = ''
    parent = known_groups['']  # base group
    for subpath in pass_paths:
        full_path += '/' + subpath
        if full_path not in known_groups.keys():
            known_groups[full_path] = db.create_group(subpath, parent=parent)
        parent = known_groups[full_path]
    return known_groups[full_path]


def _get_password_from_pass(pass_path: str) -> str:
    """Get the pasword from pass."""
    return subprocess.check_output(['pass', pass_path]).decode().splitlines()[0]



def _get_pass_base_path() -> str:
    """Get the path of the password store."""
    return os.environ.get('PASSWORD_STORE_DIR', os.path.expanduser(
        '~/.password-store'))


def _remove_leading_slash(string: str) -> str:
    """Remove a trailing slash (if any)."""
    if string[0] != '/':
        return string
    return string[1:]


if __name__ == '__main__':
    export_passwords()
