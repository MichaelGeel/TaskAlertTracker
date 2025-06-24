from pymongo import MongoClient, database

client = MongoClient | None
process_tracker = None

def get_client() -> MongoClient:
    client = MongoClient()
    return client

def get_db():
    process_tracker = get_client().process_tracker_db
    return process_tracker

get_db()