from bottle import route, run, template, static_file
import bottle
import json
import urllib2
import sqlite3, peewee

from src.persistence import entity

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/')
def service():
    return True
    
bottle.debug(True)
conn = sqlite3.connect('sqlite.db')
run(host='localhost', port=8090)