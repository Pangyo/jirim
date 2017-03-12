# -*- coding: utf-8 -*-
""" Author : Gary J """
from jirim.mongo.utils import utils


class MongoDao() :

    def __init__(self):
        self.client = None
        self.db = None
        pass

    def connect(self, dbname):
        self.client, self.db = utils.connect(dbname)
        return self.client, self.db

    def getClient(self):
        return self.client

    def getDB(self):
        return self.db

    def getCollection(self, collectionName):
        if self.db != None:
            return self.db[collectionName]

    def close(self):
        self.client.close()



