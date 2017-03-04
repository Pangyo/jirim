import time
import os

from Helper import LOG
from Model import RankModel
from Model import RelationModel

from Helper.Global import Global

from xml.etree.ElementTree import ElementTree, Element, SubElement, dump, parse

# Convert XML to RankList and return list
def XMLToRanklist():

    _rankList = []
   
    fileName = Global.GetXmlFileName()
    if fileName == None:
        return None

    if os.path.exists(fileName) == False:
        return None
    
    try:
        tree = parse(fileName)
        root = tree.getroot()
   
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


# Convert XML to Relation List and return list
def XMLToRelationlist(): 
    _relationList = []
   
    fileName = Global.GetXmlFileName()
    if fileName == None:
        return None

    if os.path.exists(fileName) == False:
        return None

    try:
        tree = parse(fileName)
        root = tree.getroot()
   
        for relationParams in root.findall("RelationParams"):

            for relation in relationParams.findall("Relation"):
                tempKey   = relation.attrib["key"]
                tempValue = relation.attrib["value"]
                tempTitle = relation.findtext("Title")
                tempLink  = relation.findtext("Link")
                
                _tempModel = RelationModel.Relation()
                _tempModel.setKey(tempKey)
                _tempModel.setValue(tempValue)
                _tempModel.setTitle(tempTitle)
                _tempModel.setLink(tempLink)    

                _relationList.append(_tempModel)

    except ValueError as e:
       LOG.FATAL("Fail to Relation List parsing XML : " + e);

    else:
       LOG.DEBUG("Success. XML to Relation List") 
    
    return _relationList
    


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
