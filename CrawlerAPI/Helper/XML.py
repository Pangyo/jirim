import time
from Helper import LOG
from Model import RankModel

from xml.etree.ElementTree import ElementTree, Element, SubElement, dump, parse

# Convert XML to RankList and return list
def XMLToRanklist():

    _rankList = []
   
    fileName = None
    #fileName = "2017_01_08_19_Rank.xml"
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
                
                _tempModel = RankModel.Rank()
                _tempModel.setIndex(tempIndex)
                _tempModel.setTitle(tempTitle)
                _tempModel.setLink(tempLink)    
            
                _rankList.append(_tempModel)

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
