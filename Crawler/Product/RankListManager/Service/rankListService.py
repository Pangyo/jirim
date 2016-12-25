import requests

from bs4 import BeautifulSoup

from Common.Language import Resources
from Common.CommonClass.BaseClass import BaseClass

from Product.RankListManager.Model.rankListModel import RankListModel

class RankListService(BaseClass):

    def __init__(self):
        self.ListRanks = []

    def MakeRankModel(self, index, title, link):
        rankModel = RankListModel()
        
        rankModel.setIndex(index)
        rankModel.setTitle(title)        
        rankModel.setLink(link)
        
        return rankModel

    def GetTextHTMLPARSER(self, url):
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, Resources.CONST_HTML_PARSER)
        return soup
    
    def GetClassLink(self, dt):
        link =dt.find('a')['href']
        return str(link)
        
    def GetClassTitle(self, dt):
        title = dt.find('a')
        return title.string.strip()
    
    def GetClassWriting(self, dd):
        person_writing = dd.find('span' , {'class' : 'writing'})
        return person_writing.string
    
    def GetClassDate(self, dd):
        person_time = dd.find('span' , {'class' : 'date'})
        return person_time.string
    
    def GetRealTimeRankList(self, item_url):
        index = 1
        
        soup = self.GetTextHTMLPARSER(item_url)
        
        for li in soup.find('div', {'class':'rankup'}).findAll('li'):
            
            rankModel = RankListModel()
        
            li_Text = li.find('a')
            
            rankLink = li_Text['href'] 
            liTitle = li_Text["title"]
            rankTitle = str(liTitle)
            
            rankModel.setIndex(index)
            rankModel.setTitle(rankTitle)            
            rankModel.setLink(rankLink)
            
            self.ListRanks.append(rankModel)
            
            index = index + 1
            
        return self.ListRanks
        