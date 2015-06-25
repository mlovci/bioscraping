__author__ = 'lovci'

from six.moves import urllib as urllib
import sqlite3
import os


class Scraper(object):

    base_url = None
    source = "unknown"

    def store(self, identifier, page, source=None):
        if source is None:
            source = self.source
        self.db_con.execute('INSERT INTO Webdata VALUES (?, ?, ?)', (identifier, page, source))
        self.db_con.commit()

    def _cached_download(self, identifier):
        existing = list(self.db_con.execute('SELECT Page FROM Webdata WHERE Id=? LIMIT 1', [identifier]))
        if len(existing) == 0:
            source, page = self._download(identifier)
            self.store(identifier, page, source)
            return page
        else:
            return existing[0][0]

    def fetch(self, identifier):
        page = self._cached_download(identifier)
        parsed = self._parse(page)
        return parsed

    def __init__(self, local_database=":memory:",
                 *args, **kwargs):

        self.local_database = local_database
        self.db_con = sqlite3.connect(self.local_database)
        self.db_con.execute("CREATE TABLE IF NOT EXISTS Webdata (Id text, Page text, Source text)")

    def __exit__(self, type, value, tb):
        self.db_con.close()

    @staticmethod
    def _parse(page):
        #no need to parse this one, it's plaintext, just readthrough
        return page

