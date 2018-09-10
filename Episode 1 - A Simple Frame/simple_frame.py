import wx


class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        button = wx.Button(self, label='Push Me')
        button.Bind(wx.EVT_BUTTON, self.on_push)

    def on_push(self, event):
        print('you pushed me')



class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='Tutorial')

        panel = MyPanel(parent=self)

        self.Show()

if __name__ == '__main__':
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()