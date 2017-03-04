from bottle import route, run, template, request

import json
import sys

from Helper import LOG
from Helper import XML
from Helper import JSON
from Helper import FUNC
from Helper import INI

from Helper.Global import Global


@route('/crawler/api/ranklist')
def api_ranklist():
    p = JSON.PacketClass()
    dic = dict()

    displayCount = request.query.display    
    rankList = Global.GetRankDataList()
    
    if rankList == None:
        p.setPacket("404", "fail" , "rank list is empty", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)

    if FUNC.IsInt(request.query.display) == False:
        p.setPacket("404", "fail" , "display is not Int.", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)
    
    if int(request.query.display) > 10:
        p.setPacket("404", "fail" , "display range Invalid", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)
    
    if int(request.query.display) < 1:
        p.setPacket("404", "fail" , "display range Invalid", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)
   
    # range list -> dictionary
    dic = JSON.ConvertRankListToDict(rankList[0 : int(request.query.display)])

    if dic == None:
        p.setPacket("404", "fail" , "rankList is Null", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)
        
    # Success
    p.setPacket("200", "success", "", dic)
    jsObject = JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)
    return jsObject

@route('/crawler/api/relationlist')
def api_relationlist():
    p = JSON.PacketClass()
    dic = dict()
    
    keyword = request.query.keyword    
    relationDict = Global.GetRelationDict()
    
    if keyword == "":
        p.setPacket("404", "fail" , "keyword is empty", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)
    
    if relationDict == None:
        p.setPacket("404", "fail" , "relation list is empty", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)

    if (keyword in relationDict) == False:
        p.setPacket("404", "fail" , "keyword is not exist in dictionary", None)
        return JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)

    # keyword relation -> dictionary
    for lst in relationDict[keyword]:
            dic.setdefault(keyword, []).append(lst)

    # Success
    p.setPacket("200", "success", "", dic)
    jsObject = JSON.MakePacket(p.header.code, p.header.status,p.header.msg,p.body.data)

    return jsObject

class Shell(object):
    def __init__(self):
        service = None

    def Pre_Initialize(self):

        if INI.Initialize() == False:
            sys.exit()

        if INI.ReadINI() == False:
            sys.exit()

        if INI.WriteINI() == False:
            sys.exit()

        if LOG.Initialize() == False:
            sys.exit()

        LOG.DEBUG("Initialize")

    def Post_Initialize(self):

        tempRankList = XML.XMLToRanklist()
        if tempRankList == None:
            sys.exit()
    
        LOG.DEBUG("Init - rank List")

        tempRelationList = XML.XMLToRelationlist()
        if tempRelationList == None:
            sys.exit()

        LOG.DEBUG("Init - relation List")

        tempRankDict = JSON.ConvertRankListToDict(tempRankList)
        if tempRankDict == None:
            sys.exit()

        LOG.DEBUG("Init - rank Dictionary")

        tempRelationDict = JSON.ConvertRelationListToDict(tempRankList, tempRelationList)
        if tempRelationDict == None:
            sys.exit()

        LOG.DEBUG("Init - relation Dictionary")

        Global.SetRankDataList(tempRankList)
        Global.SetRelationList(tempRelationList)
        Global.SetRankDataDict(tempRankDict)
        Global.SetRelationDict(tempRelationDict)

if __name__ == '__main__':
        
    sm = Shell()
    sm.Pre_Initialize()
    sm.Post_Initialize()
    
    LOG.DEBUG("Start Service.")

    run(host='localhost', port=8080)

