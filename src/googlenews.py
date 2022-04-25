#
# Google News Push Bot
# Author: Joerg Schultze-Lutter, 2022
#
# Function: Get content from Google News
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
from gnews import GNews
import logging

# Set up the global logger variable
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)


def get_google_news(
    search_term: str,
    language: object = None,
    country: object = None,
    period: str = "1d",
    max_results: object = None,
    exclude_websites: object = None,
    proxy: object = None,
):
    """
    Read the Enpass export file and converts its content to a dictionary
    Parameters
    ==========
    search_term : 'str'
        The term that we want to search for
    language: 'str'
        iso639-a2 language code or 'None'
    country: 'str'
        iso3166-a2 country code or 'None'
    period: 'str'
        default: '1d', can be 'd'ays, 'h'ours', 'm'onths, 'y'ears
    max_results: 'int'
        maximum results or 'None'
    exclude_websites: 'list'
        List item, containing strings for web sites to be excluded
        or 'None'
    proxy: 'str'
        proxy server or 'None'
    Returns
    =======
    Returns a dict which contains the search results (if present)
    """

    # Create the object
    google_news = GNews()

    # Populate search terms if provided by the user
    if language and isinstance(language, str):
        google_news.language = language

    if country and isinstance(country, str):
        google_news.country = country

    if max_results and isinstance(max_results, int):
        google_news.max_results = max_results

    if exclude_websites and isinstance(exclude_websites, list):
        google_news.exclude_websites = exclude_websites

    if proxy and isinstance(proxy, str):
        google_news.proxy = proxy

    # populate our period
    google_news.period = period

    # and run the search
    my_news = google_news.get_news(key=search_term)
    return my_news


if __name__ == "__main__":
    pass
