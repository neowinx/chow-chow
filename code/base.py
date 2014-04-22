import wx
from time import time
import datetime


TASKS = []
STOP_WATCH = wx.StopWatch()
DEFAULT_TASKS = ['Breakfast', 'Lunch']
TUPLE_INDEX_ID = 0
TUPLE_INDEX_TASK = 1
TUPLE_INDEX_TIME = 2
TUPLE_INDEX_START = 3


def create_task(task):
    return time(), task, 0, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def update_task_time(task_tuple, new_time):
    return task_tuple[TUPLE_INDEX_ID], task_tuple[TUPLE_INDEX_TASK], new_time, task_tuple[TUPLE_INDEX_START]