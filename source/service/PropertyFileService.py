import configparser

# This service class encapsulates a property file.
class PropertyFileService:

    # This is a class constructor
    def __init__(self, propertyFileLocation):
        self._propertyFileLocation = propertyFileLocation

    # This method is called by the client class that wants to read a property.
    def read(self, propertySectionName, property):
        config = self.getPropertyConfiguration()
        databaseUserId = self._getProperty(config, property, propertySectionName)
        return databaseUserId

    def getPropertyConfiguration(self):
        config = configparser.ConfigParser()
        propertyFileLocation = self._getPropertyFileLocation()
        config.read(propertyFileLocation)
        return config

    def _getProperty(self, config, property, propertySectionName):
        databaseUserId = config.get(propertySectionName, property)
        return databaseUserId

    def _getPropertyFileLocation(self):
        propertyFileLocation = self._propertyFileLocation
        return propertyFileLocation
