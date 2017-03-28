
import sys
import time
import click
import threading

from Common.Global import Global
from Common.CommonClass.BaseClass import BaseClass

from ShellInitialize import ShellInitialize
from ShellProcess import ShellProcess

class ShellMain(BaseClass):
    
    def __init__(self):
        self._shellInitialize = ShellInitialize()  
        self._shellProcess = ShellProcess()      

        
    def Initialize(self):
        result = self._shellInitialize.Pre_Initialize()
        if result == False:
            return False

        return True

    def Processing(self):

        resultRankList = self._shellProcess.GetRankList("http://www.naver.com")
        if resultRankList == None:
            return False

        #result = self._shellProcess.SendRankList(resultRankList)
        #if result == False:
        #    return False          
  
        resultRelation = self._shellProcess.GetRelation(resultRankList)
        if resultRelation == False:
            return False

        #result = self._shellProcess.SendRelationList(resultRelation)
        #if result == False:
        #    return False
        
        #result = self._shellProcess.CopyXML()
        #if result == False:
        #    return False

		
        return True
        
class CProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__pause = False
        self.__end = False
        
    def SetShellMain(self, shellMain):
        self.shellMain = shellMain
            
    def pStop(self):
        self.__pause = True
         
    def pContinue(self):
        self.__pause = False
         
    def pEnd(self):
        self.__end = True

    def run(self):
        while True:

            # Pause            
            while self.__pause:
                time.sleep(1)
                 
            # Processing
            self.shellMain.Processing()
            self.LoadingPrint(Global.GetCycleTime())            

            # End
            if self.__end:
                break

    def LoadingPrint(self, min):
        for i in Global.progressbar(range(int(min) * 60), "Processing: ", 40):
            time.sleep(1)

if __name__ == '__main__':

    lock = threading.Lock()
    
    strInput = None
    strCheck = True

    sm = ShellMain()
    if sm.Initialize() == False:
        sys.exit()

    crawlerP = CProcess()
    crawlerP.SetShellMain(sm)

    crawlerP.start() 
 
    while(True):
        
        if strInput == "start" and strCheck == False:
            strCheck = True

            crawlerP.pContinue() 
            with lock:
                time.sleep(1)   
                
        elif strInput == "stop" and strCheck == True:
            strCheck = False

            crawlerP.pStop()
            with lock:
                time.sleep(1)
        elif strInput == "exit":
            crawlerP.pEnd()
            sys.exit()
        else:
            strInput = input()
