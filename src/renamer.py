import wx
from simpleguiframe import *

SW_TITLE = "Chobo Renamer V0.1105_SJ09a"
WINDOW_W_SIZE = 800
WINDOW_H_SIZE = 600

def main(): 
    app = wx.App()
    frm = SimpleGuiFrame(SW_TITLE, None, title=SW_TITLE, size=(WINDOW_W_SIZE,WINDOW_H_SIZE))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()