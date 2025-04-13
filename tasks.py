import datetime as dt
from enum import Enum


"""
Redact Phase names as IP when finished.
"""
class Phase(Enum):
    WB_CREATION = 1
    WB_COMPLETION = 2
    ITEM_CREATION = 3
    ARTWORK_RELEASE = 4
    PIR_QIR = 5
    COST_ROLLUP = 6
    SPECIFICATION = 7
    UNBLOCKED = 8


"""
Redact Phase names as IP when finished.
"""
class Task():
    def __init__(
            self, 
            entry_date: dt.datetime,
            material_master: int,
            sku_code: int,
            description: str,
            market: str,
            urgent: bool = False
            ):
        self._entry_date = entry_date
        self._material_master = material_master
        self._sku_code = sku_code
        self._description = description
        self._market = market
        self._urgent = urgent
        self._phase = Phase(1)
        self._stages = {}
        self._create_stages()
        self._completed = False

    def _create_stages(self):
        data_setter = {
            "name": "",
            "days": 0,
            "date_init": self._entry_date,
            "init": True
            }
        if self._urgent:
            data_setter["urgent"] = 2
        else:
            data_setter["urgent"] = 1
        for val in Phase:
            print(val)
        #     match val:
        #         case Phase.WB_CREATION:
        #             data_setter["name"] = "WorkBook Creation"
        #             data_setter["days"] = int(7//data_setter["urgent"])
        #             break
        #         case Phase.WB_COMPLETION:
        #             data_setter["name"] = "WorkBook Completion"
        #             data_setter["days"] = int(7//data_setter["urgent"])
        #             break
        #         case Phase.ITEM_CREATION:
        #             data_setter["name"] = "SysItem Creation"
        #             data_setter["days"] = int(7//data_setter["urgent"])
        #             break
        #         case Phase.ARTWORK_RELEASE:
        #             data_setter["name"] = "Artwork Release"
        #             data_setter["days"] = int(-2//data_setter["urgent"])
        #             data_setter["init"] = False
        #             break
        #         case Phase(5):
        #             data_setter["name"] = "PIR & QIR"
        #             data_setter["days"] = int(3//data_setter["urgent"])
        #             break
        #         case Phase(6):
        #             data_setter["name"] = "Cost Roll-Up"
        #             data_setter["days"] = int(2//data_setter["urgent"])
        #             break
        #         case Phase(7):
        #             data_setter["name"] = "Specification Received"
        #             data_setter["days"] = int(14//data_setter["urgent"])
        #             break
        #         case Phase(8):
        #             data_setter["name"] = "SysUnblock"
        #             data_setter["days"] = int(2//data_setter["urgent"])
        #             break
        #     self._stages[val] = Stage(data_setter["name"], data_setter["days"], data_setter["date_init"])
        #     if data_setter["days"] > 0 & data_setter["init"]:
        #         data_setter["date_init"] += dt.timedelta(days=data_setter["days"])
        #         self._stages[val]._set_active()
        # print(self._stages)


# TODO: Define a dunder get for the Task that creates a JSON object of the task (uses the dunder get of the stages) for storage.
# TODO: Create a post Artwork Release phase init that initializes the rest of the stages.
# TODO: Return date set into the active call to get around not being able to set dates from Artwork Release beyond.
# TODO: Test that the match case actually works.

class Stage():
    def __init__(
            self,
            name: str,
            duration: int,
            start_date: dt.datetime,
            ):
        self._name = name
        self._duration = duration
        self._active = False
        self._completed = False
        self._start_date = start_date
        self._end_date = start_date + dt.timedelta(days=self._duration)


    def _set_active(self):
        self._active = True
        

    def _set_completed(self):
        self._active = False
        self._completed = True


# TODO: Define a __get__ (check correct dunder function) that returns the stats of the Stage as a dict for storage.