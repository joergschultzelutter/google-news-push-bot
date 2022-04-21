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
import argparse

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


def signal_term_handler(signal_number, frame):
    """
    Signal handler for SIGTERM signals. Ensures that the program
    gets terminated in a safe way, thus allowing all databases etc
    to be written to disc.
    Parameters
    ==========
    signal_number:
                    The signal number
    frame:
                    Signal frame
    Returns
    =======
    """

    logger.info(msg="Received SIGTERM; forcing clean program exit")
    sys.exit(0)


def run_interval_check(interval_value):
    interval_value = int(interval_value)
    if interval_value < 1:
        raise argparse.ArgumentTypeError("Minimum run interval is 1 (hours)")
    return interval_value


def ttl_check(interval_value):
    interval_value = int(interval_value)
    if interval_value < 1:
        raise argparse.ArgumentTypeError("Minimum ttl is 1 (days)")
    return interval_value


def get_command_line_params():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--topics",
        default="gnpush_topics.yml",
        type=argparse.FileType("r"),
        help="Program config file name (this file contains your search terms)",
    )

    parser.add_argument(
        "--messengers",
        default="gnpush_messengers.yml",
        type=argparse.FileType("r"),
        help="Messenger config file name (this file contains your messenger accounts)",
    )

    parser.add_argument(
        "--run-interval",
        dest="run_interval",
        default=24,
        type=run_interval_check,
        help="Run interval in hours; default = 24 hrs, minimal value = 1 hours",
    )

    parser.add_argument(
        "--generate-test-message",
        dest="generate_test_message",
        action="store_true",
        help="Generates a test message, forwards it to your messenger accounts, and then exits the program",
    )

    parser.add_argument(
        "--ttl",
        dest="time_to_live",
        default=7,
        type=ttl_check,
        help="Message 'time to live' setting in days. Default value is 7 (days)",
    )

    args = parser.parse_args()

    gnpush_topics = args.topics.name
    gnpush_messengers = args.messengers.name
    gnpush_run_interval = args.run_interval
    gnpush_generate_test_message = args.generate_test_message
    gnpush_time_to_live = args.time_to_live

    return (
        gnpush_topics,
        gnpush_messengers,
        gnpush_run_interval,
        gnpush_generate_test_message,
        gnpush_time_to_live,
    )


if __name__ == "__main__":
    pass
