
#from bottle import route, run, template

from Helper.LogHelper import LOG
#from Helper.XmlHelper import XML

from Common.CommonClass.BaseClass import BaseClass

import urllib.request
from bs4 import BeautifulSoup
#import json


def index():
    return sm.Startup()

class ShellMain(BaseClass):
    
    def __init__(self):
       pass 

    def Pre_Initialize(self):
        LOG.DEBUG("Pre-initialize.")
     
    def Startup(self):
        self.Pre_Initialize()

    def httprequesets(self):
        req = urllib.request.Request("http://www.naver.com")
        data = urllib.request.urlopen(req).read() # data = urllib.requset.urlopen("http://www.daum.net").read()
        soup = BeautifulSoup(data, 'html.parser')
        LOG.DEBUG(soup.title.string)
        
if __name__ == '__main__':

    #xml parser, file handle, 
    LOG.INFO("Hello World")
    sm = ShellMain()
    sm.Startup()
    sm.httprequesets()




    '''
    sm = ShellMain()
    sm.Startup()
   
    tempList = sm.GetRankList()
    if tempList != None:
        sm.GetRelationList(tempList)
 
'''
    #run(host='111.111.111.2', port=8085)
    


        #_jsRelationObject = _jsRankObject = json.dumps(tempList, default=lambda o: o.__dict__, indent=4)
        #print(_jsRelationObject)
        #return _jsRelationObject

        #_jsRankObject = json.dumps(tempList, default=lambda o: o.__dict__, indent=4)
        #print(_jsRankObject)
        
        #return _jsRankObject
