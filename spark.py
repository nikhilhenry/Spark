import wx
import wikipedia
import wolframalpha
from espeak import espeak

#Api stuff
app_id = "YPR8W2-2JJ5UWLW8G"#wolframalpha api key
client = wolframalpha.Client(app_id)#creating client for wikipedia

espeak.synth("Hey I'm Spark")#fisrt statement on bootup


#UI declaration and intialization
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
        label="Hello I am Spark the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()


    #Getting query
    def OnEnter(self, event):

        input = self.txt.GetValue()
        input = input.lower()#Changing to a lower case

        #Fun stuff

        if input == "who created you" or input == "who created you ?" or input == "who created you?" or input == "who made you" or input == "who made you ?" or input == "who made you?" :
            print "I was created by a genius, 13 year old Nikhil Henry and 14 year old Abhinav Shenoy"
            espeak.synth("I was created by a genius, 13 year old Nikhil Henry and 14 year old Abhinav Shenoy")


        elif  input == "who are you" or input == "what are you" or input == "who are you ?" or input == "what are you ?" or input == "what are you?" or input == "who are you?":
              print "I'm Spark the python Digital Assistant"
              espeak.synth("I'm Spark the python Digital Assistant")

        elif  input == "where were you made" or input == "where were you made ?" or input == "where were you created" or input == "where were you created ?" or input == "where were you made?" or input == "where were you created?":
              print "I was created in Bangalore,India"
              espeak.synth("I was created in Bangalore,India")

        elif input == "whats your name" or input == "what's your name ?" or input == "what's your name?" or input == "whats your name?" or input == "whats your name ?":
             print "My name is Python Digital Assistant but you can call me PyDa"
             espeak.synth("My name is Python Digital Assistant but you can call me PyDa")

        elif input == "howdy":
             print "howdy partner"
             espeak.synth("howdy partner")

        elif input == "i love you" or input == "i love you Spark" or input == "I love you Spark" or input == "i love you spark":
             print "I am a computer, I have no feelings"
             espeak.synth("I am a computer, I have no feelings")
        elif input == "how are you" or input == "how are you?":
             print "I am fine, how are you?"
             espeak.synth("I am fine, how are you?")
        else:

            try:

                #Fetching data
                try:#from wolframalpha
                    res = client.query(input)
                    answer = next(res.results).text
                    print answer
                    espeak.synth(answer)

                except:#from wikipedia
                    input = input.split(' ')

                    input = ' '.join(input[2:])

                    print wikipedia.summary(input)
                    espeak.synth("I found this article on wikipedia")
            except:
                print "Check your internet connection, error code 404"


#to keep runing
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
