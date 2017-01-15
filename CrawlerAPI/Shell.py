from bottle import route, run, template, request

import json

from Helper import LOG
from Helper import XML
from Helper import JSON

RankListData = None

def IsInt(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

@route('/v1/crawler/ranklist/<param>')
def api_ranklist(param):
    rankList = Shell.GetRankList()    
    if rankList == None:
        return "rank list is empty"

    if param == "range":
        start = request.query.start
        end = request.query.end
        
        if IsInt(start) == False:
            return "range start is not Int."
        if IsInt(end) == False:
            return "range end is not Int."
        
        startINT = int(start)
        endINT = int(end)

        if startINT < 1:
            return "display range Invalid"
        if endINT > 10:
            return "display range Invalid"

        tempList = rankList[startINT:endINT]

        jsObject = JSON.ConvertListToJson(tempList)
        if jsObject == None:
            return "Json is empty"
        
        return jsObject
    
@route('/v1/crawler/ranklist')
def api_ranklist1():
    display = request.query.display
    
    rankList = Shell.GetRankList()    
    if rankList == None:
        return "rank list is empty"

    if display == "":
        jsObject = JSON.ConvertListToJson(rankList)
        if jsObject == None:
            return "Json is empty"
        
        return jsObject
    else:
        if IsInt(display) == False:
            return "display is not Int."
        
        displayINT = int(display)
        if displayINT > 10:
            return "display range Invalid"
        if displayINT < 1:
            return "display range Invalid"
        
        tempList = rankList[0:displayINT]

        jsObject = JSON.ConvertListToJson(tempList)
        if jsObject == None:
            return "Json is empty"
        
        return jsObject

class Shell(object):
    def __init__(self):
        service = None

    @staticmethod
    def GetRankList():
        global RankListData
        return RankListData

    @staticmethod
    def SetRankList(ranklist):
        global RankListData
        RankListData = ranklist

if __name__ == '__main__':
        
    sm = Shell()

    tempList = XML.XMLToRanklist()
    sm.SetRankList(tempList)

    #run(host='172.16.0.149', port=8080)

