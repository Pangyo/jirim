import os
from configparser import SafeConfigParser

from Helper.Global import Global

CrawlerAPI_Home = os.getcwd()
CrawlerAPI_SYS = CrawlerAPI_Home + "\System"

CrawlerAPI_LOG = CrawlerAPI_SYS + "\LOG"
CrawlerAPI_XML = CrawlerAPI_SYS + "\XML"
CrawlerAPI_INI = CrawlerAPI_SYS + "\INI"

CrawlerAPI_LOG_Name = CrawlerAPI_LOG + "\CrawlerAPI.log"
CrawlerAPI_XML_Name = CrawlerAPI_XML + "\CrawlerAPI.xml"
CrawlerAPI_INI_Name = CrawlerAPI_INI + "\CrawlerAPI.ini"

def Initialize():

    try:
        if(os.path.exists(CrawlerAPI_SYS)  == False):    os.mkdir(CrawlerAPI_SYS)
        if(os.path.exists(CrawlerAPI_LOG)  == False):    os.mkdir(CrawlerAPI_LOG)
        if(os.path.exists(CrawlerAPI_XML)  == False):    os.mkdir(CrawlerAPI_XML)
        if(os.path.exists(CrawlerAPI_INI)  == False):    os.mkdir(CrawlerAPI_INI)

    except:
        return False;
    else:
        return True;

def ReadINI():

    if(os.path.exists(CrawlerAPI_INI_Name) == False):
        pass

    try:
        parser = SafeConfigParser()
        parser.read(CrawlerAPI_INI_Name)
        
        if parser.has_option("Path", "HomePath"     ):  Global.SetHomePath      (parser.get("Path", "HomePath"     ))
        if parser.has_option("Path", "SystemPath"   ):  Global.SetSystemPath    (parser.get("Path", "SystemPath"   ))
        if parser.has_option("Path", "LogFilePath"  ):  Global.SetLogFilePath   (parser.get("Path", "LogFilePath"  ))
        if parser.has_option("Path", "XmlFilePath"  ):  Global.SetXmlFilePath   (parser.get("Path", "XmlFilePath"  ))
        if parser.has_option("Path", "INIFilePath"  ):  Global.SetINIFilePath   (parser.get("Path", "INIFilePath"  ))

        if parser.has_option("File", "XmlFileName"  ):  Global.SetXmlFileName   (parser.get("File", "XmlFileName"  ))

    except:
        return False
    else:
        return True

def WriteINI():

    try:
        parser = SafeConfigParser()
        parser.read(CrawlerAPI_INI_Name)

        if parser.has_section("Path") == False: parser.add_section("Path")
        if parser.has_section("File") == False: parser.add_section("File")
        if parser.has_section("Data") == False: parser.add_section("Data")
   
        if None == Global.GetHomePath()       :    parser.set("Path", "HomePath",      CrawlerAPI_Home)
        if None == Global.GetSystemPath()     :    parser.set("Path", "SystemPath",    CrawlerAPI_SYS)
        if None == Global.GetLogFilePath()    :    parser.set("Path", "LogFilePath",   CrawlerAPI_LOG)
        if None == Global.GetXmlFilePath()    :    parser.set("Path", "XmlFilePath",   CrawlerAPI_XML)
        if None == Global.GetINIFilePath()    :    parser.set("Path", "INIFilePath",   CrawlerAPI_INI)
                          
        if None == Global.GetXmlFileName()    :    parser.set("File", "XmlFileName",   CrawlerAPI_XML_Name)
        
        with open(CrawlerAPI_INI_Name, 'w') as configfile:
            parser.write(configfile)

        Global.SetHomePath      (parser.get("Path", "HomePath"     ))
        Global.SetSystemPath    (parser.get("Path", "SystemPath"   ))
        Global.SetLogFilePath   (parser.get("Path", "LogFilePath"  ))
        Global.SetXmlFilePath   (parser.get("Path", "XmlFilePath"  ))
        Global.SetINIFilePath   (parser.get("Path", "INIFilePath"  ))
        
        Global.SetXmlFileName   (parser.get("File", "XmlFileName"  ))
        
    except:
        return False
    else:
        return True