from pymongo import MongoClient, database
from dotenv import load_dotenv
import os


load_dotenv()


client: MongoClient | None = None
process_tracker: database.Database | None = None


"""
Using local MongoDB installation, so minimal path handling is implemented here. 
In a mature dev environment, would move the database into an external deployment and include path handling and auth here.
"""
def get_client() -> MongoClient:
    global client
    client = MongoClient()
    return client


def get_db():
    global process_tracker
    db_name = os.getenv("TASK_DB_NAME")
    process_tracker = get_client()[db_name]
    return process_tracker


get_db()