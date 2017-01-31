

# Path
LOGFILEPATH = None
XMLFILEPATH = None

# File
XmlFileName = None

class Global(object):
    
    @staticmethod
    def GetXMLFileName():
        global XmlFileName
        return XmlFileName
    
    @staticmethod
    def SetXMLFileName(strXml):
        global XmlFileName
        XmlFileName = strXml
