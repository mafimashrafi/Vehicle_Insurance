"""
This file contains some constant variables
that repeat all over the code base for more than once.

Except for MongoDB connections.
We have them in environmental file.
"""
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DB_NAME")
COLLECTION = os.getenv("COLLECTION_NAME")
