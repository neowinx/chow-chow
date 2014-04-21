import wx


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item


class PromptingComboBox(wx.ComboBox):
    def __init__(self, *args, **kwargs):
        wx.ComboBox.__init__(self, *args, **kwargs)
        self.choices = []
        self.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_CHAR, self.EvtChar)
        self.Bind(wx.EVT_COMBOBOX, self.EvtCombobox)
        self.ignore_evt_text = False

    def EvtCombobox(self, event):
        self.ignore_evt_text = True
        event.Skip()

    def EvtChar(self, event):
        if event.GetKeyCode() == 8 or event.GetKeyCode() == 127:
            self.ignore_evt_text = True
        event.Skip()

    def EvtText(self, event):
        if self.ignore_evt_text:
            self.ignore_evt_text = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.choices :
            if choice.startswith(currentText):
                self.ignore_evt_text = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetMark(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()