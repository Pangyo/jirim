import json
from Helper import LOG
from enum import Enum

class HeaderClass():
    def __init__(self):
        pass

    def setCode(self, code):
        self.code = code
    
    def setStatus(self, status):
        self.status = status
    
    def setMsg(self, msg):
        self.msg = msg

class BodyClass():
    def __init__(self):
        self.data.setdefault("data", dict)

    def setData(self, data):
        self.data = data

    data = dict()

class PacketClass():
    def __init__(self):
        self.packet.setdefault("header", HeaderClass)
        self.packet.setdefault("body", BodyClass)

    def makePacket(self):
        self.packet["header"] = header
        self.packet["body"] = body

    def setPacket(self, code, status, msg, rdict):
        self.header.setCode(code)
        self.header.setStatus(status)
        self.header.setMsg(msg)

        self.body.setData(rdict)
        
    packet = dict()
    header = HeaderClass()
    body = BodyClass()

def ConvertRankListToDict(ranklist):
    rankDict = dict()

    if ranklist == None:
        return None

    try:
        for lst in ranklist:
            rankDict.setdefault(lst.title, []).append(lst)

    except:
        return None
    else:
        return rankDict

def ConvertRelationListToDict(ranklist, relationlist):
    relationDict= dict()

    if ranklist == None:
        return None

    if relationlist == None:
        return None

    try:
        for rank in ranklist:
            relationDict.setdefault(rank.title, [])
        
        for relation in relationlist:
            if relation.value in relationDict:
                relationDict[relation.value].append(relation)
    except:
        return None
    else:
        return relationDict

def MakePacket(code, status, msg, rdict):
    
    # Init
    _h = HeaderClass()
    headerCode = code
    headerStatus = status
    headerMsg = msg

    _b = BodyClass()
    bodyData = rdict

    _p = PacketClass()

    # Set Header
    _h.setCode(headerCode)
    _h.setStatus(headerStatus)
    _h.setMsg(headerMsg)    

    # Set Body
    _b.setData(bodyData)

    # Set Packet
    _p.packet['header'] = _h 
    _p.packet['body'] = _b

    jsObject = ConvertDictToJson(_p.packet)
    if jsObject == None:
        return None
    
    return jsObject

def ConvertDictToJson(rDict):

    _jsDict = None
    
    if isinstance(rDict, dict) == False:
        LOG.FATAL("rDict is not dictionary.")
        return _jsDict

    try:
        _jsDict = json.dumps(rDict, ensure_ascii = False, default=lambda o: o.__dict__, indent=4)
    except:
        LOG.FATAL("convert dictionary to json fail")
        return None
    else:
        LOG.DEBUG("Success. dictionary to json")

    return _jsDict
    

def ConvertListToJson(rlist):

    _jsList = None
    
    if isinstance(rlist, list) == False:
        LOG.FATAL("rList is not list.")
        return _jsList
    
    try:
       _jsList = json.dumps(rlist, ensure_ascii = False, default=lambda o: o.__dict__, indent=4)
    except:
       LOG.FATAL("convert list to json fail")
    else:
       LOG.DEBUG("Success. list to json")
    
    return _jsList


def ConvertStrToJson(rStr):
    _jsStr = None

    if rStr == None:
        LOG.FATAL("rStr is not String.")
        return _jsStr
    
    try:
        _jsSTr = json.dump(rStr, ensure_ascii = False)
    except:
        LOG.FATAL("convert String to json fail")
    else:
        LOG.DEBUG("Success. String to json")

    return _jsStr