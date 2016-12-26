from bottle import request, route, get, run, template, static_file
import bottle

import logging
from logging import debug, info, error

import json
import urllib2
import signal
import sys

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')
    
@route('/map')
def map():
    return template('views/map')
    
    
@route('/map2')
def map():
    return template('views/map2')
    
@route('/')
def hello():
    # id title from
    response = urllib2.urlopen('http://111.111.111.2:8085/keywords')
    json_str = response.read()
    print "from servers.."
    print json_str
    
    json_obj = json.loads(json_str);
    
    return template('views/home', infos=json_obj)

@get('/graph')
def hello():
    url_encoded_keyword = request.query.keyword
   
    info(url_encoded_keyword) 
    keyword = urldecode(url_encoded_keyword)
    
    graphJson = {
       "exid":[
          {
             "name":"aoa",
             "link":"https://www.naver.com"
          }
       ]
    }
    
    return template('views/home', keyword=keyword, graph=graphJson)
    
@bottle.error(404)
def error404(error):
    return 'Nothing here, sorry'

def signal_handler(signal, frame):
    print('process down')
    sys.exit(0)
 
    
def urlencode(s): 
    return urllib2.quote(s)

def urldecode(s):
    return urllib2.unquote(s).decode('utf8')
	
bottle.debug(True)
logging.basicConfig(filename='web.log',level=logging.DEBUG)

signal.signal(signal.SIGINT, signal_handler)

run(host='localhost', port=80)


# <html>
#{{infos}}
#         <ul>
#          % for info in infos:
#             <li>
#             </li>       
#            <br> 
#          % end
#         </ul>
#</html>
