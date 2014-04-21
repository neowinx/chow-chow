from gui.main import *

FRAME_ICON = 'icon32.png'


class TasksFrame(TasksBaseFrame):
    def __init__(self, parent):
        TasksBaseFrame.__init__(self, parent)
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(FRAME_ICON)))