import shutil

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

        if INI.Initialize() == False:
            return False
        
        if INI.ReadINI() == False:  
            return False

        if INI.WriteINI() == False:
            return False

        if LOG.Initialize() == False:
            return False

        LOG.DEBUG("Pre-initialize.")


    def Post_Initialize(self):
        LOG.DEBUG("Post-initialize.")
       
        self._rankListService = RankListService()
        self._relationListService = RelationService() 


    def Startup(self):
        self.Pre_Initialize()

        self.Post_Initialize()

    def GetRelationList(self, rList):
        LOG.DEBUG("Initilize - Relation")

        for node in rList:
            tempList = self._relationListService.GetRelationList(node.link)
            LOG.DEBUG("Get List Data - Relation")

            # Rank List delete from INI RelationListCount
            listCount = Global.GetRelationCount()
            while(True):
                if(len(tempList) <= int(listCount)):
                    break;
                else:
                    tempList.pop()

            if XML.RelationListToXML(tempList, node.index, node.title) == True:
                LOG.DEBUG("Save Xml - Relation")
            else:
                LOG.FATAL("Fail Xml - Relation")
                return False

        return True
        
    def GetRankList(self, url):
        LOG.DEBUG("Initilize - Rank")
        
        tempList = self._rankListService.GetRealTimeRankList(url)
        LOG.DEBUG("Get List Data - Rank")
        
        # Rank List delete from INI RankListCount
        listCount = Global.GetRankListCount()
        
        while(True):
            if(len(tempList) <= int(listCount)):
                break;
            else:
               tempList.pop()
       
        if XML.RanklistToXML(tempList) == True:
            LOG.DEBUG("Save Xml - Rank")
            return tempList
        else:
            LOG.FATAL("Fail Xml - Rank")
            return None


if __name__ == '__main__':

    sm = ShellMain()
    sm.Startup()

    result = None
    tempList = sm.GetRankList("http://www.naver.com")
    
    if tempList != None:
        reuslt = sm.GetRelationList(tempList)

    try:
        if reuslt == True:
            shutil.copyfile(Global.GetXmlFilePath(), Global.GetXmlFileName())

    except IOError as e:
        LOG.FATAL("Crawler File Copy Fail" + e)
    else:
        LOG.DEBUG("Crawler File Copy Success")
    
