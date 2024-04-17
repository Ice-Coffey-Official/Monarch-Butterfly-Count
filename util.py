from typing import List
import pandas as pd
import math
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.remote.webelement import WebElement
from ButterflySite import butterflySite
import time
from random import random
from config import config

class util:

    def __init__(self):
        self.configuration = config()
    
    def __charToInt__(self, char : str):
        return ord(char.lower()) - 97

    def excelColToList(self, col = 'A'):
        path = self.configuration.getDataPath()
        df = pd.read_excel(path, usecols=col)
        return [int(site_id) for site_id in df[df.columns[self.__charToInt__(col)]] if not math.isnan(site_id)]
    
    def siteListToPandas(self, sites: list[butterflySite]):
        siteId = []
        longitude = []
        latitude = []
        region = []
        regionalCoordinator = []
        email = []
        boundaryPublished = []
        count = []
        for s in sites:
            siteId.append(s.getSiteId())
            longitude.append(s.getLongitude())
            latitude.append(s.getLatitude())
            region.append(s.getRegion())
            regionalCoordinator.append(s.getRegionalCoordinator())
            email.append(s.getEmail())
            boundaryPublished.append(s.getBoundaryPublished())
            count.append(s.getCounts())
        return pd.DataFrame(
            {
                self.configuration.SITE_ID : siteId,
                'Longitude' : longitude,
                'Latitude' : latitude,
                'Region' : region,
                'Regional Coordinator' : regionalCoordinator,
                'Regional Coordinator\'s Email' : email,
                'Boundary Published' : boundaryPublished,
                'Has Counts' : count
            }
        )


    def joinDataScrape(self, data : list[butterflySite], path = 'data.xlsx'):
        df1 = pd.read_excel(path)
        df1.dropna(subset=[self.configuration.SITE_ID], inplace=True)
        df1[self.configuration.SITE_ID] = df1[self.configuration.SITE_ID].astype(int)
        df2 = self.siteListToPandas(data)
        df2[self.configuration.SITE_ID] = df2[self.configuration.SITE_ID].astype(int)

        return pd.merge(df2, df1, on=self.configuration.SITE_ID, how='outer')
    
    def openDriver(self, incognito:bool = False, headless:bool= False, disableGPU:bool= False):
        edge_options = Options()
        edge_options.add_argument("ms:inPrivate") if self.configuration.isIncognito() else True
        edge_options.add_argument("headless") if self.configuration.isHeadless() else True
        edge_options.add_argument("disable-gpu") if self.configuration.isDisableGPU() else True
        return webdriver.Edge(options=edge_options)
    
    def extractData(self, info:List[WebElement]):
        sID = None
        lat = None
        long = None
        reg = None
        coord = None
        email = None
        bound = None
        count = None
        for attribute in info:
            if ("site id: " in attribute.text.lower()):
                sID = attribute.text.lower().partition("site id: ")[-1]
            elif ("latitude: " in attribute.text.lower()):
                lat = attribute.text.lower().partition("latitude: ")[-1]
            elif ("longitude: " in attribute.text.lower()):
                long = attribute.text.lower().partition("longitude: ")[-1]
            elif ("region: " in attribute.text.lower()):
                reg = attribute.text.lower().partition("region: ")[-1]
            elif ("regional coordinator(s): " in attribute.text.lower()):
                coordEmail = attribute.text.lower().partition("regional coordinator(s): ")[-1]
                coord, sep, email = coordEmail.partition(' (')
                email = email.strip(')')
            elif ("boundary published: " in attribute.text.lower()):
                bound = attribute.text.lower().strip("boundary published: ")
            elif ("this site does not have counts" in attribute.text.lower()):
                count = False
            else:
                count = True
        
        return butterflySite(
            siteId = sID,
            longitude = long,
            latitude = lat,
            region = reg,
            regionalCoordinator = coord,
            email = email,
            boundaryPublished = bound,
            counts = count
        )
    
    def variableSleep(self, base:float = 1, var:float = 1):
        time.sleep(base+var*random())