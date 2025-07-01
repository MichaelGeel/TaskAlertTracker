import datetime as dt
from pydantic import BaseModel

class Stage(BaseModel):
    id: str | None = None
    name: str
    description: str
    duration: int
    start_date: dt.datetime|None = None
    end_date: dt.datetime|None = None

class Task(BaseModel):
    id: str | None = None
    name: str
    type: str
    task_description: str
    entry_date: dt.datetime
    completed_date: dt.datetime|None = None
    material_master: str
    sku_code: str
    market: str
    urgency: bool
    completed: bool
    on_hold: bool = False
    hold_reason: str|None = None
    next_stage_index: int = 1
    stages: list[Stage]


# TODO: set up attribute constraints on certain fields using the Pydantic Field method based on requirements for the codes.
