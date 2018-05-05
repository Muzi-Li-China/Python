import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'花名册',size=(520,450))
        panel = wx.Panel(self)
        labeAll = wx.StaticText(panel,
                                -1,
                                '记录',
                                pos=(220,5),
                                )
        self.textAll = wx.TextCtrl(panel,
                                   -1,
                                   size = (480,200),
                                   pos = (10,25),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
        labelName = wx.StaticText(panel,
                                  -1,
                                  '姓名',
                                  pos = (10,235),
                                  )
        self.textName = wx.TextCtrl(panel,
                                    -1,
                                    size = (300,25),
                                    pos = (40,230),
                                    )
        labelSex = wx.StaticText(panel,
                                 -1,
                                 '性别',
                                 pos = (10,265),
                                 )
        self.textSex = wx.TextCtrl(panel,
                                   -1,
                                   size = (300,25),
                                   pos = (40,260),
                                   )
        labelAge = wx.StaticText(panel,
                                 -1,
                                 '年龄',
                                 pos =(10,295),
                                 )
        self.textAge = wx.TextCtrl(panel,
                                   -1,
                                   size = (300,25),
                                   pos = (40,290),
                                   )
        self.btnPut = wx.Button(panel,-1,'提交',size=(75,25),pos = (220,350))
        self.Bind(wx.EVT_BUTTON,self.OnButtonPut,self.btnPut)

    def OnButtonPut(self,event):
        name = self.textName.GetValue()
        self.textName.Clear()
        sex = self.textSex.GetValue()
        self.textSex.Clear()
        age = self.textAge.GetValue()
        self.textAge.Clear()
        user = 'name：%s, sex：%s, age：%s\n'%(name,sex,age)
        self.textAll.AppendText(user)


app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
