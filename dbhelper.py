import sqlite3
import sys
import os


DB_NAME = os.path.dirname(sys.argv[0]) + "/feed_notifier.sqlite"


class DBHelper:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS last_update (service text, user text, url text, pub_date datetime)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add(self, service, user, url, uploaded_at):
        stmt = "SELECT url FROM last_update WHERE service='%s' AND user='%s'" % (service, user)
        res = self.conn.execute(stmt).fetchall()
        if len(res) > 0:
            stmt = "UPDATE last_update SET url='%s', pub_date='%s' WHERE service='%s' AND user='%s'" % (url, uploaded_at, service, user)
        else:
            stmt = "INSERT INTO last_update (service, user, url, pub_date) VALUES ('%s','%s','%s', '%s');" % (service, user, url, uploaded_at)
        self.conn.execute(stmt)
        self.conn.commit()

    def delete(self, service, user):
        stmt = "DELETE FROM last_update WHERE service='%s' AND user='%s'" % (service, user)
        self.conn.execute(stmt)
        self.conn.commit()

    def get_last(self, service, user):
        stmt = "SELECT url, pub_date FROM last_update WHERE service='%s' AND user='%s'" % (service, user)
        return self.conn.execute(stmt)

    def get_all_users(self, service):
        stmt = "SELECT user FROM last_update WHERE service='%s'" % service
        return self.conn.execute(stmt)

    def close(self):
        self.conn.close()