import wx
import os
from time import time
import datetime
from code.sqlite_functions import *

db_create_initial_schema()
TASKS = db_select_tasks()
STOP_WATCH = wx.StopWatch()
TUPLE_INDEX_ID = 0
TUPLE_INDEX_TASK = 1
TUPLE_INDEX_TIME = 2
TUPLE_INDEX_START = 3


def create_task(task):
    return time(), task, 0, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def update_task_time(task_tuple, new_time):
    return task_tuple[TUPLE_INDEX_ID], task_tuple[TUPLE_INDEX_TASK], new_time, task_tuple[TUPLE_INDEX_START]


def update_task_task(task_tuple, new_task):
    return task_tuple[TUPLE_INDEX_ID], new_task, task_tuple[TUPLE_INDEX_TIME], task_tuple[TUPLE_INDEX_START]


def task_names():
    return [choice[TUPLE_INDEX_TASK] for choice in TASKS]


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )