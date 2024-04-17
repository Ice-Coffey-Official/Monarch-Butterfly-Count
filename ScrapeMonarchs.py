from selenium.webdriver.common.by import By
import pandas as pd
from util import util
from config import config

utility = util()
configuration = config()
IDs = utility.excelColToList(col = 'A')
driver = utility.openDriver()
siteUrl = "https://experience.arcgis.com/experience/f9c6ce4664e0470eb681a46a143477ed/"
sites = []

page = driver.get(siteUrl)
utility.variableSleep(base = configuration.getLargeBackoff(), var = configuration.getLargeVariableBackoff())

for i in IDs:
    cancelButtonList = driver.find_elements(by=By.CLASS_NAME, value="esri-search__clear-button.esri-widget--button")
    cancelButton = cancelButtonList[0] if len(cancelButtonList) > 0 else None
    cancelButton.click() if cancelButton else True
    searchButton = driver.find_element(by=By.CLASS_NAME, value="esri-search__submit-button.esri-widget--button")
    searchButton.click()
    utility.variableSleep(base = configuration.getSmallBackoff(), var = configuration.getSmallVariableBackoff())
    searchBar = driver.find_element(by=By.TAG_NAME, value="input")
    utility.variableSleep(base = configuration.getSmallBackoff(), var = configuration.getSmallVariableBackoff())
    searchBar.send_keys(str(i))
    searchButton.click()
    utility.variableSleep(base = configuration.getMediumBackoff(), var = configuration.getMediumVariableBackoff())
    site_info = driver.find_element(by=By.CLASS_NAME, value="esri-feature-content").find_elements(by=By.TAG_NAME, value="p")
    sites.append(utility.extractData(site_info))

jointData = utility.joinDataScrape(data=sites, path = configuration.getDataPath())

with pd.ExcelWriter(configuration.getSavePath()) as writer:
    jointData.to_excel(writer, sheet_name=configuration.getSheetName(), index=configuration.isIndexed())