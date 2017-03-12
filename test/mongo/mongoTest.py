# -*- coding: utf-8 -*-
""" Author : Gary J """

import unittest

from jirim.log import helper
from jirim.config.mongo import mongoConfig
from jirim.mongo.utils.mongoDao import MongoDao



class TestMongoConnection(unittest.TestCase):

    def setUp(self):
        self.log = helper.get_logger("test")
        self.mongoDao = MongoDao()
        self.client, self.db = self.mongoDao.connect(mongoConfig.DATABASE_NAME)

    def test_insert(self):
        rawDataCollection = self.mongoDao.getCollection(mongoConfig.RAWDATA_COLLECTION)
        id = 1
        name = "Gwiyeong"
        firstName = "Jeong"
        rawDataCollection.insert_one({"name":name, "id":id, "firstName" : firstName})
        myData = rawDataCollection.find_one({"id":1})
        self.assertIsNotNone(myData)
        self.assertEqual(name, myData['name'], "")
        self.assertEqual(firstName, myData['firstName'], "")




if __name__ == '__main__':
    unittest.main()
