import wx
from filedrop import *
from simpleguipanel import *

WINDOW_W_SIZE = 400
WINDOW_H_SIZE = 600

class RenamerPanel(SimpleGuiPanel):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent, *args, **kw)
        self.initUI()
        self.parent = parent

    def initUI(self):
        renameBtnId = wx.NewId()
        renameBtn = wx.Button(self, renameBtnId, "Rename", size=(60,30))
        renameBtn.Bind(wx.EVT_BUTTON, self.OnRenameBtn)
        self.btnBox.Add(renameBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        copyBtnId = wx.NewId()
        copytBtn = wx.Button(self, copyBtnId, "Copy", size=(60,30))
        copytBtn.Bind(wx.EVT_BUTTON, self.OnCopyBtn)
        self.btnBox.Add(copytBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

    def OnRenameBtn(self, event):
        print("OnRenameBtn")
        self.parent.OnRename()

    def OnCopyBtn(self, event):
        print("OnCopyBtn")
        self.parent.OnCopyToClipBoard()
