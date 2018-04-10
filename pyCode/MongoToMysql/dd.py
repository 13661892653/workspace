#coding=utf-8
import speech
import win32api
import os

##while True:
##    words=raw_input("Please input some words:")
##    if words.lower()=='stop':
##        break
##    speech.say(words)

##contents=speech.input("Say something,please.")
##speech.say(contents)
##print(contents)

if __name__ == '__main__':
    Start = '你在哪'
    Hello = '你好'
    Control = '关闭语音控制'
    openPython = '我要写代码'
    openMusic = '我要听音乐'
    stormPlayer = '我要看电影'
    tencentQQ = '我要'
    listenMusic = '我累了'
    Hawk = '你是谁'
    Users = '你知道我是谁么'
    Love = '你喜欢我么'

    ##    judge=speech.input()
    ##    while True:
    ##        if(judge == Start):
    ##            speech.say("我在这呢，你说吧")
    ##            break

    while True:
        words = speech.input("Say you want to do.")
        ##print(words)
        if (words == Control):
            speech.say("已关闭语音控制")
            break
        elif (words == Hello):
            speech.say("你也好，今天过得怎么样")
        elif (words == openPython):
            os.system('D:\Python\python.exee')
        ##            win32.api.ShellExecute(0,'open','D:\Python\python.exe','','',0)
        ##            win32.api.ShellExecute(0,'open','D:\Python\python.exe','','',1)
        elif (words == openMusic):
            os.system('D:\QQ音乐\QQMusic\QQMusic.exe')
        ##            win32.api.ShellExecute(0,'open','D:\QQ音乐\QQMusic\QQMusic.exe','','',0)
        ##            win32.api.ShellExecute(0,'open','D:\QQ音乐\QQMusic\QQMusic.exe','','',1)
        elif (words == stormPlayer):
            os.system('D:\暴风影音\StormPlayer.exe')
        elif (words == tencentQQ):
            os.system('D:\QQ\Bin\QQ.exe')
        elif (words == listenMusic):
            speech.say("那就听会儿音乐吧")
            os.system('D:\QQ音乐\QQMusic\QQMusic.exe')
        elif (words == Hawk):
            speech.say("我叫Hawk")
        elif (words == Users):
            speech.say("我是谁，我也不知道")
        elif (words == Love):
            speech.say("不喜欢，下一个")
        else:
            speech.say("暂时不支持此功能")

words=speech.input("Say you want to do.")
words=str(words)
print(words)