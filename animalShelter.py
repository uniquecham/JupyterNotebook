from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Nicole1976'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 11998
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@localhost:11998' % ('aacuser', 'Nicole1976')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def create(self, data):
        # Checks to see if the data is null or empty and returns false in either case
        if data is not None:
            if data:
                self.database.animals.insert_one(data)                     
                return True
        else:
            return False

    def read(self, search):
        # Checks to see if the data is null or empty and returns exception in either case
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception
                                  
