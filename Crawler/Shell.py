
from Helper.LogHelper import LOG
from Helper.XmlHelper import XML
from Helper.InIHelper import INI

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
    
        if INI.Initialize() == False:
            return False
        
        if INI.ReadINI() == False:  
            return False

        if INI.WriteINI() == False:
            return False

    def Post_Initialize(self):
        LOG.DEBUG("Post-initialize.")
       
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

    #tempList = sm.GetRankList()
    #if tempList != None:
    #    sm.GetRelationList(tempList)
 
