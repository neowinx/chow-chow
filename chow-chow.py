#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

TRAY_TOOLTIP = 'Chow Chow'
TRAY_ICON = 'icon32.png'
FRAME_ICON = 'icon32.png'
DEFAULT_TASKS = ['Breakfast', 'Lunch']


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item


class PromptingComboBox(wx.ComboBox):
    def __init__(self, parent, value, choices=[], style=0, **par):
        wx.ComboBox.__init__(self, parent, wx.ID_ANY, value, style=style | wx.CB_DROPDOWN, choices=choices, **par)
        self.choices = choices
        self.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_CHAR, self.EvtChar)
        self.Bind(wx.EVT_COMBOBOX, self.EvtCombobox)
        self.ignoreEvtText = False

    def EvtCombobox(self, event):
        self.ignoreEvtText = True
        event.Skip()

    def EvtChar(self, event):
        if event.GetKeyCode() == 8:
            self.ignoreEvtText = True
        event.Skip()

    def EvtText(self, event):
        if self.ignoreEvtText:
            self.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.choices :
            if choice.startswith(currentText):
                self.ignoreEvtText = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetMark(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()


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
        wx.Frame.__init__(self, parent, id, title)
        self.task_bar_icon = ChowChowTaskBarIcon(self)
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(FRAME_ICON)))
        self.Show(True)

        self.Bind(wx.EVT_CLOSE, self.on_close)

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)

        lbl_insert_task = wx.StaticText(panel, label="Insert your task:")
        sizer.Add(lbl_insert_task, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        self.cmb_task = PromptingComboBox(panel, '', DEFAULT_TASKS, style=wx.CB_SORT)
        self.cmb_task.Bind(wx.EVT_KEY_DOWN, self.key_down)
        self.cmb_task.Bind(wx.EVT_KEY_UP, self.key_up)
        sizer.Add(self.cmb_task, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        button_ok = wx.Button(panel, label="Ok", size=(90, 28))
        button_close = wx.Button(panel, label="Close", size=(90, 28))
        sizer.Add(button_ok, pos=(3, 3))
        sizer.Add(button_close, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)

        panel.SetSizerAndFit(sizer)
        self.Fit()
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