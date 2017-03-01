# -*- coding: utf-8 -*-
""" Author : Jae Eun Yoo """


from util.common.constants import *
from util.database.helper import *
from flask import Flask, request, abort, Response


data_manager = Flask(__name__)


@data_manager.route("/")
def test():
	return "hello"

# if __name__ == '__main__':
# 	print(ACCESSIBLE_ADDR)
# 	# data_manager.run(debug=True,host=ACCESSIBLE_IP,port=ACCESSIBLE_PORT)