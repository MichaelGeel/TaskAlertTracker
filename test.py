import tkinter as tk
from tasks import Task
import datetime as dt

root = tk.Tk()

test_task = Task(dt.datetime.today(), 1234, 1235, "Test Item", "France")