#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

TRAY_TOOLTIP = 'Chow Chow'
TRAY_ICON = 'drawing.png'
FRAME_ICON = 'icon32.png'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item


class ChowChowTaskBarIcon(wx.TaskBarIcon):

    def __init__(self, frame):
        super(ChowChowTaskBarIcon, self).__init__()
        self.frame = frame
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(TRAY_ICON)), TRAY_TOOLTIP)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Show/Hide Configuration', self.on_show_main_window)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def on_left_down(self, event):
        diag = wx.SingleChoiceDialog(self.frame, 'Enter the name of the task', 'Task', ('holiss', 'huluss'))
        res = diag.ShowModal()
        diag.Destroy()
        print res

    def on_show_main_window(self, event):
        if self.frame.IsShown():
            self.frame.Show(False)
        else:
            self.frame.Show(True)

    def on_exit(self, event):
        self.frame.Close()


class ChowChowFrame(wx.Frame):

    def __init__(self, parent, id, title):

        # init the Frame
        wx.Frame.__init__(self, parent, id, title, size=(310, 200))
        self.tbicon = ChowChowTaskBarIcon(self)

        # set the Frame icon
        self.SetIcon(wx.IconFromBitmap(wx.Bitmap(FRAME_ICON)))

        # hide the Frame at the begining
        self.Show(False)

        # set the callback when the Frame is closed
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        diag = wx.MessageDialog(self, 'Do you really want to close Chow Chow?', 'Why? Wof!',
                                wx.OK | wx.CANCEL | wx.ICON_QUESTION | wx.CENTRE)
        result = diag.ShowModal()
        diag.Destroy()
        if result == wx.ID_OK:
            self.tbicon.RemoveIcon()
            self.tbicon.Destroy()
            self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = ChowChowFrame(None, -1, 'Chow Chow')
    app.MainLoop()