import wx

tasks = []
stop_watch = wx.StopWatch()


class Task():
    def __init__(self, task_name):
        self.task = task_name
        self.time = 0