# google-news-push-bot

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![CodeQL](https://github.com/joergschultzelutter/google-news-push-bot/actions/workflows/codeql.yml/badge.svg)](https://github.com/joergschultzelutter/google-news-push-bot/actions/workflows/codeql.yml)

## Google News Push Messenger Bot

Performs a Google News search with 1..n search terms and sends new search result URLs to the user. 

## Feature set

- The bot uses a freely configurable expiring dictionary that prevents duplicate search results from being sent to the user.
- Uses the [Apprise](https://github.com/caronc/apprise) program library to send messages to the user. 1..n messengers can be configured.

## Program details

- [Installation and Configuration](docs/INSTALLATION.md)
- [Supported Command Line Parameters](docs/COMMANDS.md)