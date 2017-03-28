import os
from configparser import SafeConfigParser

from Common.Global import Global

Crawler_Home = os.getcwd()
Crawler_SYS = Crawler_Home + "\System"

Crawler_LOG = Crawler_SYS + "\LOG"
Crawler_XML = Crawler_SYS + "\XML"
Crawler_INI = Crawler_SYS + "\INI"

Crawler_LOG_Name = Crawler_LOG + "\Crawler.log"
Crawler_XML_Name = Crawler_XML + "\Crawler.xml"
Crawler_INI_Name = Crawler_INI + "\Crawler.ini"

def Initialize():

    try:
        if(os.path.exists(Crawler_SYS)  == False):    os.mkdir(Crawler_SYS)
        if(os.path.exists(Crawler_LOG)  == False):    os.mkdir(Crawler_LOG)
        if(os.path.exists(Crawler_XML)  == False):    os.mkdir(Crawler_XML)
        if(os.path.exists(Crawler_INI)  == False):    os.mkdir(Crawler_INI)

    except:
        return False;
    else:
        return True;

def ReadINI():

    if(os.path.exists(Crawler_INI_Name) == False):
        pass

    try:
        parser = SafeConfigParser()
        parser.read(Crawler_INI_Name)
        
        if parser.has_option("Path",    "HomePath"     ):   Global.SetHomePath      (parser.get("Path",     "HomePath"      ))
        if parser.has_option("Path",    "SystemPath"   ):   Global.SetSystemPath    (parser.get("Path",     "SystemPath"    ))
        if parser.has_option("Path",    "LogFilePath"  ):   Global.SetLogFilePath   (parser.get("Path",     "LogFilePath"   ))
        if parser.has_option("Path",    "XmlFilePath"  ):   Global.SetXmlFilePath   (parser.get("Path",     "XmlFilePath"   ))
        if parser.has_option("Path",    "INIFilePath"  ):   Global.SetINIFilePath   (parser.get("Path",     "INIFilePath"   ))

        if parser.has_option("File",    "XmlFileName"  ):   Global.SetXmlFileName   (parser.get("File",     "XmlFileName"   ))

        if parser.has_option("Data",    "RankListCount"):   Global.SetRankListCount (parser.get("Data",     "RankListCount" ))
        if parser.has_option("Data",    "RelationCount"):   Global.SetRelationCount (parser.get("Data",     "RelationCount" ))
        if parser.has_option("Data",    "RelationDepth"):   Global.SetRelationDepth (parser.get("Data",     "RelationDepth" ))

        if parser.has_option("Option",  "ServerIP"     ):   Global.SetServerIP      (parser.get("Option",   "ServerIP"      ))
        if parser.has_option("Option",  "CycleTime"    ):   Global.SetCycleTime     (parser.get("Option",   "CycleTime"     ))

    except:
        return False
    else:
        return True

def WriteINI():

    try:
        parser = SafeConfigParser()
        parser.read(Crawler_INI_Name)

        if parser.has_section("Path")   == False:   parser.add_section("Path")
        if parser.has_section("File")   == False:   parser.add_section("File")
        if parser.has_section("Data")   == False:   parser.add_section("Data")
        if parser.has_section("Option") == False:   parser.add_section("Option")
   
        if None == Global.GetHomePath()         :       parser.set("Path", "HomePath",      Crawler_Home)
        if None == Global.GetSystemPath()       :       parser.set("Path", "SystemPath",    Crawler_SYS)
        if None == Global.GetLogFilePath()      :       parser.set("Path", "LogFilePath",   Crawler_LOG)
        if None == Global.GetXmlFilePath()      :       parser.set("Path", "XmlFilePath",   Crawler_XML)
        if None == Global.GetINIFilePath()      :       parser.set("Path", "INIFilePath",   Crawler_INI)
                          
        if None == Global.GetXmlFileName()      :       parser.set("File", "XmlFileName",   Crawler_XML_Name)
                          
        if None == Global.GetRankListCount()    :       parser.set("Data", "RankListCount", "10")
        if None == Global.GetRelationCount()    :       parser.set("Data", "RelationCount", "10")
        if None == Global.GetRelationDepth()    :       parser.set("Data", "RelationDepth", "1")

        if None == Global.GetServerIP()         :       parser.set("Option", "ServerIP", "None") 
        if None == Global.GetCycleTime()        :       parser.set("Option", "CycleTime", "30")

        with open(Crawler_INI_Name, 'w') as configfile:
            parser.write(configfile)

        Global.SetHomePath      (parser.get("Path"      ,   "HomePath"      ))
        Global.SetSystemPath    (parser.get("Path"      ,   "SystemPath"    ))
        Global.SetLogFilePath   (parser.get("Path"      ,   "LogFilePath"   ))
        Global.SetXmlFilePath   (parser.get("Path"      ,   "XmlFilePath"   ))
        Global.SetINIFilePath   (parser.get("Path"      ,   "INIFilePath"   ))
        
        Global.SetXmlFileName   (parser.get("File"      ,   "XmlFileName"   ))
        
        Global.SetRankListCount (parser.get("Data"      ,   "RankListCount" ))
        Global.SetRelationCount (parser.get("Data"      ,   "RelationCount" ))
        Global.SetRelationDepth (parser.get("Data"      ,   "RelationDepth" ))

        Global.SetServerIP      (parser.get("Option"    ,   "ServerIP"      ))
        Global.SetCycleTime     (parser.get("Option"    ,   "CycleTime"     ))

    except:
        return False
    else:
        return True