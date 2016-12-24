
from bottle import route, run, template

from Helper.LogHelper import LOG
from Helper.XmlHelper import XML

from Common.CommonClass.BaseClass import BaseClass

from Product.RankListManager.Service.rankListService import RankListService
from Product.RelationListManager.Service.relationService import RelationService

import json

@route('/keywords')
def index():
    return sm.Startup()


class ShellMain(BaseClass):
    
    def __init__(self):
        self._rankList = None
        self._relationList = None
        
        self._jsRankObject = None    
        self._jsRelationObject = None
        
    def Pre_Initialize(self):
        LOG.DEBUG("Pre-initialize.")
        
        #self._president = PresidentService()
        self._rankList = RankListService()
        #self._relat ionList = RelationService() 
     
    def Startup(self):
        self.Pre_Initialize()
        
    def GetRelationList(self):
        tempList = self._relationList.GetRelationList("https://search.naver.com/search.naver?where=nexearch&query=%EA%B9%80%EC%9C%A0%EC%A0%95&sm=top_lve&ie=utf8")
        
        #_jsRelationObject = _jsRankObject = json.dumps(tempList, default=lambda o: o.__dict__, indent=4)
        #print(_jsRelationObject)
        #return _jsRelationObject
        
    def GetRankList(self):
        
        LOG.DEBUG("Init. GetRankList")
        
        tempList = self._rankList.GetRealTimeRankList("http://www.naver.com")
        tempList.pop()

        LOG.DEBUG("Get RankList")
        
        XMLCheck = XML.RanklistToXML(tempList);

        #for node in tempList:
        #    print(node.title)
        
        #_jsRankObject = json.dumps(tempList, default=lambda o: o.__dict__, indent=4)
        #print(_jsRankObject)
        
        #return _jsRankObject
            
if __name__ == '__main__':

    sm = ShellMain()
    sm.Startup()
    
    #sm.GetRelationList()
    sm.GetRankList()
    #run(host='111.111.111.2', port=8085)
    