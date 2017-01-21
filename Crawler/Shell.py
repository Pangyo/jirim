
from Helper.LogHelper import LOG
from Helper.XmlHelper import XML

from Common.Global import Global
from Common.CommonClass.BaseClass import BaseClass

from Product.RankListManager.Service.rankListService import RankListService
from Product.RelationListManager.Service.relationService import RelationService

class ShellMain(BaseClass):
    
    def __init__(self):
        
        self._rankListService = None
        self._relationListService = None
        
        # after json , now not use
        self._jsRankObject = None    
        self._jsRelationObject = None
        
    def Pre_Initialize(self):
        LOG.DEBUG("Pre-initialize.")
       
        self._rankListService = RankListService()
        self._relationListService = RelationService() 
     
    def Startup(self):
        self.Pre_Initialize()
        
    def GetRelationList(self, rList):
        LOG.DEBUG("GetRelationList[Initilize]")

        for node in rList:
            tempList = self._relationListService.GetRelationList(node.link)
            LOG.DEBUG("GetRelationList[List Complete]")

            XML.RelationListToXML(tempList, node.index, node.title)
            LOG.DEBUG("GetRelationList[SaveXML]")   
        
        
    def GetRankList(self):
        LOG.DEBUG("GetRankList[Initilize]")
        
        tempList = self._rankListService.GetRealTimeRankList("http://www.naver.com")
        tempList.pop()
        LOG.DEBUG("GetRankList[List Complete]")
        
        XMLCheck = XML.RanklistToXML(tempList)
        LOG.DEBUG("GetRankList[SaveXML]")

        if XMLCheck == True:
            return tempList
        else:
            return None
            
if __name__ == '__main__':

    sm = ShellMain()
    sm.Startup()

    tempList = sm.GetRankList()
    if tempList != None:
        sm.GetRelationList(tempList)
 

    #run(host='111.111.111.2', port=8085)
        #_jsRelationObject = _jsRankObject = json.dumps(tempList, default=lambda o: o.__dict__, indent=4)
        #print(_jsRelationObject)
        #return _jsRelationObject

        #_jsRankObject = json.dumps(tempList, default=lambda o: o.__dict__, indent=4)
        #print(_jsRankObject)
        
        #return _jsRankObject