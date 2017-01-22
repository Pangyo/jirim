
class Relation:
    
    def __init__(self):
        pass
    
    def setInit(self, title, link, key, value):    
        self.link = link
        self.title = title
        self.key = key
        self.value = value

    def setTitle(self, title):
        self.title = title
    
    def setLink(self, link):
        self.link = link

    def setKey(self, key):
        self.key = key
    
    def setValue(self, value):
        self.value = value