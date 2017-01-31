import time
from Helper.LogHelper import LOG
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump, parse #Elementtree

def ReadXml():
    tree = parse('Rank_list.xml')
    LOG.DEBUG("Xml load ok")
    jirim = tree.getroot()
    return jirim
    #from_tag = jirim.getchildren()
    #LOG.DEBUG(jirim.find('RankParams').find('Rank').find('Index').text)
    '''
    for child in jirim.find('RankParams').findall('Rank'):
        print(child.find('Index').text) 
        print(child.find('Title').text)
        print(child.find('Link').text)
     ''' 
    #from_index = jirim.find("Rank")
    #LOG.DEBUG(from_index)

    '''
    child = jirim.getiterator()
    LOG.DEBUG("child: " + str(child))
    #LOG.DEBUG("child.items():" + str(child.items()))
    '''

def GetCurrentTime():
    now = time.localtime()

    return "%04d_%02d_%02d_%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour)
    #return "%04d_%02d_%02d_%02d_%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

