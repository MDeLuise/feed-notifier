#!/usr/bin/env python3

import sys
import time
import os

from feed_managers.YoutubeFeedManager import YoutubeFeedManager
from feed_managers.TwitchFeedManager import TwitchFeedManager
#from notifiers.EmailNotifier import EmailNotifier
from notifiers.TelegramNotifier import TelegramNotifier


SETTINGS_FILE = os.path.dirname(sys.argv[0]) + "/feeds.txt"




if (__name__ == "__main__"):
    notifier = TelegramNotifier()
    #if len(sys.argv) > 1 and sys.argv[1] == "-e":
    #    notifier = EmailNotifier()

    plugins = [
        YoutubeFeedManager(notifier, SETTINGS_FILE),
        TwitchFeedManager(notifier, SETTINGS_FILE)
    ]

    for plugin in plugins:
        plugin.run()