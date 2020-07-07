import datetime
from bs4 import BeautifulSoup
import requests
import datetime

from notifiers.Notifier import Notifier


TOKEN="" # insert the telegram bot token here
URL="https://api.telegram.org/bot"
CHAT_ID="" # insert your telegram chat ID here


class TelegramNotifier(Notifier):
    
    def error(self, msg):
        self.notify(msg)

    def notify(self, msg):
        requests.get("%s%s/sendmessage?chat_id=%s&parse_mode=Markdown&text=%s" % \
            (URL, TOKEN, CHAT_ID, msg))