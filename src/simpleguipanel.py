import wx
from filedrop import *

WINDOW_W_SIZE = 400
WINDOW_H_SIZE = 600

class SimpleGuiPanel(wx.Panel):
    def __init__(self, parent, *args, **kw):
        super(SimpleGuiPanel, self).__init__(*args, **kw)
        self._OnEnableDragDrop()
        self._initUi()
        self.SetAutoLayout(True)
        self.parent = parent

    def _OnEnableDragDrop(self):
        filedrop = FileDrop(self)
        self.SetDropTarget(filedrop)

    def _initUi(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(WINDOW_W_SIZE, WINDOW_H_SIZE))
        self.text.SetValue("")
        sizer.Add(self.text, 1, wx.EXPAND)
        
        self.btnBox = wx.BoxSizer(wx.HORIZONTAL)

        clearBtnId = wx.NewId()
        clearBtn = wx.Button(self, clearBtnId, "Clear", size=(50,30))
        clearBtn.Bind(wx.EVT_BUTTON, self.OnClearBtn)
        self.btnBox.Add(clearBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(self.btnBox, 0, wx.ALIGN_CENTRE, 5)
        self.SetSizer(sizer)

    def OnCallback(self, filelist):
        print("OnCallback")
        self.parent.OnUpdateList(filelist)

    def OnUpdateList(self, fileList):
        self._printFileList(fileList)

    def _printFileList(self, files):
        fileList = ""
        for file in files:
            fileList += file + "\n"
        self.text.SetValue(fileList)

    def OnClearBtn(self, event):
        self.text.SetValue("")

    def OnGetText(self):
        return self.text.GetValue()