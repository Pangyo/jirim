# Path
HomePath    = None
SystemPath  = None
LogFilePath = None
XmlFilePath = None
INIFilePath = None

# File
XmlFileName = None

# List, Dictionary
RankDataList = None
RelationList = None
RankDataDict = dict()
RelationDict = dict()

class Global(object):
    
    # Home
    @staticmethod
    def GetHomePath():
        global HomePath
        return HomePath

    @staticmethod
    def SetHomePath(strH):
        global HomePath
        HomePath = strH
    
    # System
    @staticmethod
    def GetSystemPath():
        global SystemPath
        return SystemPath

    @staticmethod
    def SetSystemPath(strS):
        global SystemPath
        SystemPath = strS
    
    # Log - path    
    @staticmethod
    def GetLogFilePath():
        global LogFilePath
        return LogFilePath

    @staticmethod
    def SetLogFilePath(strL):
        global LogFilePath
        LogFilePath = strL

    # Xml - path
    @staticmethod
    def GetXmlFilePath():
        global XmlFilePath
        return XmlFilePath

    @staticmethod
    def SetXmlFilePath(strX):
        global XmlFilePath
        XmlFilePath = strX

    # INI - path
    @staticmethod
    def GetINIFilePath():
        global INIFilePath
        return INIFilePath

    @staticmethod
    def SetINIFilePath(strI):
        global INIFilePath
        INIFilePath = strI
    
    # Xml - name    
    @staticmethod
    def GetXmlFileName():
        global XmlFileName
        return XmlFileName

    @staticmethod
    def SetXmlFileName(strX):
        global XmlFileName
        XmlFileName = strX


    # List, Dictionary
    @staticmethod
    def GetRankDataList():
        global RankDataList
        return RankDataList
    
    @staticmethod
    def GetRelationList():
        global RelationList
        return RelationList

    @staticmethod
    def GetRankDataDict():
        global RankDataDict
        return RankDataDict

    @staticmethod
    def GetRelationDict():
        global RelationDict
        return RelationDict

    @staticmethod
    def SetRankDataList(rankDataList):
        global RankDataList
        RankDataList = rankDataList

    @staticmethod
    def SetRelationList(relationList):
        global RelationList
        RelationList = relationList

    @staticmethod
    def SetRankDataDict(rankDataDict):
        global RankDataDict
        RankDataDict = rankDataDict

    @staticmethod
    def SetRelationDict(relationDict):
        global RelationDict
        RelationDict = relationDict

