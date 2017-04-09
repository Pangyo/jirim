# -*- coding: utf-8 -*-
""" Author : Jae Eun Yoo """
SHOW_TABLES = "SHOW TABLES;"

def query_create_table(title, columns):
	query = "CREATE TABLE {title}(time TIME".format(title=title)
	for column_name, column_type in columns:
		query += ", {column_name} {column_type}".format(column_name=column_name, column_type=column_type)
	
	query += ");"
	return query


def query_insert_rank(title, rank_type):
	query = "INSERT INTO {title}(time".format(title=title)
	value_area = ") VALUES (%s"
	for column_name, _ in rank_type:
		query += ", {column_name}".format(column_name=column_name)
		value_area += ", %s"

	value_area += ");"
	query += value_area
	return query
