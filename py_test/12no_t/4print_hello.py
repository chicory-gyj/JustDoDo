#!/usr/bin/python
def hello(event):
    print 'Hello,world!'
import wx
app=wx.App()
win=wx.Frame(None,title='isn\'t funny?',size=(400,200))
button=wx.Button(win,label='Hello')
button.Bind(wx.EVT_BUTTON,hello)
win.Show()
app.MainLoop()
    
