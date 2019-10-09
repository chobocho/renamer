import wx
from simpleguipanel import *
from simpleguimenu import * 
from renamerpanel import *
from doaction import *

WINDOW_W_SIZE = 800
WINDOW_H_SIZE = 600

class SimpleGuiFrame(wx.Frame):
    def __init__(self, versionInfo, *args, **kw):
        super(SimpleGuiFrame, self).__init__(*args, **kw)
        self.SW_VERSION = versionInfo
        self._addMenubar()
        
        self.splitter = wx.SplitterWindow(self, -1, wx.Point(0, 0), wx.Size(WINDOW_W_SIZE, WINDOW_H_SIZE), wx.SP_3D | wx.SP_BORDER)
        self.leftPanel = SimpleGuiPanel(self, self.splitter)
        self.rightPanel = RenamerPanel(self, self.splitter)
        self.splitter.SplitVertically(self.leftPanel, self.rightPanel)
        self.splitter.SetMinimumPaneSize(20)
       
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)
       
        self.doAction = DoAction(self)

    def _addMenubar(self):
        self.menu = SimpleGuiMenu(self)

    def OnUpdateList(self, fileList):
        self.leftPanel.OnUpdateList(fileList)
        self.rightPanel.OnUpdateList(fileList)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        msg = self.SW_VERSION + "\nhttp://chobocho.com"
        title = 'About'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)

    def OnShowError(self, msg):
        title = 'Error'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_ERROR)

    def OnShowSuccess(self, msg):
        title = 'Rename'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)

    def OnRename(self):
        print ("Frame: OnRename")
        preSourceFileList = self.leftPanel.OnGetText()
        sourceFileList = preSourceFileList.split('\n')
        preTargetFileList = self.rightPanel.OnGetText()
        targetFileList = preTargetFileList.split('\n')
        result, msg = self.doAction.OnRename(sourceFileList, targetFileList)

        if (result == False):
            self.OnShowError(msg)
        else: 
            self.OnShowSuccess(msg)

    def OnCopyToClipBoard(self):
        target = self.rightPanel.OnGetText()
        if len(target) == 0:
            return
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(target))
            wx.TheClipboard.Close()

 