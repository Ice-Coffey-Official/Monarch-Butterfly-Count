class butterflySite:

    def __init__(self, siteId : int, longitude : float, latitude : float, region : str, regionalCoordinator : str, email : float, boundaryPublished : int, counts : bool):
        self.__siteId__ = siteId
        self.__longitude__ = longitude
        self.__latitude__ = latitude
        self.__region__ = region
        self.__regionalCoordinator__ = regionalCoordinator
        self.__email__ = email
        self.__boundaryPublished__ = boundaryPublished
        self.__counts__ = counts

    def __repr__(self):
        return str({
            "Site ID Number" : self.__siteId__,
            "Latitude" : self.__latitude__,
            "Longitude" : self.__longitude__,
            "Region" : self.__region__,
            "Regional Coordinator" : self.__regionalCoordinator__,
            "Regional Coordinator Email" : self.__email__,
            "Boundary Published" : self.__boundaryPublished__,
            "Counts" : self.__counts__
        })
    
    def __str__(self):
        return str({
            "Site ID Number" : self.__siteId__,
            "Latitude" : self.__latitude__,
            "Longitude" : self.__longitude__,
            "Region" : self.__region__,
            "Regional Coordinator" : self.__regionalCoordinator__,
            "Regional Coordinator Email" : self.__email__,
            "Boundary Published" : self.__boundaryPublished__,
            "Counts" : self.__counts__
        })
    
    def getSiteId(self):
        return self.__siteId__
    
    def getLongitude(self):
        return self.__longitude__
    
    def getLatitude(self):
        return self.__latitude__
    
    def getRegion(self):
        return self.__region__
    
    def getRegionalCoordinator(self):
        return self.__regionalCoordinator__
    
    def getEmail(self):
        return self.__email__
    
    def getBoundaryPublished(self):
        return self.__boundaryPublished__
    
    def getCounts(self):
        return self.__counts__
