
class TreeNode:
    def __init__(self, keyword, url, parent):
        self.keyword = keyword
        self.url = url
        self.children = {} #dic 
        self.parent = parent

    def Node_Insert(self, keyword, url):
        self.children[keyword] = TreeNode(keyword, url, self.keyword) #is it ok?

