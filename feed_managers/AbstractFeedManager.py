from abc import ABC, abstractmethod 
from dbhelper import DBHelper
import re
import time
import sys
from datetime import datetime

from errors import UserError


class AbstractFeedManager(ABC):
    def __init__(self, tag, notifier, feeds_file):
        self._my_feeds = []
        self._feeds_file = feeds_file
        self._notifier = notifier
        self._tag = tag
        self._db = DBHelper()
        self._db.setup()


    def run(self):
        self._get_my_feeds()
        self._updates()
        self._db.close()


    def _get_my_feeds(self):
        feeds = ""
        try:
            with open(self._feeds_file, "r") as f:
                feeds = f.readlines()
        except FileNotFoundError:
            print("error: cannot read %s file" % self._feeds_file)
            self._notifier.error("cannot read %s file" % self._feeds_file)
            sys.exit(1)

        self._my_feeds = []
        my_feed = False
        for feed in feeds:
            my_feed = feed == ("# %s\n" % self._tag) if feed[0] == "#" else my_feed
            if not my_feed or feed[0] == "#": continue
            self._my_feeds += [feed.split(",")[1][:-1]]
        
        self._remove_old_users_in_db()


    def _updates(self):
        for user in self._my_feeds:
            try:
                user_update = self._fetch(user)
            except UserError as e:
                self._notifier.error(str(e))
                continue
            if len(user_update) == 0: continue # channel without video
            user_update.sort(key=lambda x: x["date"])
            
            last_entries_in_db_for_user = self._db.get_last(self._tag, user).fetchall()
            if len(last_entries_in_db_for_user) == 0: # user not in db, save last video & continue
                self._db.add(self._tag, user, user_update[-1]["url"], user_update[-1]["date"])
                continue 
            
            last_update_in_db = last_entries_in_db_for_user[0]
            for update in user_update:
                if datetime.strptime(last_update_in_db[1], "%Y-%m-%d %H:%M:%S") < update["date"]:
                    self._notifier.notify(update["update_text"])
                    self._db.add(self._tag, user, update["url"], update["date"])


    def _remove_old_users_in_db(self):
        users_in_db = self._db.get_all_users(self._tag)
        for user in users_in_db:
            if user[0] not in self._my_feeds: self._db.delete(self._tag, user[0])


    @abstractmethod
    def _fetch(self, user):
        """ must return [{"date", "url", "update_text"}]
        """

        pass