import pymongo
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

database_url = os.environ['DATABASE_URL']
database_name = os.environ['DATABASE_NAME']

client = pymongo.MongoClient(database_url)

database = client[database_name]
