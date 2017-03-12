from jirim.Tree.Helper.LogHelper import LOG
from jirim.Tree.Helper.XmlHelper import XML
from jirim.Tree.Product.ListMaker.Model import ListModel
from jirim.mongo.utils.mongoDao import MongoDao
from jirim.config.mongo import mongoConfig
import datetime

#move to XML
def XmlToList():
    jirim = XML.ReadXml()
    keywordlist = {} #rootlist dic
    #ggggg = jirim.find('RankParams').findall('Rank'):

    mongoDao = MongoDao()
    mongoDao.connect(mongoConfig.DATABASE_NAME)

    ranking_collection = mongoDao.getCollection(mongoConfig.RANKING_COLLECTION)
    for child in jirim.find('RankParams').findall('Rank'): #create keywordlist
        keyword = {}
        keyword['keyword'] = child.find('Title').text
        keyword['collect_time'] = str(datetime.datetime.now().time())
        LOG.DEBUG(datetime.datetime.now().time())
        keyword['rank'] = child.find('Index').text
        keyword['link'] = child.find('Link').text
        ranking_collection.insert_one(keyword)
        LOG.DEBUG(keyword)
        keywordlist[child.find('Title').text] = []
                
    LOG.DEBUG("print keywordlist")
    print(keywordlist)

    relation_collection = mongoDao.getCollection(mongoConfig.RELATION_COLLECTION)
    for child_RelationParams in jirim.findall('RelationParams'):
        for child_Relation in child_RelationParams.findall('Relation'): #create relation
                    relationKeyword = {}
                    relationKeyword['keyword'] = child_Relation.find('Title').text
                    relationKeyword['relation_keyword'] = child_Relation.attrib["value"]
                    relationKeyword['link'] = child_Relation.find('Link').text
                    relationKeyword['collect_time'] = str(datetime.datetime.now().time())
                    relation_collection.insert_one(relationKeyword)
                    makeList(keywordlist, child_Relation.attrib["value"], makebasickeyword(child_Relation.find('Title').text, child_Relation.find('Link').text))

    #LOG.DEBUG("print keywordlist[0] basic_keyword_list")
    for i in keywordlist:#[0].basic_keyword_list:
        print("======================================")
        print(i)
        num = 0
        '''
        for j in keywordlist[i]:
            num = num + 1 
            print(" " + str(num) + " " + str(j.name))
            '''
        print("======================================")
    return keywordlist

def makeList(keywordlist_index, key, basic_keyword):
    keywordlist_index[key].append(basic_keyword)


def makebasickeyword(name, url):
    basic_keyword1 = ListModel.basic_keyword()
    basic_keyword1.setInit(name, url)
    return basic_keyword1


        
