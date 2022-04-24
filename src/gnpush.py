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
from utils import (
    get_yaml_file,
    get_command_line_params,
    signal_term_handler,
    add_expiring_url,
)
from expiringdict import ExpiringDict
from pprint import pformat
import time
from apprisemsg import send_apprise_message

# Set up the global logger variable
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)


def gnpush_main():
    logger.info(msg="Startup ...")

    # Get command line parms
    (
        gnpush_topics,
        gnpush_messengers,
        gnpush_run_interval,
        gnpush_generate_test_message,
        gnpush_time_to_live,
        gnpush_msg_buffer_size,
    ) = get_command_line_params()

    # Get the topics from our YAML file
    mytopics = get_yaml_file(gnpush_topics)
    logger.debug(msg=f"Received topics: {pformat(mytopics)}")

    # Register the SIGTERM handler; this will allow a safe shutdown of the program
    logger.info(msg="Registering SIGTERM handler for safe shutdown...")
    signal.signal(signal.SIGTERM, signal_term_handler)

    # Set up the ExpiringDict for our entries
    # ttl value is in days but expiringdict needs seconds
    logger.info(msg=f"Setting up ExpiringDict with ttl of {gnpush_time_to_live} days and {gnpush_msg_buffer_size} entries")
    gnpush_message_cache = ExpiringDict(
        max_len=gnpush_msg_buffer_size, max_age_seconds=gnpush_time_to_live * 3600
    )

    while True:
        try:
            logger.info(msg=f"Processing your request ...")

            # List which contains our URLs that we need to send to the user (if we found any new topics)
            urls_to_send = []

            for topic in mytopics:
                # fmt: off
                search_term = mytopics[topic]["search_term"] if "search_term" in mytopics[topic] else None
                exclude_websites = mytopics[topic]["exclude_websites"] if "exclude_websites" in mytopics[topic] else None
                country = mytopics[topic]["country"] if "country" in mytopics[topic] else None
                language = mytopics[topic]["language"] if "language" in mytopics[topic] else None
                max_results = mytopics[topic]["max_results"] if "max_results" in mytopics[topic] else None
                period = mytopics[topic]["period"] if "period" in mytopics[topic] else None
                proxy = mytopics[topic]["proxy"] if "proxy" in mytopics[topic] else None
                # fmt: on

                logger.debug(
                    msg=f"Running Google News search on search term '{search_term}'"
                )
                search_results = get_google_news(
                    search_term=search_term,
                    language=language,
                    country=country,
                    period=period,
                    max_results=max_results,
                    exclude_websites=exclude_websites,
                    proxy=proxy,
                )

                # process our search results
                for search_result in search_results:
                    # did we receive URL info?
                    if "url" in search_result:
                        _url = search_result["url"]
                        # Try to add the url to our expiring dict - we
                        # will get a 'True' response in case the URL was _not_
                        # yet present and got added to the expiring dict
                        if add_expiring_url(url=_url, url_cache=gnpush_message_cache):
                            # If URL was added to our expiring dict, then
                            # add it to our target list of URLs
                            if _url not in urls_to_send:
                                urls_to_send.append(_url)
                            logger.info(
                                msg=f"Successfully added {_url} to expiring cache"
                            )
            # did we find anything that we need to send?
            _count = len(urls_to_send)
            if _count > 0:
                logger.debug(msg=f"Found {_count} new messages in total")
                # Format the message body:
                # urls with trailing \n except for the last item
                body = f"I found {_count} new messages for you:\n\n"
                body = body + ("\n".join(urls_to_send[:]))

                # Send the message via Apprise
                _result = send_apprise_message(
                    title="gnpush Notification",
                    body=body,
                    apprise_config_file=gnpush_messengers,
                )

                # log message status
                _msg = "Successfully sent" if _result else "Failed to send"
                _msg = _msg + f" {_count} new messages via Apprise"
                logger.info(msg=_msg)

            # enter sleep mode
            logger.info(msg=f"Sleeping for {gnpush_run_interval} hours")
            time.sleep(3600 * gnpush_run_interval)

        except (KeyboardInterrupt, SystemExit):
            logger.info(
                msg="Received KeyboardInterrupt or SystemExit in progress; shutting down ..."
            )
            break


if __name__ == "__main__":
    gnpush_main()
