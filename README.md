pass to keepass export
======================

A simple pass to keepass export script.

This script creates a new keepass store containing parts of or a complete
PASS(1) storage.
To detect the path of the password storage, it relies on the environment
variable PASSWORD_STORE_DIR (if set).

Requirements
------------

You will need python 3 as well as the libraries listed in *requirements.txt*.

Usage
-----

Specify the pass path of the password to use for the keepass database in line 24 as *KEEPASS_PW* (relative to your pass root).

If you do not want to export all of your passwords (i.e. to export the passwords for a single customer or of a single service), you can specify a path (again, relative to your pass root) to export in line 27 as *EXPORT_SUBPATH*. By default, all passwords are exported.

After executing the script, you get a keepass file called *out-$date.kdb* where *$date* is a timestamp of the second when the script was started. This can be opened with KeepassX or older Keepass versions and imported in newer Keepass versions.

License
-------

Copyright 2016 Pascal Wichmann

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
