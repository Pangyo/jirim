import shutil

from Helper.LogHelper import LOG
from Helper.XmlHelper import XML
from Helper.JsonHelper import JSON

from Common.Global import Global
from Common.CommonClass.BaseClass import BaseClass

from Product.RankListManager.Service.rankListService import RankListService
from Product.RelationListManager.Service.relationService import RelationService

class ShellProcess(BaseClass):
    
    def __init__(self):
        pass

    def GetRelation(self, rList):
        resultDict = dict()

        LOG.DEBUG("Initilize - Relation")
        
        for node in rList:
            List = RelationService().GetRelationList(node.link)
            LOG.DEBUG("Get List Data - Relation")

            # Rank List delete from INI RelationListCount
            tempList = self.CheckListCount(Global.GetRelationCount(), List)
            resultDict[node.title] = tempList

            # Save Xml
            if XML.RelationListToXML(tempList, node.index, node.title) == True:
                LOG.DEBUG("Save Xml - Relation")
            else:
                LOG.FATAL("Fail Xml - Relation")
                return False

        return resultDict

    def GetRankList(self, url):
        LOG.DEBUG("Initilize - Rank")
        
        List = RankListService().GetRankList(url)
        LOG.DEBUG("Get List Data - Rank")
        
        # Rank List delete from INI RankListCount
        tempList = self.CheckListCount(Global.GetRankListCount(), List)

        # Save Xml
        if XML.RanklistToXML(tempList) == True:
            LOG.DEBUG("Save Xml - Rank")
            return tempList
        else:
            LOG.FATAL("Fail Xml - Rank")
            return None

    def SendRelationList(self, rList):
        # Send Server        
        for node in rList:    
            jsStr = JSON.ConvertRelationListToJson(node, rList[node])
            result = JSON.SendToServer(jsStr)
            
            if result == False:
                return False

        return True

    def SendRankList(self, rList):
        # Send Server
        jsStr = JSON.ConvertRankListToJson(rList)
        result = JSON.SendToServer(jsStr)

        return result

    # Make Crawler.xml file 
    def CopyXML(self):
        try:
            shutil.copyfile(Global.GetXmlFilePath(), Global.GetXmlFileName())
        except IOError as e:
            LOG.FATAL("Crawler File Copy Fail" + e)
            return False
        else:
            LOG.DEBUG("Crawler File Copy Success")
            return True

    # RankList, RelationList delete count from INI
    def CheckListCount(self, count, rlist):
        
        while(True):
            if(len(rlist) <= int(count)):
                break;
            else:
               rlist.pop()

        return rlist