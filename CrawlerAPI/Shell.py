from bottle import route, run, template, request

import json

from Helper import LOG
from Helper import XML
from Helper import JSON
from Helper import FUNC

RankListData = None
RelationListData = None
CrawlerDict = dict()

@route('/v1/crawler/ranklist/<param>')
def api_ranklistRange(param):
    rankList = Shell.GetRankList()    
    if rankList == None:
        return "rank list is empty"

    if param == "range":
        start = request.query.start
        end = request.query.end
        
        if FUNC.IsInt(start) == False:
            return "range start is not Int."
        if FUNC.IsInt(end) == False:
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
def api_ranklist():
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
        if FUNC.IsInt(display) == False:
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

@route('/v1/crawler/relationlist')
def api_relationlist():
    keyword = request.query.keyword
    
    cDict = Shell.GetCrawlerDict()
    tempCrawlerDict = dict()
    
    if cDict == None:
        return "dictionary is null"

    if keyword in cDict:
        for lst in cDict[keyword]:
            tempCrawlerDict.setdefault(keyword, []).append(lst)
    else:
        return "keyword is not exist in dictionary" 

    jsObject = JSON.ConvertDictToJson(tempCrawlerDict)
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

    @staticmethod
    def SetRelationList(relationlist):
        global RelationListData
        RelationListData = relationlist

    @staticmethod
    def GetRelationList():
        global RelationListData
        return RelationListData

    @staticmethod
    def GetCrawlerDict():
        global CrawlerDict
        return CrawlerDict

    @staticmethod
    def SetCrawlerDict(crawlerDict):
        global CrawlerDict
        CrawlerDict = crawlerDict

if __name__ == '__main__':
        
    tempRankList = None
    tempRelationList = None
    tempCrawlerDict = dict()

    sm = Shell()

    tempRankList = XML.XMLToRanklist()
    tempRelationList = XML.XMLToRelationlist()

    sm.SetRankList(tempRankList)
    sm.SetRelationList(tempRelationList)

    for rank in tempRankList:
        tempCrawlerDict.setdefault(rank.title, [])
        
    for relation in tempRelationList:
        if relation.value in tempCrawlerDict:
            tempCrawlerDict[relation.value].append(relation)     
        
    sm.SetCrawlerDict(tempCrawlerDict) 

    #jsObject = json.dumps(CrawlerDict, ensure_ascii = False, default=lambda o: o.__dict__, indent=4)

    #run(host='192.168.21.122', port=8080)

