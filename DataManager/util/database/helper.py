# -*- coding: utf-8 -*-
""" Author : Jae Eun Yoo """

import MySQLdb as db
import time
from datetime import date, datetime
from util.database.query import *
from util.common.constants import *

def get_cursor():
	try:
		conn = db.connect("localhost", "root", "rlaskagns", "jirim" )
		return conn, conn.cursor()
	except:
		return None, None


def is_table(title):
	conn, cursor = get_cursor();
	cursor.execute("SHOW TABLES;")
	title += date.today().strftime("_%Y_%m_%d")
	titles = cursor.fetchall()
	for title_tuple in titles:
		if title == title_tuple[0]:
			conn.close()
			return True

	conn.close()
	return False



def create_table(title=None, columns=None):
	if not (title and columns):
		return False

	conn, cursor = get_cursor()
	if not (conn and cursor):
		return False

	try:
		title += date.today().strftime("_%Y_%m_%d")
		cursor.execute(query_create_table(title=title, columns=columns))
		conn.commit()
		conn.close()
		return True

	except:
		conn.close()
		return False


def insert_rank(title=None, data=None):
	if not (title and data):
		return False

	if not is_table(title):
		if title is RANK_REALTIME:
			create_table(title=RANK_REALTIME, columns=TYPE_RANK_REALTIME)

	conn, cursor = get_cursor()
	if not (conn and cursor):
		return False

	if title is RANK_REALTIME:
		data.insert(0, datetime.now().strftime("%H:%M:%S"))
		title += date.today().strftime("_%Y_%m_%d")
		cursor.execute(query_insert_rank(title, TYPE_RANK_REALTIME), data)
		conn.commit()
		conn.close()


def select_rank():
	pass

def insert_relation():
	pass

def select_relation():
	pass