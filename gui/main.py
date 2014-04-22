from gui.generated import *
from gui.extra import *
from persistence.basic import *

TRAY_TOOLTIP = 'Chow Chow'
TRAY_ICON = 'icon32.png'
FRAME_ICON = 'icon32.png'


class TasksFrame(TasksBaseFrame):
    def __init__(self, parent):
        TasksBaseFrame.__init__(self, parent)
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(FRAME_ICON)))


class ChowChowTaskBarIcon(wx.TaskBarIcon):

    def __init__(self, frame):
        super(ChowChowTaskBarIcon, self).__init__()
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(TRAY_ICON)), TRAY_TOOLTIP)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.show_hide_main_window)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'View Tasks', self.view_tasks)
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def view_tasks(self, event):
        num_tasks = len(TASKS)
        if num_tasks > 0:
            tasks_frame = TasksFrame(self.frame)
            tasks_frame.tasks_grid.AppendRows(num_tasks - 1)
            TASKS[-1] = update_task_time(TASKS[-1], STOP_WATCH.Time())
            row = 0
            for t in TASKS:
                print 'task_id:', t[TUPLE_INDEX_ID]
                tasks_frame.tasks_grid.SetCellValue(row, 0, t[TUPLE_INDEX_TASK])
                tasks_frame.tasks_grid.SetCellValue(row, 1, (t[TUPLE_INDEX_TIME] / 60000).__str__())
                tasks_frame.tasks_grid.SetCellValue(row, 2, t[TUPLE_INDEX_START])
                row += 1

            tasks_frame.Show(True)

    def show_hide_main_window(self, event):
        if self.frame.IsShown():
            self.frame.Show(False)
        else:
            self.frame.Show(True)
            self.frame.cmb_task.SetFocus()

    def on_exit(self, event):
        self.frame.Close()


class ChowChowFrame(MainFrame):

    def __init__(self, parent):
        MainFrame.__init__(self, parent)

        # UI stuff that cannot be generated

        # Assing the task baricon
        self.task_bar_icon = ChowChowTaskBarIcon(self)
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(FRAME_ICON)))
        self.Show(True)

        # Loading tasks inside the combo

        self.cmb_task.choices = DEFAULT_TASKS
        self.cmb_task.Clear()
        self.cmb_task.AppendItems(DEFAULT_TASKS)

        # Center the frame and set focus in the combo

        self.Centre()
        self.cmb_task.SetFocus()

    def cmb_task_key_up(self, event):
        if event.GetKeyCode() == 13:
            if self.insert_task():
                self.Show(False)

    def cmb_task_key_down(self, event):
        if event.GetKeyCode() == 27:
            self.Show(False)
        else:
            event.Skip()

    def btn_ok_click(self, event):
        if self.insert_task():
            self.Show(False)

    def btn_cancel_click(self, event):
        self.Show(False)

    def insert_task(self):
        if len(TASKS) > 0:
            TASKS[-1] = update_task_time(TASKS[-1], STOP_WATCH.Time())
        TASKS.append(create_task(self.cmb_task.GetValue()))
        STOP_WATCH.Start()
        self.cmb_task.SetValue('')
        return True

    def on_close(self, event):
        diag = wx.MessageDialog(self, 'Do you really want to close Chow Chow?', 'Why? Woof!',
                                wx.OK | wx.CANCEL | wx.ICON_QUESTION | wx.CENTRE)
        result = diag.ShowModal()
        diag.Destroy()
        if result == wx.ID_OK:
            self.task_bar_icon.RemoveIcon()
            self.task_bar_icon.Destroy()
            self.Destroy()