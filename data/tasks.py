from .init import process_tracker
import datetime as dt
from model.tasks import Task, Stage


"""
Because MongoDB autocreates collections and databases, no explicit creation of the collection/database is necessary.
"""


def model_to_dict(task: Task) -> dict:
    return task.model_dump()

def entry_to_model(entry: dict) -> Task:
    return Task(
        entry.id,
        entry.name,
        entry.type,
        entry.task_description,
        entry.entry_date,
        entry.completed_date,
        entry.material_master,
        entry.sku_code,
        entry.market,
        entry.urgency,
        entry.completed,
        entry.on_hold,
        entry.hold_reason,
        entry.next_stage_index,
        [
        Stage(
            stage["id"],
            stage["name"], 
            stage["description"], 
            stage["duration"], 
            stage["start_date"],
            stage["end_date"]
            ) for stage in entry.stages
        ]
    )

def fetch_all(type: str) -> list[Task]:
    # TODO: Include type filter into the find query to specify the type of task.
    # TODO: Test
    return process_tracker.tasks.find()

def fetch_report(type: str, entry_date: dt.datetime) -> list[Task]:
    pass

def fetch_one(id: str) -> Task:
    pass

# TODO: Test, once fetch_one implemented.
def create(task: Task) -> Task:
    task_id = process_tracker.tasks.insert_one(model_to_dict(task)).inserted_id
    return fetch_one(task_id)


def update(task: Task) -> Task:
    pass

def delete(task: Task) -> bool:
    pass