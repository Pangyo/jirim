from bottle import request, route, get, template, static_file
import bottle

import logging
from logging import debug, info, error

import json
import urllib2
import signal
import sys

# Static Routes
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    response = bottle.static_file(filepath, root="static/css")
    response.set_header("Cache-Control", "public, max-age=604800")

    return response

# @get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
# def font(filepath):
#     return static_file(filepath, root="static/font")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    response = bottle.static_file(filepath, root="static/img")
    response.set_header("Cache-Control", "public, max-age=604800")
    return response


@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    debug(filepath)
    response = bottle.static_file(filepath, root="static/js")
    response.set_header("Cache-Control", "public, max-age=604800")
    return response

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

    graphJson = {
        "result":[
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%9D%B4%ED%96%A5&sm=top_lve&ie=utf8",
                "title":"%EC%9D%B4%ED%96%A5",
                "index":"1"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%82%B0%EB%8B%A4%EB%9D%BC%EB%B0%95&sm=top_lve&ie=utf8",
                "title":"%EC%82%B0%EB%8B%A4%EB%9D%BC%EB%B0%95",
                "index":"2"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%B2%9C%EB%91%A5&sm=top_lve&ie=utf8",
                "title":"%EC%B2%9C%EB%91%A5",
                "index":"3"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=10%EC%96%B5%EC%97%94&sm=top_lve&ie=utf8",
                "title":"10%EC%96%B5%EC%97%94",
                "index":"4"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=1%EB%B0%952%EC%9D%BC&sm=top_lve&ie=utf8",
                "title":"1%EB%B0%952%EC%9D%BC",
                "index":"5"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%A0%95%EC%9B%90%EC%8A%A4%EB%8B%98&sm=top_lve&ie=utf8",
                "title":"%EC%A0%95%EC%9B%90%EC%8A%A4%EB%8B%98",
                "index":"6"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=top_lve&ie=utf8",
                "title":"%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95",
                "index":"7"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%9E%84%EC%9D%80%EC%88%98&sm=top_lve&ie=utf8",
                "title":"%EC%9E%84%EC%9D%80%EC%88%98",
                "index":"8"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%A0%95%EA%B7%9C%EC%9E%AC&sm=top_lve&ie=utf8",
                "title":"%EC%A0%95%EA%B7%9C%EC%9E%AC",
                "index":"9"
            },
            {
                "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%8A%88%ED%8D%BC%EB%A7%A8%EC%9D%B4%EB%8F%8C%EC%95%84%EC%99%94%EB%8B%A4&sm=top_lve&ie=utf8",
                "title":"%EC%8A%88%ED%8D%BC%EB%A7%A8%EC%9D%B4%EB%8F%8C%EC%95%84%EC%99%94%EB%8B%A4",
                "index":"10"
            }
        ]
}


    debug(graphJson)

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

logging.basicConfig(filename='web.log',level=logging.DEBUG)

signal.signal(signal.SIGINT, signal_handler)

bottle.run(host='localhost', port=80, debug=True)


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
