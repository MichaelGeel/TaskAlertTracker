from model.tasks import Task, Stage
import datetime as dt
import unittest

mock_up_tasks = [
    {
        "name": "First Test",
        "type": "tester",
        "task_description": "This is the first task",
        "entry_date": dt.datetime.now(),
        "material_master": 123456,
        "sku_code": "1234567",
        "market": "industrial",
        "urgency": True,
        "completed": False,
        "stages": [
            {
                "name": "Project Scoping",
                "description": "This step is the scoping of the project",
                "duration": 4,
                "start_date": dt.datetime.now()
            },
            {
                "name": "Data Exploration",
                "description": "Exploring the data",
                "duration": 8
            }
        ]
    },
    {
        "name": "Second Item",
        "type": "diffs",
        "task_description": "This is the second task",
        "entry_date": dt.datetime.now(),
        "material_master": 123457,
        "sku_code": "1234567",
        "market": "mining",
        "urgency": False,
        "completed": False,
        "stages": [
            {
                "name": "Project Scoping",
                "description": "This step is the scoping of the project",
                "duration": 4,
                "start_date": dt.datetime.now()
            },
            {
                "name": "Data Exploration",
                "description": "Exploring the data",
                "duration": 8
            }
        ]
    }
]