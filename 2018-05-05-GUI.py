import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'花名册',size=(520,450))
        panel = wx.Panel(self)
        #静态标签
        labelAll = wx.StaticText(panel,
                                -1,
                                '记录',
                                )
        #文本框
        self.textAll = wx.TextCtrl(panel,
                                   -1,
                                   size = (480,200),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY) #文本框的属性
        labelName = wx.StaticText(panel,
                                  -1,
                                  '姓名',
                                  pos = (10,235),
                                  )
        self.textName = wx.TextCtrl(panel,
                                    -1,
                                    size = (300,25),
                                    )
        labelSex = wx.StaticText(panel,
                                 -1,
                                 '性别',
                                 )
        self.textSex = wx.TextCtrl(panel,
                                   -1,
                                   size = (300,25),
                                   )
        labelAge = wx.StaticText(panel,
                                 -1,
                                 '年龄',
                                 )
        self.textAge = wx.TextCtrl(panel,
                                   -1,
                                   size = (300,25),
                                   )
        self.btnPut = wx.Button(panel,-1,'提交',size=(75,25)) #添加按钮
        self.Bind(wx.EVT_BUTTON,self.OnButtonPut,self.btnPut) #响应事件

        #布局管理器
        nameSizer = wx.BoxSizer()
        nameSizer.Add(labelName, proportion=0,flag=wx.ALIGN_CENTER)
        nameSizer.Add(self.textName, proportion=0,flag=wx.ALIGN_CENTER)

        sexSizer = wx.BoxSizer()
        sexSizer.Add(labelSex, proportion=0, flag=wx.ALIGN_CENTER)
        sexSizer.Add(self.textSex, proportion=0, flag=wx.EXPAND)

        ageSizer = wx.BoxSizer()
        ageSizer.Add(labelAge, proportion=0, flag=wx.ALIGN_CENTER)
        ageSizer.Add(self.textAge, proportion=0, flag=wx.EXPAND)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(labelAll, proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll, proportion=0,flag=wx.EXPAND)
        mainSizer.Add(nameSizer, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(sexSizer, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(ageSizer, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.btnPut, proportion=0, flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainSizer)

    #事件函数
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
