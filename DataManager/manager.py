# -*- coding: utf-8 -*-
""" Author : Jae Eun Yoo """


from util.common.constants import *
from util.database.helper import *
from util.database.query import *

from datetime import date
from flask import Flask, request, abort, Response
import sqlite3
import json

data_manager = Flask(__name__)

def decode_request_data(data, data_type="json"):
	data = None
	if data_type is "json":
		data = json.loads(response_data.decode("utf-8"))
	
	elif data_type is "xml" :
		pass

	return data


def is_right_format(data, data_type):
	for column_name, _ in data_type:
		if not column_name in data:
			return False

	return True


@data_manager.route("/api/crawler/rank/<rank_type>", methods=["POST"])
def handle_crawler_rank(rank_type):
	response = dict()
	rank_list = decode_request_data(request.data)

	if rank_type is RANK_REALTIME:
		if type(rank_list) is not list:
			pass

		for rank in rank_list:
			if type(rank) is not dict:
				pass

			if not is_right_format(rank, TYPE_RANK_REALTIME):
				pass

			crawled_data = list()
			for key, _ in TYPE_RANK_REALTIME:
				crawled_data.append(rank[key])

			insert_rank(title=RANK_REALTIME, data=crawled_data)


# @data_manager.route("/api/crawler/relation/<realation_type>", methods=["POST"])
# def handle_crawler_relation(relation_type):
# 	response = dict()
# 	rank_list = json.loads(response_data.decode("utf-8"))

# 	if realation_type is "realti me":
# 		if type(rank_list) is not dict:
# 			pass

# 		for rank in rank_list:
# 			if type(rank) is not dict:
# 				pass

# 			if not is_right_rank_list(rank, "index", "title", "link"):
# 				pass

# 		save(rank_list)	


if __name__ == '__main__':
	data_manager.run(debug=True,host=ACCESSIBLE_IP,port=ACCESSIBLE_PORT)