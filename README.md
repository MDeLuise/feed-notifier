# feed-notifier
A simple and expandible feed notifier.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Screenshots](#screenshots)

## General info
A side project focused on learning web scraping and how to use a simple telegram bot.
Feed-notifier consists in a simple and extendible feed RSS, default rss sources are YouTube and Twitch.
	
## Technologies
Project is created with:
* python 3.6
* beautifulsoup4

see `requirements.txt` for a complete list of used libraries
	
## Setup
To run this project:
* modify `feeds.txt` adding chanell you want to be notified of
* in `notifiers/TelegramNotifier.py` add telegram bot token and your telegram chat id

Then:

```
$ pip3 install -r requirements.txt
$ python3 main.py &
```

After that, every time a new video is uploaded in a followed chanell you'll receive a telegram message.
If you want to add a new feed rss manager, place the file in `feed_managers/` folder, then add the import in `main.py` and modify `plugins` list.
If you want to add a new notifier, place the file in `notifiers/` folder, then add the import in `main.py` and modify `notifier` variable.

## Screenshots
![Screenshot](docs/images/screenshot_1.png)
