import json
import requests

from Helper.LogHelper import LOG
from Common.Global import Global

def ConvertRankListToJson(rList):
    
    jsObject = None

    if rList == None:
        return jsObject

    if isinstance(rList, list) == False:
        LOG.FATAL("rList is not list.")
        return jsObject
        
    try:
        #jsObject = json.dumps(rList, ensure_ascii = False, default=lambda o: o.__dict__, indent=4)
        jsObject = json.dumps(rList, default=lambda o: o.__dict__, indent=4)
    except:
        LOG.FATAL("convert list to json fail Rank")
    else:
        LOG.DEBUG("Success. list to json Rank")

    return jsObject
    
def ConvertRelationListToJson(title, rList):

    jsObject = None

    if rList == None:
        return jsObject

    if isinstance(rList, list) == False:
        LOG.FATAL("rList is not list.")
        return jsObject

    try:
        convertdict = dict()
        for lst in rList:
            convertdict.setdefault(title, []).append(lst)

        jsObject = json.dumps(convertdict, default=lambda o: o.__dict__, indent=4)
        
    except:
        LOG.FATAL("convert list to json fail Relation = " + title)
    else:
        LOG.DEBUG("Success. list to json Relation = " + title)

    return jsObject

def SendToServer(jsStr):
    
    serverip = Global.GetServerIP()
    if jsStr == None:
        LOG.FATAL("Json is None")
        return False

    if serverip == 'None':
        LOG.FATAL("server IP is None")
        return False

    try:
        requests.post(serverip, jsStr)

    except requests.exceptions.RequestException as e:
        LOG.FATAL("Fail. Send to Server : " + e)
        return False
    else:
        LOG.DEBUG("Success. Send to Server")
        return True
    