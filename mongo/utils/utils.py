# -*- coding: utf-8 -*-
""" Author : Gary J """

from pymongo import MongoClient
from jirim.log import helper
from jirim.config.mongo import mongoConfig

log = helper.get_logger("mongoUtils")


def connect(dbname, username=None, password=None):

    try:
        client = MongoClient(host=mongoConfig.HOST, port=mongoConfig.PORT, connect=False)
    except Exception as e:
        log.error("Error trying to connect: %s" % str(e))
    db = client[dbname]
    if username:
        if password == None:
            try:
                db.authenticate(username, password, mechanism='MONGODB-CR')
            except Exception as e:
                log.error("Error trying to authenticate: %s" % str(e), -3)
    return client, db
