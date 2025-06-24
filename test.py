from model.tasks import Phase
import datetime as dt

# root = tk.Tk()

# test_task = Task(dt.datetime.today(), 1234, 1235, "Test Item", "France")

phase_1 = Phase(
    [{"name": "WorkbookCreation", "duration": 7}, {"name": "WorkBookCompletion", "duration": 7}],
    False
    )