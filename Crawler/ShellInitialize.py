from Helper.LogHelper import LOG
from Helper.InIHelper import INI

from Common.CommonClass.BaseClass import BaseClass

class ShellInitialize(BaseClass):

    def __init__(self):
        pass

    def Pre_Initialize(self):

        if INI.Initialize() == False:
            return False
        
        if INI.ReadINI() == False:  
            return False

        if INI.WriteINI() == False:
            return False

        if LOG.Initialize() == False:
            return False

        LOG.DEBUG("Pre-initialize.")

        return True
