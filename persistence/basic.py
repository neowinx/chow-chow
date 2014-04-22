import wx

tasks = []
stop_watch = wx.StopWatch()
DEFAULT_TASKS = ['Breakfast', 'Lunch']


class Task():
    def __init__(self, task_name):
        self.task = task_name
        self.time = 0