from Helper.LogHelper import LOG
from Helper.XmlHelper import XML
from Product.ListMaker.Model import ListModel

#move to XML
def XmlToList():
    jirim = XML.ReadXml()
    keywordlist = {} #rootlist dic
    #ggggg = jirim.find('RankParams').findall('Rank'):

    for child in jirim.find('RankParams').findall('Rank'): #create keywordlist
        keywordlist[child.find('Title').text] = []
                
    LOG.DEBUG("print keywordlist")
    print(keywordlist)

    for child_RelationParams in jirim.findall('RelationParams'):
        for child_Relation in child_RelationParams.findall('Relation'): #create relation
                    makeList(keywordlist, child_Relation.attrib["value"], makebasickeyword(child_Relation.find('Title').text, child_Relation.find('Link').text))

    LOG.DEBUG("print keywordlist[0] basic_keyword_list")
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


        
