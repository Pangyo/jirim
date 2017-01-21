'''
Created on 2016. 11. 13.

@author: yunjae
'''

import requests

from bs4 import BeautifulSoup

from Common.Language import Resources
from Common.CommonClass.BaseClass import BaseClass
from Product.RelationListManager.Model.relationModel import RelationtModel

class RelationService(BaseClass):

    def __init__(self):
        self.RelationList = []
    
    def GetTextHTMLPARSER(self, url):
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, Resources.CONST_HTML_PARSER)
        return soup
    
    
    def GetRelationList(self, item_url):
        
        soup = self.GetTextHTMLPARSER(item_url)
        
        # lst_relate None case, it is not exist relation list so, go to the next ranklist
        lst_relate = soup.find('dd', {'class':'lst_relate'})
        if lst_relate == None:
            return self.RelationList

        for li in lst_relate.findAll('li'):
            relationM = RelationtModel()
            li_Text = li.find('a')
            
            relationTitle = li_Text.string.strip()
            relationLink = li_Text['href']
            
            relationM.setTitle(relationTitle)
            relationM.setLink(relationLink)
            
            self.RelationList.append(relationM)
        
        return self.RelationList
    