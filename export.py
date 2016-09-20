#!/usr/bin/env python3
"""
A simple pass to keepass export script.

This script creates a new keepass store containing parts of or a complete
PASS(1) storage.
To detect the path of the password storage, it relies on the environment
variable PASSWORD_STORE_DIR (if set).
"""

import os
import subprocess

from collections import Generator
from keepassdb import Database

# the path of the keepass file
KEEPASS_PATH = os.path.join(os.getcwd(), 'out.kpd')

# the location of the password to encrypt the keepass file with in pass
KEEPASS_PW = 'keepass_pw'

# the path inside the pass to export (empty means export all)
EXPORT_SUBPATH = 'subpath-to-export/'


def export_passwords():
    """Export the passwords."""
    pass_base_path = _get_pass_base_path()
    export_path = _get_pass_export_path(pass_base_path)

    for full_password_path in _recursive_list_pass_dir(export_path):
        pass_path = full_password_path.replace(pass_base_path, '', 1)
        pass_path = _remove_leading_slash(pass_path)
        password = _get_password_from_pass(pass_path)
        print(pass_path)
        print(password)


def _get_password_from_pass(pass_path) -> str:
    """Get the pasword from pass."""
    # [:-1] to remove trailing newline
    return subprocess.check_output(['pass', pass_path]).decode()[:-1]


def _recursive_list_pass_dir(base_dir: str) -> Generator:
    """List a directory recursively."""
    for path, dirs, files in os.walk(base_dir):
        for file in files:
            if file[-4:] != '.gpg':
                continue
            yield os.path.join(path, file[:-4])


def _get_pass_base_path() -> str:
    """Get the path of the password store."""
    return os.environ.get('PASSWORD_STORE_DIR', os.path.expanduser(
        '~/.password-store'))


def _get_pass_export_path(base_path: str) -> str:
    """Get the export path."""
    return os.path.join(base_path, EXPORT_SUBPATH)


def _remove_leading_slash(string: str) -> str:
    """Remove a trailing slash (if any)."""
    if string[0] != '/':
        return string
    return string[1:]


if __name__ == '__main__':
    export_passwords()
