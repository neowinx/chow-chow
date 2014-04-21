#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

from gui.extra import PromptingComboBox, create_menu_item

TRAY_TOOLTIP = 'Chow Chow'
TRAY_ICON = 'icon32.png'
FRAME_ICON = 'icon32.png'
DEFAULT_TASKS = ['Breakfast', 'Lunch']


class ChowChowTaskBarIcon(wx.TaskBarIcon):

    def __init__(self, frame):
        super(ChowChowTaskBarIcon, self).__init__()
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(TRAY_ICON)), TRAY_TOOLTIP)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.show_hide_main_window)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        #create_menu_item(menu, 'Show/Hide Configuration', self.show_hide_main_window)
        #menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def show_hide_main_window(self, event):
        if self.frame.IsShown():
            self.frame.Show(False)
        else:
            self.frame.Show(True)
            self.frame.cmb_task.SetFocus()

    def on_exit(self, event):
        self.frame.Close()


class ChowChowFrame(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=wx.Size(-1, -1))
        self.task_bar_icon = ChowChowTaskBarIcon(self)
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(FRAME_ICON)))
        self.Show(True)

        self.Bind(wx.EVT_CLOSE, self.on_close)

        panel = wx.Panel(self, size=wx.DefaultSize)
        gb_sizer = wx.GridBagSizer(0, 0)
        gb_sizer.SetFlexibleDirection(wx.BOTH)
        gb_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        lbl_insert_task = wx.StaticText(panel, label="Insert your task:")
        gb_sizer.Add(lbl_insert_task, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.cmb_task = PromptingComboBox(panel, '', DEFAULT_TASKS, style=wx.CB_SORT)
        self.cmb_task.Bind(wx.EVT_KEY_DOWN, self.key_down)
        self.cmb_task.Bind(wx.EVT_KEY_UP, self.key_up)
        gb_sizer.Add(self.cmb_task, pos=(1, 0), span=(1, 1), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        button_ok = wx.Button(panel, label="Ok", size=(90, 28))
        button_close = wx.Button(panel, label="Close", size=(90, 28))

        gb_sizer.Add(button_ok, pos=(3, 3))
        gb_sizer.Add(button_close, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)

        panel_sizer = wx.BoxSizer(wx.VERTICAL)

        panel_sizer.Add(gb_sizer)

        panel.SetSizerAndFit(panel_sizer)

        main_bsizer = wx.BoxSizer(wx.VERTICAL)

        main_bsizer.Add(panel)

        self.SetSizer(main_bsizer)
        self.Centre()
        self.cmb_task.SetFocus()

    def key_up(self, event):
        if event.GetKeyCode() == 13:
            if self.insert_task():
                self.Show(False)

    def key_down(self, event):
        if event.GetKeyCode() == 27:
            self.Show(False)
        else:
            event.Skip()

    def insert_task(self):
        print 'Inserting task: %s', self.cmb_task.GetValue()
        return True

    def on_close(self, event):
        diag = wx.MessageDialog(self, 'Do you really want to close Chow Chow?', 'Why? Wof!',
                                wx.OK | wx.CANCEL | wx.ICON_QUESTION | wx.CENTRE)
        result = diag.ShowModal()
        diag.Destroy()
        if result == wx.ID_OK:
            self.task_bar_icon.RemoveIcon()
            self.task_bar_icon.Destroy()
            self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = ChowChowFrame(None, -1, 'Chow Chow')
    app.MainLoop()