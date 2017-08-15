#!/usr/bin/python
import wx

def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

app=wx.App()
win=wx.Frame(None,title='Find A File',size=(430,400))
bkg=wx.Panel(win)

loadbutton=wx.Button(bkg,label='Open')
loadbutton.Bind(wx.EVT_BUTTON,load)

savebutton=wx.Button(bkg,label='Save')
savebutton.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadbutton,proportion=0,flag=wx.EXPAND|wx.LEFT,border=5)
hbox.Add(savebutton,proportion=0,flag=wx.EXPAND|wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM,border=5)

bkg.SetSizer(vbox)


win.Show()
app.MainLoop()
