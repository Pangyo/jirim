from bottle import request, route, get, run, template, static_file, error
import bottle

import logging
from logging import debug

import json
import urllib2


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
    keyword = request.query.keyword
   
    debug(keyword) 

    json_obj = { "1": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EA%B9%80%EC%9C%A0%EC%A0%95&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uae40\uc720\uc815", "index": 1 }, "2": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EC%9D%B4%EC%8A%B9%ED%99%98&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uc774\uc2b9\ud658", "index": 2 }, "3": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%ED%99%A9%EC%9A%B0%EC%8A%AC%ED%98%9C&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\ud669\uc6b0\uc2ac\ud61c", "index": 3 }, "4": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EC%95%84%EB%B2%84%EB%8B%98+%EC%A0%9C%EA%B0%80+%EB%AA%A8%EC%8B%A4%EA%B2%8C%EC%9A%94&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uc544\ubc84\ub2d8 \uc81c\uac00 \ubaa8\uc2e4\uac8c\uc694", "index": 4 }, "5": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EC%84%A4%EB%AF%BC%EC%84%9D&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uc124\ubbfc\uc11d", "index": 5 }, "6": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EA%B9%80%EC%A0%9C%EB%8F%99&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uae40\uc81c\ub3d9", "index": 6 }, "7": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EB%A1%9C%EB%98%90&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\ub85c\ub610", "index": 7 }, "8": { "link": "http://search.naver.com/search.naver?where=nexearch&query=ufc&sm=top_lve&ie=utf8", "infrom": "naver", "title": "ufc", "index": 8 }, "9": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EB%B0%95%EA%B7%BC%ED%98%9C&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\ubc15\uadfc\ud61c", "index": 9 }, "10": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EC%98%A4%EB%8A%98%EB%82%A0%EC%94%A8&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uc624\ub298\ub0a0\uc528", "index": 10 }, "11": { "link": "http://search.naver.com/search.naver?where=nexearch&query=%EA%B9%80%EC%9C%A0%EC%A0%95&sm=top_lve&ie=utf8", "infrom": "naver", "title": "\uae40\uc720\uc815", "index": 11 } }

    return template('views/home', keyword=keyword, infos=json_obj)
    
@error(404)
def error404(error):
    return 'Nothing here, sorry'

	
bottle.debug(True)
logging.basicConfig(filename='web.log',level=logging.DEBUG)

run(host='10.0.2.15', port=8080)


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
