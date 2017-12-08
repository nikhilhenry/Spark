import wx
import wikipedia
import wolframalpha
import os

#Api stuff
app_id = "YPR8W2-2JJ5UWLW8G"#wolframalpha api key
client = wolframalpha.Client(app_id)#creating client for wikipedia

os.system("espeak Hey_I\'m_Spark")#fisrt statement on bootup


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
            os.system("espeak I_was_created_by_a_genius,_13_year_old_Nikhil_Henry_and_14_year_old_Abhinav_Shenoy")


        elif  input == "who are you" or input == "what are you" or input == "who are you ?" or input == "what are you ?" or input == "what are you?" or input == "who are you?":
              print "I'm Spark the python Digital Assistant"
              os.system("espeak I\'m_Spark_the_python_Digital_Assistant")

        elif  input == "where were you made" or input == "where were you made ?" or input == "where were you created" or input == "where were you created ?" or input == "where were you made?" or input == "where were you created?":
              print "I was created in Bangalore,India"
              os.system("espeak I_was_created_in_Bangalore,India")

        elif input == "whats your name" or input == "what's your name ?" or input == "what's your name?" or input == "whats your name?" or input == "whats your name ?":
             print "My name is Python Digital Assistant but you can call me PyDa"
             os.system("espeak My_name_is_Spark!")

        elif input == "howdy":
             print "howdy partner"
             os.system("espeak howdy_partner")

        elif input == "i love you" or input == "i love you Spark" or input == "I love you Spark" or input == "i love you spark":
             print "I am a computer, I have no feelings"
             os.system("espeak I_am_a_computer,_I_have_no_feelings")
        elif input == "how are you" or input == "how are you?":
             print "I am fine, how are you?"
             os.system("espeak I_am_fine,_how_are_you?")
        else:

            try:

                #Fetching data
                try:#from wolframalpha
                    res = client.query(input)
                    answer = next(res.results).text
                    answer = answer.replace(" ", "_")
                    print answer
                    os.system("espeak ")

                except:#from wikipedia
                    input = input.split(' ')

                    input = ' '.join(input[2:])

                    print wikipedia.summary(input)
                    os.system("espeak I found this article on wikipedia")
            except:
                print "Check your internet connection, error code 404"


#to keep runing
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()