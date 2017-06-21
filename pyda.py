import wx
import wikipedia
import wolframalpha


app_id = "YPR8W2-2JJ5UWLW8G"
client = wolframalpha.Client(app_id)



class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

        input = self.txt.GetValue()
        input = input.lower()
        print input 
        if input == "who created you" or "who created you ?" or "who made you" or "who made you ?" :
            answer = "I was created by a genius, 13 year old Nikhil Henry"
            print answer

        elif  input == "who are you" or "what are you" or "who are you ?" or "what are you ?":
              print "I'm PyDa the python Digital Assistant"

        elif  input == "where were you made" or "where were you made ?" or "where were you created" or "where were you created ?":
              print "I was created in bangalore,india"

        else:
            try:
                res = client.query(input)
                answer = next(res.results).text
                print answer

            except:
                input = input.split(' ')
                input = ' '.join(input[2:])

                print wikipedia.summary(input)



if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
