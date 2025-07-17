from typing import Annotated, Any, Callable
from fastapi import FastAPI

import datetime as dt
from pydantic import BaseModel, ConfigDict, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from bson.objectid import ObjectId
# TODO: Finish off implementation for the ObjectId type in Pydantic



class Stage(BaseModel):
    id: ObjectId | None = None
    name: str
    description: str
    duration: int
    start_date: dt.datetime|None = None
    end_date: dt.datetime|None = None


class Task(BaseModel):
    id: ObjectId | None = None
    name: str
    type: str
    task_description: str
    entry_date: dt.datetime
    completed_date: dt.datetime|None = None
    material_master: int
    sku_code: str
    market: str
    urgency: bool
    completed: bool
    on_hold: bool = False
    hold_reason: str|None = None
    next_stage_index: int = 1
    stages: list[Stage]


# TODO: set up attribute constraints on certain fields using the Pydantic Field method based on requirements for the codes.
