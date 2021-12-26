import configparser

# This service class encapsulates a property file. Many instances of this
# service class can be created. In that case each instance may contain
# one property file.
class PropertyFileService:

    # This is the class constructor that is used for the property file.
    # Pass in the location of the property file to this constructor.
    def __init__(self, propertyFileLocation):
        self._propertyFileLocation = propertyFileLocation

    # This method is called by the client class that wants to read a property.
    # We see that this method does not start with an underscore. This is the
    # convention for public methods in Python classes.
    def read(self, propertySectionName, property):
        config = self._getPropertyConfiguration()  # Get config object from method below.
        databaseUserId = self._getProperty(config, propertySectionName, property)
        return databaseUserId

    # Private methods in classes starts by convention with an underscore in
    # Python. The first line in this method creates a configuration parser object.
    def _getPropertyConfiguration(self):
        config = configparser.ConfigParser()
        propertyFileLocation = self._getPropertyFileLocation() # Call method below.
        config.read(propertyFileLocation)
        return config

    # This private method returns the property file location that was
    # passed in in the constructor of this class.
    def _getPropertyFileLocation(self):
        propertyFileLocation = self._propertyFileLocation
        return propertyFileLocation

    # This private method returns the property from the property file
    # that was passed in to the constructor of this class. Properties
    # in Python property files are arranged by section.
    def _getProperty(self, config, propertySectionName, property):
        databaseUserId = config.get(propertySectionName, property)
        return databaseUserId
