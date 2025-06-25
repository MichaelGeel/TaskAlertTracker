import datetime as dt
from pydantic import BaseModel

class Stage(BaseModel):
    name: str
    description: str
    duration: int
    start_date: dt.datetime|None
    end_date: dt.datetime|None

class Task(BaseModel):
    name: str
    task_description: str
    entry_date: dt.datetime
    completed_date: dt.datetime|None
    material_master: str
    sku_code: str
    market: str
    urgency: bool
    completed: bool
    on_hold: bool
    hold_reason: str|None
    active_stage_index: int
    stages: list[Stage]
