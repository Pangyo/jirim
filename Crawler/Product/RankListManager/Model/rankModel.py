
class RankModel:
    
    def __init__(self):
        pass
    
    def setInit(self, index, title, link):
        self.index = index
        self.title = title
        self.link = link
    
    def setIndex(self, index, private = True):
        self.index = index
    
    def setTitle(self, title, private = True):
        self.title = title
        
    def setLink(self, link):
        self.link = link
        