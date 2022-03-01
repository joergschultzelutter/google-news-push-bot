#
# Google News Push Bot
# Author: Joerg Schultze-Lutter, 2022
#
# Function: Various utility functionsc
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

import logging
import yaml
import os.path

# Set up the global logger variable
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)


def get_yaml_file(filename: str = "gnpush.yaml"):
    """
    Read the Enpass export file and converts its content to a dictionary
    Parameters
    ==========
    filename : 'str'
        File name of the YAML file that we are going to read
    Returns
    =======
    Content from YAML file
    """
    content = None
    if os.path.isfile(filename):
        with open(filename, "r") as stream:
            try:
                content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.debug(msg=exc)
                raise ValueError("Invalid YAML file")
        return content
    else:
        raise ValueError(f"YAML configuration file not found")
