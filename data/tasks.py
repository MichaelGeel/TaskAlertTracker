from .init import process_tracker
from model.tasks import Task, Stage


def model_to_dict(task: Task) -> dict:
    return task.model_dump()

def entry_to_model(entry: dict) -> Task:
    return Task(
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
            stage["name"], 
            stage["description"], 
            stage["duration"], 
            stage["start_date"],
            stage["end_date"]
            ) for stage in entry.stages
        ]
    )


"""
Because MongoDB autocreates collections and databases, no explicit creation of the collection/database is necessary.
"""