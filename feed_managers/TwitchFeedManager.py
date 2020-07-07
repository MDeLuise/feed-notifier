import datetime
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import sys

from errors import UserError
from feed_managers.AbstractFeedManager import AbstractFeedManager



class TwitchFeedManager(AbstractFeedManager):
    def __init__(self, notifier, feeds_file):
        super().__init__("tw", notifier, feeds_file)

    def _fetch(self, user):
        name = user.split("/")[-2] if user[-1] == "/" else user.split("/")[-1]
        resp = requests.get("https://twitchrss.appspot.com/vod/%s" % name)
        if resp.status_code == 404: raise UserError(name)
        soup = BeautifulSoup(resp.text, 'lxml')
        videos = soup.findAll("item")
        
        to_return = []
        for video in videos:
            video_url = re.search("https://www.twitch.tv/videos/[0-9]*", video.text)
            if not bool(video_url): # i.e. is a live video
                url = "https://www.twitch.tv/%s" % name
            else: # is not a live video
                url = video_url[0] if sys.version_info[1] >= 6 else video_url.group(0)
            
            to_return += [
            {"date": datetime.strptime(video.find("pubdate").text, "%a, %d %b %Y %H:%M:%S UT"),
            "url": url,
            "update_text": "%s ([Twitch](%s))" % (name, url)
            }]

        return to_return