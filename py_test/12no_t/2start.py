#!/usr/bin/python
import wx
app=wx.App()
win=wx.Frame(None,title='Find a file',size=(430,400))
openbtn=wx.Button(win,label='Open',pos=(300,10),size=(60,20))
savebtn=wx.Button(win,label='Save',pos=(360,10),size=(60,20))
filename=wx.TextCtrl(win,pos=(10,10),size=(250,20))
contents=wx.TextCtrl(win,pos=(10,40),size=(400,300),style=wx.TE_MULTILINE|wx.HSCROLL)
win.Show()
app.MainLoop()

