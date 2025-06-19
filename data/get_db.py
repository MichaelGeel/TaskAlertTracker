from pymongo import MongoClient


def get_client() -> MongoClient:
    client = MongoClient()
    return client

def get_db(db_name: str):
    task_process_database = get_client().task_process_db
    match db_name:
        case "Task":
            db = task_process_database.task_doc
        case "Task_Process":
            db = task_process_database.task_process_doc
        case "Phase":
            db = task_process_database.phase_doc
        case "Stage":
            db = task_process_database.stage_doc
        case _:
            return Exception("The requested document does not exist")
    return db