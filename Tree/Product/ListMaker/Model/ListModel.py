
class basic_keyword:
    def __init__(self):
        pass
    
    def setInit(self, name, url):
        self.name = name
        self.url = url

    def setName(self, name):
        self.name = name

    def setUrl(self, url):
        self.url = url 

class keyword_relation:
    def __init__(self):
        pass

    def setInit(self, name):
        self.name = name
        self.basic_keyword_list = []

    def addList(self, basic_keyword):
        self.basic_keyword_list.append(basic_keyword)



