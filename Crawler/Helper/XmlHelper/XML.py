import time

from Helper.LogHelper import LOG
from Common.Global import Global
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump, parse
from Product.RankListManager.Service.rankListService import RankListService

# Convert RelationList to XML and Save Xml format
def RelationListToXML(rList, rKey, rVal):

    if isinstance(rList, list) == False:
        LOG.DEBUG("rList is not list.");
        return False
        
    try:
        if Global.GetXmlFilePath() == None:
            return False

        fileName = Global.GetXmlFilePath()

        tree = parse(fileName)
        if tree == None:
            return False

        root = tree.getroot()

        # relationparams
        relationParams = Element("RelationParams");
        
        for node in rList:
            relation = Element("Relation")
            relation.attrib["key"] = str(rKey)
            relation.attrib["value"] = str(rVal)
            
            SubElement(relation, "Title").text = str(node.title)
            SubElement(relation, "Link").text = str(node.link)

            # relation param append
            relationParams.append(relation)

        root.append(relationParams)

        # make xml format
        indent(root)
        # save xml
        ElementTree(root).write(fileName, encoding="utf-8", xml_declaration=True)

    except ValueError as e:
       LOG.FATAL("Fail to RelationList XML : " + e);
       return False

    else:
       LOG.DEBUG("Success. RelationList to XML. Key = " + str(rKey) + ", Value = " + str(rVal)) 
       return True 


# Convert RankList to XML and save xml format
def RanklistToXML(rList):
        
    if isinstance(rList, list) == False:
        LOG.DEBUG("rList is not list.");
        return False

    try:
        path = Global.GetXmlFilePath() + "\\"
        currentTime = GetCurrentTime()
        fileName =  path + currentTime + "_Rank.xml"

        root = Element("Jirim")
    
        # rankparams
        rankParams = Element("RankParams")
        rankParams.attrib["date"] = currentTime
        rankParams.attrib["from"] = "naver"
        
        for node in rList:
            rank = Element("Rank")
            SubElement(rank, "Index").text = str(node.index)
            SubElement(rank, "Title").text = str(node.title)
            SubElement(rank, "Link" ).text = str(node.link)
            
            LOG.DEBUG("RankList title = " + str(node.title)) 
            rankParams.append(rank);
        
        root.append(rankParams)
        
        # make xml format
        indent(root)
        # save xml
        ElementTree(root).write(fileName, encoding="utf-8", xml_declaration=True)
        # save xml name
        Global.SetXmlFilePath(fileName)
        
    except ValueError as e:
       LOG.FATAL("Fail to RankList XML : " + e);
       return False

    else:
       LOG.DEBUG("Success. RankList to XML") 
       return True      
        
# Convert XML to RankList and return list
def XMLToRanklist():

    _rankList = []
    _rankListService = RankListService()
   
    fileName = Global.GetXMLFileName()
    #fileName = "2016_12_25_11_Rank.xml"
    if fileName == None:
        return 
    
    try:
        tree = parse(fileName)
        root = tree.getroot()
        #rootIter = tree.getiterator()
   
        for rankParams in root.findall("RankParams"):
            for rank in rankParams.findall("Rank"):
                tempIndex = rank.findtext("Index")
                tempTitle = rank.findtext("Title")
                tempLink  = rank.findtext("Link")
        
                tempRankModel = _rankListService.MakeRankModel(tempIndex, tempTitle, tempLink)
                _rankList.append(tempRankModel)

    except ValueError as e:
       LOG.FATAL("Fail to RankList parsing XML : " + e);

    else:
       LOG.DEBUG("Success. XML to RankList") 
    
    return _rankList

# print in debug - xml format
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def GetCurrentTime():
    now = time.localtime()

    return "%04d_%02d_%02d_%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour)
    #return "%04d_%02d_%02d_%02d_%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

