#!/usr/bin/env python3
"""
A simple pass to keepass export script.

This script creates a new keepass store containing parts of or a complete
PASS(1) storage.
To detect the path of the password storage, it relies on the environment
variable PASSWORD_STORE_DIR (if set).
"""

import os

# the path of the keepass file
KEEPASS_PATH = os.path.join(os.getcwd(), 'out.kpd')

# the location of the password to encrypt the keepass file with in pass
KEEPASS_PW = 'keepass_pw'

# the path inside the pass to export (empty means export all)
EXPORT = 'subpath-to-export'


def export_passwords():
    """Export the passwords."""
    return


def _get_pass_base_path() -> str:
    """Get the path of the password store."""
    return os.environ.get('PASSWORD_STORE_DIR', os.path.expanduser(
        '~/.password-store'))


if __name__ == '__main__':
    print(_get_pass_base_path())
