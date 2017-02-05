from Helper.LogHelper import LOG
from Helper.XmlHelper import XML
from Product.TreeMaker.Model import TreeModel

#move to XML
def list_to_tree(keywordlist):
    Root = TreeModel.TreeNode('root', 'root', 'root')
    print("------------tree--------------")
    '''
    print(Root.keyword)
    print(Root.url)
    print(Root.parent)
    print(Root.children)
    '''

    #insert
    for i in keywordlist.keys():
        LOG.DEBUG(i)
        Root.Node_Insert(i,"")
    
    #print
    for i in keywordlist:
        print(Root.children[i].keyword) #print depth 1
