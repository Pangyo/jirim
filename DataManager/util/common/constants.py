# -*- coding: utf-8 -*-
""" Author : Jae Eun Yoo """

# Web Server Configuration
ACCESSIBLE_IP		= "0.0.0.0"
ACCESSIBLE_PORT		= 8080
ACCESSIBLE_ADDR		= (ACCESSIBLE_IP, ACCESSIBLE_PORT)


# HTTP Response Definition
RC_OK = 200
RM_OK = "Request Handled Successfully."

RC_BAD_REQUEST = 400
RM_BAD_REQUEST = "Bad Request."


# Rank Data Types Definition
RANK_REALTIME = "REALTIME"
TYPE_RANK_REALTIME = [["rank", "INT(100)"], ["title", "VARCHAR(100)"], ["link", "TEXT"]]