# encoding=utf-8
import Tkinter
import ttk
import sys
import threading
import os
import tkFileDialog
import urllib

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
#URL opener version
URLOpenerVersion="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3)"

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
    #Encode Message
    try:
        Message=Message.decode('utf8')
    except:
        pass
    try:
        Message=Message.decode('gbk')
    except:
        pass
    Message=Message.encode('utf-8')
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
        DownloadMP3(Information)

class AppURLopener(urllib.FancyURLopener):
    version=URLOpenerVersion

def DownloadProcess(a,b,c):
    if c==0:
        UpdateStation("Google don't have this voice. Please check the choosing language.")
    else:
        per = 100.0 * a * b / c
        if per>100:
            per=100
        UpdateStation('Download '+'%.2f%%' % per)

def DownloadMP3(Information):
    Message=Information[0]
    LengthMessage=len(Message.decode('utf-8'))
    StoragePath=Information[1]
    Language=Information[2]
    urllib._urlopener=AppURLopener()
    ie='ie=UTF-8'
    q='q='+urllib.quote(Message)
    if Language==LanguageList[0]:
        tl='tl=zh-CN'
    elif Language==LanguageList[1]:
        tl='tl=en'
    else:
        tl='tl=ja'
    WebSite='https://translate.google.com.hk/translate_tts?'+\
        ie+'&'+q+'&'+tl
    if LengthMessage>10:
        StoragePath=StoragePath+Message.decode('utf-8')[0:9].encode('utf-8')+'.mp3'
    else:
        StoragePath=StoragePath+Message+'.mp3'
    try:
        urllib.urlretrieve(WebSite,StoragePath,DownloadProcess)
    except:
        UpdateStation("Download failed. Please check the network.")
    else:
        fp=open(ProgramPath+'/store/recent_download.txt','w')
        fp.write(StoragePath)
        fp.close()
#########################################################################
####### Play Voice Button ##############################################
#Play Voice thread
def PlayVoiceButton():
    PlayVoiceThread=threading.Thread(target=PlayVoiceFunction)
    PlayVoiceThread.start()
#Play Voice Function
def PlayVoiceFunction():
    #get recent download file
    try:
        fp=open(ProgramPath+'/store/recent_download.txt','r')
        StoragePath=fp.readline()
        if StoragePath[len(StoragePath)-1]=='\n':
            StoragePath=StoragePath[:len(StoragePath)-1]
        fp.close()
    except:
        UpdateStation("Please download at least one file.")
    else:
        #play voice
        StoragePathOs=StoragePath.replace(' ','\ ')
        if os.path.isfile(StoragePath):
            UpdateStation("Begin to play recent download file.")
            if sys.platform[:5]=="linux":
                os.popen2('aplay -q' + StoragePathOs)
            elif sys.platform=='darwin':
                os.system('afplay '+StoragePathOs)
            else:
                UpdateStation("Now, it cannot play voice in Windows.")
            #    WindowsPlayVoice(StoragePath)
            UpdateStation("Finish playing")
        else:
            UpdateStation("You haven't download file.")
#PLay Voice for windows
#def WindowsPlayVoice(StoragePath):
    #1.二进制方法读取前 10000 个字节，保证能读到第一帧音频数据
#    f = open(StoragePath, 'rb' )
#    data= f.read(10000)
    #2.创建合成器对象，解析出最初的几帧音频数据
#    import pymedia.muxer as muxer
#    dm = muxer.Demuxer('mp3')
#    frames = dm.parse( data )
#    print len(frames)
    #3.根据解析出来的 Mp3 编码信息，创建解码器对象
#    import pymedia.audio.acodec as acodec
#    dec = acodec.Decoder( dm.streams[ 0 ] )
    #像下面这样也行
    #params = {'id': acodec.getCodecID('mp3'), 'bitrate': 128000, 'sample_rate': 44100, 'ext': 'mp3', 'channels': 2}
    #dec= acodec.Decoder(params)
    #4.解码第一帧音频数据
#    frame = frames[0]
    #音频数据在 frame 数组的第二个元素中
#    r= dec.decode( frame[ 1 ] )
#    UpdateStation("sample_rate:%s , channels:%s " % (r.sample_rate,r.channels))
    #注意：这一步可以直接解码 r=dec.decode( data)，而不用读出第一帧音频数据
    #但是开始会有一下噪音，如果是网络流纯音频数据，不包含标签信息，则不会出现杂音
    #5.创建音频输出对象
#    import pymedia.audio.sound as sound
#    snd = sound.Output( r.sample_rate, r.channels, sound.AFMT_S16_LE )
    #6.播放
#    if r: snd.play( r.data )
    #7.继续读取、解码、播放
#    while True:
#        data = f.read(512)
#        if len(data)>0:
#            r = dec.decode( data )
#            if r: snd.play( r.data )
#        else:
#            break
    #8.延时，直到播放完毕
#    import time
#    while snd.isPlaying(): time.sleep( .5 )
########################################################################
###### Open Folder Button #############################################
def OpenFolderFunction():
    Information=TakeInformation()
    Path=Information[1]
    PathOs=Path.replace(' ','\ ')
    if os.path.exists(Path):
        if sys.platform=='darwin':
            os.system("open "+PathOs)
        else:
            UpdateStation("Now, Only can open folder in Mac")
    else:
        UpdateStation("The path you input doesn't exist.")
######################################################################

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
PlayButton=Tkinter.Button(ControlFrame,text="Play Voice",command=PlayVoiceButton)
PlayButton.pack(side="left")
OpenFolderButton=Tkinter.Button(ControlFrame,text="Open Folder",command=OpenFolderFunction)
OpenFolderButton.pack(side="left")
#Station bar
Station=Tkinter.StringVar()
StationBar=Tkinter.Label(root,textvariable=Station)
StationBar.pack(fill="x")
UpdateStation("Let's take liberties with Google! (╯▔▽▔)╯")

root.mainloop()