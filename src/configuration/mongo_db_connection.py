import os
import sys
import pymongo
import certifi
from pymongo import MongoClient

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URI

ca = certifi.where()

class MongoDBClient:
    """
    MongoDB client class.
    MongoDB client is responsible for connecting to MongoDB server.
    """
    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        MongoDB client constructor.
        :param database_name: name of the MongoDB database
        :param MongoDB_URI: MongoDB uri to connect to MongoDB server
        """
        try:
            if MongoDBClient.client is None:
                if MONGODB_URI is None:
                    raise Exception(f"MongoDB URI is {MONGODB_URI} is not set")
                MongoDBClient.client = pymongo.MongoClient(MONGODB_URI)

            self.client = MongoClient
            self.database_name = database_name
            self.database = self.client[database_name]
            logging.info(f"MongoDB client initialized successfully")

        except Exception as e:
            raise MyException(e, sys)
