import time
from Helper.LogHelper import LOG
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump

def GetCurrentTime():
    now = time.localtime()

    return "%04d_%02d_%02d_%02d_%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

# Convert RankList to XML and save xml format
def RanklistToXML(rList):
        
    if isinstance(rList, list) == False:
        LOG.DEBUG("rList is not list.");
        return False

    try:
        currentTime = GetCurrentTime()
        fileName = currentTime + "_Rank.xml"

        root = Element("Jirim")
    
        # rankparams
        rankParams = Element("RankParams")
        rankParams.attrib["date"] = currentTime
        rankParams.attrib["from"] = "naver"
        
        for node in rList:
            rank = Element("Rank")
            SubElement(rank, "Index").text = str(node.index)
            SubElement(rank, "Title").text = node.title
            SubElement(rank, "Link" ).text = node.link
            
            rankParams.append(rank);
        
        root.append(rankParams)
        
        # make xml format
        indent(root)
        # save xml
        ElementTree(root).write(fileName, encoding="utf-8", xml_declaration=True)

    except ValueError as e:
       LOG.FATAL("Fail to RankList XML : " + e);
       return False

    else:
       LOG.DEBUG("Success. RankList to XML") 
       return True      
        
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
