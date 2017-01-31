import json
from Helper import LOG

def ConvertDictToJson(rDict):

    _jsDict = None
    
    if isinstance(rDict, dict) == False:
        LOG.FATAL("rDict is not dictionary.")
        return _jsDict

    try:
        _jsDict = json.dumps(rDict, ensure_ascii = False, default=lambda o: o.__dict__, indent=4)
    except:
        LOG.FATAL("convert dictionary to json fail")
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