# -*- coding: utf-8 -*-
""" Author : Jae Eun Yoo """
from util.common.constants import ACCESSIBLE_ADDR
from gevent.wsgi import WSGIServer
from manager import data_manager
from datetime import timedelta

if __name__ == '__main__':
	print("Data Manager start..")
	servers = list()
	data_manager.debug = True
	data_manager.permanent_session_lifetime = timedelta(minutes=5)
	servers.append(WSGIServer(ACCESSIBLE_ADDR,data_manager))
	for server in servers:
		server.serve_forever()
