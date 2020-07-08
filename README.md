# feed-notifier
A simple and expandible feed notifier.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Plug-in](#plug-in)
* [Screenshots](#screenshots)

## General info
A side project focused on learning web scraping and how to use a simple telegram bot.  
Feed-notifier consists in a simple and extendible feed RSS, default rss sources are YouTube and Twitch.
	
## Technologies
Project is created with:
* python 3.6
* beautifulsoup4
* sqlite3

see `requirements.txt` for a list of used libraries generated with `pip3 freeze` command.
	
## Setup
To run this project:
* modify `feeds.txt` adding chanell you want to be notified of
* in `notifiers/TelegramNotifier.py` add telegram bot token and your telegram chat id

Then:

```
$ pip3 install -r requirements.txt
$ python3 main.py
```

Every time the script is runned, if a new video is uploaded or a new live is broadcasted in a followed chanell you'll receive a telegram message.  
Create a cron job running the script if you want to run automatically the script at a given time.

## Plug-in
If you want to add a new feed rss manager, create a subclass of `feed_managers/AbstractFeedManager.py` and place the file in `feed_managers/` folder, then add the import in `main.py` and modify `plugins` list.  
If you want to add a new notifier, create a subclass of `notifiers/Notifier.py` and place the file in `notifiers/` folder, then add the import in `main.py` and modify `notifier` variable.

## Screenshots
<img src="docs/images/screenshot_1.png" width="250">
