#!/opt/local/bin/python3
#
# Google News Push Bot
# Author: Joerg Schultze-Lutter, 2022
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

from pprint import pformat
import logging
import yaml
import apprise
import signal
from googlenews import get_google_news
from utils import get_yaml_file, get_command_line_params, signal_term_handler
from expiringdict import ExpiringDict
from pprint import pformat

# Set up the global logger variable
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    logger.info(msg="Startup ...")

    # Get command line parms
    (
        gnpush_topics,
        gnpush_messengers,
        gnpush_run_interval,
        gnpush_generate_test_message,
        gnpush_time_to_live,
    ) = get_command_line_params()

    # Get the topics from our YAML file
    mytopics = get_yaml_file(gnpush_topics)
    logger.info(msg=pformat(mytopics))

    # Register the SIGTERM handler; this will allow a safe shutdown of the program
    logger.info(msg="Registering SIGTERM handler for safe shutdown...")
    signal.signal(signal.SIGTERM, signal_term_handler)

    # Set up the ExpiringDict for our entries
    mowas_message_cache = ExpiringDict(
        max_len=1000, max_age_seconds=gnpush_time_to_live * 86400
    )

    while True:
        try:
            logger.debug(msg=f"Processing your topics data ...")

        except (KeyboardInterrupt, SystemExit):
            logger.info(
                msg="Received KeyboardInterrupt or SystemExit in progress; shutting down ..."
            )
            break
