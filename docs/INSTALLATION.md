# Installation

## General instructions

- Download the repo. Then install the packages.

```bash
    user@phost:~/google-news-push-bot $ pip install -r requirements.txt
```

- rename the messenger template configuration file - this is the file which contains your target Apprise accounts

```bash
    user@phost:~/google-news-push-bot/src $ mv gnpush_messengers.yml.TEMPLATE gnpush_messengers.yml
```

- Add 1..n Apprise messenger configurations to your ```gnpush_messengers.yml``` file (see [Documentation](https://github.com/caronc/apprise/wiki/config_yaml) for further details)

- rename the search term template configuration file - this is the file which contains your search terms for the Google News search

```bash
    user@phost:~/google-news-push-bot/src $ mv gnpush_topics.yml.TEMPLATE gnpush_topics.yml
```

- Update the configuration file (valid value examples - see [here](https://github.com/ranahaani/GNews/)), For starters, use the example provided with this repo

- Start the program in test mode. This will send out a brief test message to your configured messenger accounts and then terminate the program. In case all libraries have been installed, you should a similar ouput to this one:

```bash
    user@phost:~/google-news-push-bot/src $ python gnpush.py --
    04/25/2022 10:43:25 AM - Startup ...
    04/25/2022 10:43:25 AM - Loaded 1 entries from file:///Users/myuser/google-news-push-bot/src/gnpush_messengers.yml?encoding=utf-8&cache=yes
    04/25/2022 10:43:25 AM - Notifying 1 service(s) asynchronously.
    04/25/2022 10:43:25 AM - Sent Telegram notification.
    04/25/2022 10:43:25 AM - Successfully sent a test message via Apprise
```

When you can see this message, all required libraries have been installed and your Apprise configuration seems to be ok, too.

## Google News search parameter configuration

The ``gnpush_topics.yml`` file contains your search parameters. Example:

```bash
Suchbegriff_1:
  search_term: Weltraum
  language: de
  country: DE
  period: 7d
  max_results: 10
  exclude_websites:
    - yahoo.com
    - cnn.com
  proxy: www.myproxy.de
Suchbegriff_2:
  search_term: Rente
  language: de
  country: DE
  period: 7d
  max_results: 10
```

Each search term needs to be listed with a unique search term id (```Suchbegriff_1```, ```Suchbegriff_2``` and so on). You are free to choose different names but remember that these names are unique.

Remaining parameters:

- ```search_term``` - the search term that you want to loop up on Google News
- ```language``` - [ISO639-a1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language. For a list of supported codes see [this page](https://github.com/ranahaani/GNews/#supported-languages)
- ```country``` - [ISO3166-a2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. For a list of supported codes see [this page](https://github.com/ranahaani/GNews/#supported-countries)
- ```period``` - search period; see [this page](https://github.com/ranahaani/GNews/#results-specification) for further details. This parameter represents the article search span on Google News
- ```max_results``` - maximum number of search results; see [this page](https://github.com/ranahaani/GNews/#results-specification) for further details.
- ```exclude_websites``` - optional list of 1..n websites that are to be exempted as search result source; see [this page](https://github.com/ranahaani/GNews/#results-specification) for further details.
- ```proxy``` - optional proxy for your search query; see [this page](https://github.com/ranahaani/GNews/#results-specification) for further details.


Now have a look at the [program's command line parameters](COMMANDS.md)