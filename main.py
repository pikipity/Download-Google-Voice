# encoding=utf-8
import Tkinter
import ttk
import sys

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
DataPathButton=Tkinter.Button(DataPathFrame,text="...")
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
DownloadButton=Tkinter.Button(ControlFrame,text="Download Voice")
DownloadButton.pack(side="left")
PlayButton=Tkinter.Button(ControlFrame,text="Play Voice")
PlayButton.pack(side="left")
OpenFolderButton=Tkinter.Button(ControlFrame,text="Open Folder")

root.mainloop()