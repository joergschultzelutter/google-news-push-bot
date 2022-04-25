#
# Google News Push Bot
# Author: Joerg Schultze-Lutter, 2022
#
# Function: Apprise Communication Module
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import apprise
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)


def send_apprise_message(title: str, body: str, apprise_config_file: str):
    """
    Send a nessage via Apprise messenger
    Parameters
    ==========
    title : 'str'
        Message title
    body: 'str'
        Message body
    apprise_config_file: 'str'
        Apprise YAML configuration file

    Returns
    =======
    result : 'bool'
        Apprise command execution status
    """

    _apprise_instance = apprise.Apprise()
    _apprise_config = apprise.AppriseConfig()
    _apprise_config.add(apprise_config_file)

    _apprise_instance.clear()
    _apprise_instance.add(_apprise_config)

    result = _apprise_instance.notify(title=title, body=body)
    return result


if __name__ == "__main__":
    pass
