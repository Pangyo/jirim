from bottle import request, route, get, template, static_file
import bottle

import logging
from logging import debug, info, error

import json
import urllib.parse
import signal
import sys

# Static Routes
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    debug(filepath)
    response = bottle.static_file(filepath, root="static/css")
    response.set_header("Cache-Control", "public, max-age=604800")

    return response

@get("/static/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/fonts")

@get("/static/css/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/fonts")

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

    json_obj = json.loads(json_str);

    return template('views/home', infos=json_obj)

@get('/sample')
def sample():
    return template('views/sample')

@get('/graph')
def hello():
    url_encoded_keyword = request.query.keyword
    info(url_encoded_keyword)

    keyword = urldecode(url_encoded_keyword)

    graphJson = {
        "relations":[
    {
        "key":"1",
        "title":"제안대군",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%A0%9C%EC%95%88%EB%8C%80%EA%B5%B0&sm=top_lve&ie=utf8",
        "relations" : [
            {
                "key":"1",
                "title":"성종",
                "link":"?where=nexearch&query=%EC%84%B1%EC%A2%85&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군",
            },
            {
                "key":"1",
                "title":"안순왕후",
                "link":"?where=nexearch&query=%EC%95%88%EC%88%9C%EC%99%95%ED%9B%84&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"예종",
                "link":"?where=nexearch&query=%EC%98%88%EC%A2%85&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"조선 성종",
                "link":"?where=nexearch&query=%EC%A1%B0%EC%84%A0+%EC%84%B1%EC%A2%85&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"자을산군",
                "link":"?where=nexearch&query=%EC%9E%90%EC%9D%84%EC%82%B0%EA%B5%B0&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"인혜왕대비",
                "link":"?where=nexearch&query=%EC%9D%B8%ED%98%9C%EC%99%95%EB%8C%80%EB%B9%84&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"조선 제안대군",
                "link":"?where=nexearch&query=%EC%A1%B0%EC%84%A0+%EC%A0%9C%EC%95%88%EB%8C%80%EA%B5%B0&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"예종 가계도",
                "link":"?where=nexearch&query=%EC%98%88%EC%A2%85+%EA%B0%80%EA%B3%84%EB%8F%84&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"한명회",
                "link":"?where=nexearch&query=%ED%95%9C%EB%AA%85%ED%9A%8C&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"쾌도난마",
                "link":"?where=nexearch&query=%EC%BE%8C%EB%8F%84%EB%82%9C%EB%A7%88&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"자성대왕대비",
                "link":"?where=nexearch&query=%EC%9E%90%EC%84%B1%EB%8C%80%EC%99%95%EB%8C%80%EB%B9%84&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"성종과제안대군",
                "link":"?where=nexearch&query=%EC%84%B1%EC%A2%85%EA%B3%BC%EC%A0%9C%EC%95%88%EB%8C%80%EA%B5%B0&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"천일야사",
                "link":"?where=nexearch&query=%EC%B2%9C%EC%9D%BC%EC%95%BC%EC%82%AC&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"지운",
                "link":"?where=nexearch&query=%EC%A7%80%EC%9A%B4&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"예종의 아들",
                "link":"?where=nexearch&query=%EC%98%88%EC%A2%85%EC%9D%98+%EC%95%84%EB%93%A4&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"인성대군",
                "link":"?where=nexearch&query=%EC%9D%B8%EC%84%B1%EB%8C%80%EA%B5%B0&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"월산대군",
                "link":"?where=nexearch&query=%EC%9B%94%EC%82%B0%EB%8C%80%EA%B5%B0&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"의경세자",
                "link":"?where=nexearch&query=%EC%9D%98%EA%B2%BD%EC%84%B8%EC%9E%90&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"인수대비",
                "link":"?where=nexearch&query=%EC%9D%B8%EC%88%98%EB%8C%80%EB%B9%84&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            },
            {
                "key":"1",
                "title":"연산군",
                "link":"?where=nexearch&query=%EC%97%B0%EC%82%B0%EA%B5%B0&ie=utf8&sm=tab_she&qdt=0",
                "value":"제안대군"
            }
        ]
    },
    {
        "key":"2",
        "title":"한국사능력검정시험 34회",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%ED%95%9C%EA%B5%AD%EC%82%AC%EB%8A%A5%EB%A0%A5%EA%B2%80%EC%A0%95%EC%8B%9C%ED%97%98+34%ED%9A%8C&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"3",
        "title":"트럼프",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%ED%8A%B8%EB%9F%BC%ED%94%84&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"4",
        "title":"2ne1",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=2ne1&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"5",
        "title":"헨리",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%ED%97%A8%EB%A6%AC&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"6",
        "title":"나혼자산다",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%EB%82%98%ED%98%BC%EC%9E%90%EC%82%B0%EB%8B%A4&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"7",
        "title":"팬텀싱어",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%ED%8C%AC%ED%85%80%EC%8B%B1%EC%96%B4&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"8",
        "title":"수지 화보",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%88%98%EC%A7%80+%ED%99%94%EB%B3%B4&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"9",
        "title":"편의점을 털어라",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%ED%8E%B8%EC%9D%98%EC%A0%90%EC%9D%84+%ED%84%B8%EC%96%B4%EB%9D%BC&sm=top_lve&ie=utf8",
        "relations": []
    },
    {
        "key":"10",
        "title":"조우진",
        "link":"http://search.naver.com/search.naver?where=nexearch&query=%EC%A1%B0%EC%9A%B0%EC%A7%84&sm=top_lve&ie=utf8",
        "relations": []
    }
]
}

#    debug(graphJson)

    return template('views/home', keyword=keyword, graph=graphJson)

@bottle.error(404)
def error404(error):
    return 'Nothing here, sorry'

@bottle.error(500)
def error404(error):
    return 'Internal Error, sorry'

def signal_handler(signal, frame):
    print('process down')
    sys.exit(0)

def urldecode(s):
    return urllib.parse.unquote(s)

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
