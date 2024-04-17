import random

class config:
     
    def __init__(self):
        self.__dataPath__ = 'data.xlsx'
        self.__defaultLargeBackoff__ = 7
        self.__defaultMediumBackoff__ = 3
        self.__defaultSmallBackoff__ = 0.4
        self.__variableLargeBackoff__ = 2
        self.__variableMediumBackoff__ = 1
        self.__variableSmallBackoff__ = 0.2
        self.__sheetSaveName__ = "Western Monarch Count" #The Sheet Save Name
        self.__pathSaveName__ = "Western Monarch Counter.xlsx" #The Save Path Name
        self.__numberedRows__ = False #Whether or not the first column is numbered
        self.__incognito__ = True #Whether or not the first column is numbered
        self.__headless__ = True #Whether or not the first column is numbered
        self.__disableGPU__ = True #Whether or not the first column is numbered
    
    SITE_ID = 'SITE ID'

    def getDataPath(self):
        return self.__dataPath__
    
    def getLargeBackoff(self):
        return self.__defaultLargeBackoff__
    
    def getMediumBackoff(self):
        return self.__defaultMediumBackoff__
    
    def getSmallBackoff(self):
        return self.__defaultSmallBackoff__

    def getLargeVariableBackoff(self):
        return random.random()*self.__variableLargeBackoff__
    
    def getMediumVariableBackoff(self):
        return random.random()*self.__variableMediumBackoff__
    
    def getSmallVariableBackoff(self):
        return random.random()*self.__variableSmallBackoff__
    
    def getSheetName(self):
        return self.__sheetSaveName__
    
    def getSavePath(self):
        return self.__pathSaveName__
    
    def isIndexed(self):
        return self.__numberedRows__
    
    def isIncognito(self):
        return self.__incognito__
    
    def isHeadless(self):
        return self.__headless__
    
    def isDisableGPU(self):
        return self.__disableGPU__
    