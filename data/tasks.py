from .init import process_tracker
import datetime as dt
from model.tasks import Task, Stage
from bson.objectid import ObjectId


"""
Because MongoDB autocreates collections and databases, no explicit creation of the collection/database is necessary.
"""


def model_to_dict(task: Task) -> dict:
    return task.model_dump()

def entry_to_model(entry: dict) -> Task:
    return Task(
        str(entry._id),
        entry.name,
        entry.type,
        entry.task_description,
        entry.entry_date,
        entry.completed_date,
        int(entry.material_master),
        entry.sku_code,
        entry.market,
        entry.urgency,
        entry.completed,
        entry.on_hold,
        entry.hold_reason,
        entry.next_stage_index,
        [
        Stage(
            str(stage["_id"]),
            stage["name"], 
            stage["description"], 
            stage["duration"], 
            stage["start_date"],
            stage["end_date"]
            ) for stage in entry.stages
        ]
    )

# TODO: Validate whether actually need to worry about exposing the _id field to the front end or if okay and more a sensitive data concern.

def fetch_all(type: str) -> list[Task]:
    # TODO: Test
    # TODO: Error handling incase invalid type - if doesn't just return empty list
    raw_tasks = process_tracker.tasks.find({"type": type})
    return [entry_to_model(task) for task in raw_tasks]

def fetch_report(type: str, entry_date: dt.datetime) -> list[Task]:
    # TODO: Test
    # TODO: Error handling incase invalid type - If doesn't just return empty list
    raw_tasks = process_tracker.tasks.find({"type": type, "entry_date": {"$gte": entry_date}})
    return [entry_to_model(task) for task in raw_tasks]

def fetch_one(id: ObjectId) -> Task:
    # TODO: Error handling in case of invalid id value/type
    # TODO: Test
    return entry_to_model(process_tracker.tasks.find_one({"_id": id}))

def create(task: Task) -> Task:
    # TODO: Test
    task_id = process_tracker.tasks.insert_one(model_to_dict(task)).inserted_id
    # Call fetch_one as insert_one only returns the _id of the created entry.
    return fetch_one(task_id) 

def update(updates: dict) -> Task:
    pass

def delete(task: Task) -> bool:
    pass