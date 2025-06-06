import datetime as dt
from enum import Enum



# class Task():
#     def __init__(
#             self, 
#             entry_date: dt.datetime,
#             material_master: int,
#             sku_code: int,
#             description: str,
#             market: str,
#             urgent: bool = False
#             ):
#         self._entry_date = entry_date
#         self._material_master = material_master
#         self._sku_code = sku_code
#         self._description = description
#         self._market = market
#         self._urgent = urgent
#         self._stages = {}
#         self._create_stages()
#         self._completed = False

#     def _create_stages(self):
#         pass
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
        #     self._stages[val] = Stage(data_setter["name"], data_setter["days"])
        #     if data_setter["days"] > 0 & data_setter["init"]:
        #         data_setter["date_init"] += dt.timedelta(days=data_setter["days"])
        #         self._stages[val]._set_active()
        # print(self._stages)


class Stage():
    def __init__(
            self,
            name: str,
            duration: int,
            ):
        self._name = name
        self._duration = duration
        self._active = False
        self._completed = False


    def _set_active(self, start_date: dt.datetime,):
        self._active = True
        self._start_date = start_date
        self._end_date = start_date + dt.timedelta(days=self._duration)
        

    def _set_completed(self):
        self._active = False
        self._completed = True


class Phase():
    def __init__(
            self,
            stage_config: list,
            urgency: bool = False
            ):
        self._urgent = urgency
        self._stage_config = stage_config
        self._create_phase()

    def _create_phase(
            self
        ):
        self._stages = []
        urgency_multiplier = 1
        if self._urgent:
            urgency_multiplier = 0.5
        for stage in self._stage_config:
            self._stages.append(Stage(stage["name"], stage["duration"]))


    def _init_phase(self, start_date: dt.datetime):
        rolling_date = start_date
        for stage in self._stages:
            stage._set_active(rolling_date)
            rolling_date += dt.timedelta(days=stage._duration)


# TODO: Define a __get__ (check correct dunder function) that returns the stats of the Stage as a dict for storage.
# TODO: Define a __print__ dunder that prints the details of the stage when called.