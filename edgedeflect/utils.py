"""
EdgeDeflect utils.
Version: 0.1.0

Copyright (c) 2023-present ElBe Development.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the 'Software'),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

###########
# IMPORTS #
###########

import argparse
import winreg


############################
# GET DEFAULT BROWSER PATH #
############################


def get_default_browser_path() -> str:
    """Returns the path to the default browser.

    Returns:
        str: Path to the default browser.
    """

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"SOFTWARE\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice",
    ) as browser_choice_reg:
        browser_choice = winreg.QueryValueEx(browser_choice_reg, "ProgId")[0]

    with winreg.OpenKey(
        winreg.HKEY_CLASSES_ROOT, rf"{browser_choice}\shell\open\command"
    ) as browser_path_reg:
        return winreg.QueryValueEx(browser_path_reg, "")[0].split('"')[1]


###################
# ARGUMENT PARSER #
###################


parser = argparse.ArgumentParser(
    prog="edgeDeflect",
    description="EdgeDeflect redirects `microsoft-edge://` links to your default browser.",
    epilog="Still in development!",
)
parser.add_argument(
    "--browser",
    action="store",
    help="Path to the browser to use instead of edge.",
    default=get_default_browser_path(),
    required=False,
)
parser.add_argument(
    "--no-backup", help="Will not create a backup.", action="store_false"
)
parser.add_argument(
    "--overwrite",
    help="Will forcefully overwrite existing backups without prompting.",
    action="store_false",
)
