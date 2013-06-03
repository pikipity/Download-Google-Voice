# encoding=utf-8
import Tkinter
import ttk
import sys
import threading
import os
import tkFileDialog

#icon path
if sys.platform[:5] == 'linux' or sys.platform=='darwin':
    ProgramPath=sys.argv[0][0:sys.argv[0].rfind('/')]#no final "/"
    IconPath=ProgramPath+'/icon/Voice.icns'
else:
    ProgramPath=sys.argv[0]
    ProgramPath=ProgramPath.replace('\\','/')
    ProgramPath=ProgramPath[0:ProgramPath.rfind('/')]#no final "/"
    IconPath=ProgramPath+'icon/Voice.ico'
#Default Message
MessageDefault=u"一起调戏谷歌娘"
#Data Default Path
DataDefaultPath=ProgramPath+'/store/'
#Language Default
LanguageDefault="Chinese"
#Language can be selected
LanguageList=["Chinese","English","Japanese"]

#Update station bar message function
def UpdateStation(Message):
    Station.set(Message)

########## Data Path Button #############################################
def DataPathButton():
    DataPathChoosing=tkFileDialog.askdirectory(title="Storage Path",initialdir=DataDefaultPath)
    if DataPathChoosing:
        DataPathEntry.delete(0,"end")
        DataPathEntry.insert("end",DataPathChoosing)

########## Download Voice button ########################################
#Take Information function
def TakeInformation():
    Message=MessageEntry.get()
    StoragePath=DataPathEntry.get().replace("\\","/")
    if not StoragePath[len(StoragePath)-1]=="/":
        StoragePath=StoragePath+"/"
        DataPathEntry.delete(0,"end")
        DataPathEntry.insert("end",StoragePath)
    Language=LanguageChoose.get()
    Information=[Message,StoragePath,Language]
    return Information

#Check Information
def CheckInformation(Information):
    Message=Information[0]
    StoragePath=Information[1]
    Language=Information[2]
    #Decode Message
    try:
        Message.decode('utf8')
    except:
        pass
    else:
        try:
            Message.decode("gbk")
        except:
            pass
        else:
            pass
    #Check Storage Path
    if not os.path.exists(StoragePath):
        UpdateStation("Storage Path Wrong. There is not this folder.")
        return 0
    else:
        #Check if language in the LanguageList
        for Languagex in LanguageList:
            if Language==Languagex:
                return 1
            else:
                if Languagex==LanguageList[len(LanguageList)-1]:
                    UpdateStation("Language is not supported. PLease choose a language in the list.")
                    return 0
                else:
                    pass

#Download Voice thread
def DownloadVoiceButton():
    DownloadVoiceThread=threading.Thread(target=DownloadVoiceMainFunction)
    DownloadVoiceThread.start()

#Downliad Voice Main Function
def DownloadVoiceMainFunction():
    Information=TakeInformation()
    if not CheckInformation(Information):
        pass
    else:
        UpdateStation("Get all information. And Information are correct.")

#########################################################################

#root window
root=Tkinter.Tk()
root.title('Google Voice Downloader')
root.iconbitmap(IconPath)

#input message part
MessageFrame=Tkinter.Frame(root)
MessageFrame.pack()
MessageLabel=Tkinter.Label(MessageFrame,text="Message: ")
MessageLabel.pack(side="left")
MessageEntry=Tkinter.Entry(MessageFrame,width=150/2)
MessageEntry.pack(side="left")
MessageEntry.insert("end",MessageDefault)
#Data path
DataPathFrame=Tkinter.Frame(root)
DataPathFrame.pack()
DataPathLabel=Tkinter.Label(DataPathFrame,text="Storage Path: ")
DataPathLabel.pack(side="left")
DataPathEntry=Tkinter.Entry(DataPathFrame,width=150/2)
DataPathEntry.pack(side="left")
DataPathEntry.insert("end",DataDefaultPath)
DataPathButton=Tkinter.Button(DataPathFrame,text="...",command=DataPathButton)
DataPathButton.pack()
#Lagnuage
LanguageFrame=Tkinter.Frame(root)
LanguageFrame.pack()
LanguageLabel=Tkinter.Label(LanguageFrame,text="Language: ")
LanguageLabel.pack(side="left")
LanguageChoose=Tkinter.StringVar()
LanguageChoose.set(LanguageDefault)
LanguageSelect=ttk.Combobox(LanguageFrame,text=LanguageChoose,values=LanguageList)
LanguageSelect.pack(side="left")
#Control Button
ControlFrame=Tkinter.Frame(root)
ControlFrame.pack()
DownloadButton=Tkinter.Button(ControlFrame,text="Download Voice",command=DownloadVoiceButton)
DownloadButton.pack(side="left")
PlayButton=Tkinter.Button(ControlFrame,text="Play Voice")
PlayButton.pack(side="left")
OpenFolderButton=Tkinter.Button(ControlFrame,text="Open Folder")
#Station bar
Station=Tkinter.StringVar()
StationBar=Tkinter.Label(root,textvariable=Station)
StationBar.pack(fill="x")
UpdateStation("Let's take liberties with Google! (╯▔▽▔)╯")

root.mainloop()