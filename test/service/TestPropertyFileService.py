import unittest
from source.service.PropertyFileService import PropertyFileService

# This Unit Test class holds a suite of test cases that we can use to make sure that
# PropertyFileService class is working properly.
class TestPropertyFileService(unittest.TestCase):

    # This setup method also called a test fixture. It ensures that the tests in this test suite
    # always starts with the instance variable is always initialized with an instance of the
    # PropertyFileService class before it starts. The setUp method is run before each method in the
    # test suite is run.
    def setUp(self):
        self._propertyFileService = PropertyFileService("C:/training/properties/TestProperties.properties")

    def test_readDatabaseUserId(self):
        databaseUserId = self._propertyFileService.read("DATABASE_CONNECTION", "database.user.id")
        self.assertEqual("userid", databaseUserId, "Expected database user Id to be 'db_userid'")

    def test_readDatabasePassword(self):
        databaseUserId = self._propertyFileService.read("DATABASE_CONNECTION", "database.password")
        self.assertEqual("password", databaseUserId, "Expected database password to be 'password'")
