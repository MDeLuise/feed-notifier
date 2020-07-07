import datetime
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import sys

from errors import UserError
from feed_managers.AbstractFeedManager import AbstractFeedManager



class YoutubeFeedManager(AbstractFeedManager):
    def __init__(self, notifier, feeds_file):
        super().__init__("yt", notifier, feeds_file)

    def _fetch(self, user):
        channel_id = re.search("(https://.*)", user)
        channel_id = channel_id[0].split("/")[-1] if sys.version_info[1] >= 6 else channel_id.group(0).split("/")[-1]
        resp = requests.get("https://www.youtube.com/feeds/videos.xml?channel_id=%s" % channel_id)
        if resp.status_code == 404: raise UserError(name)
        soup = BeautifulSoup(resp.text, 'lxml')
        videos = soup.findAll("entry")
        name = soup.find("name").text
        
        to_return = []
        for video in videos:
            video_id = video.find("yt:videoid").text
            url = "https://www.youtube.com/watch?v=%s" % video_id
            to_return += [
            {"date": datetime.strptime(video.find("published").text, "%Y-%m-%dT%H:%M:%S+00:00"),
            "url": url,
            "update_text": "%s ([YouTube](%s))" % (name, url)
            }]

        return to_return