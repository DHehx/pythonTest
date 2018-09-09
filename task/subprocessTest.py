#启动其他应用程序
import subprocess,webbrowser,time
# subprocess.Popen('C:\Windows\System32\calc.exe')
# subprocess.Popen(['C:\Windows\System32\\notepad.exe','C:\\test.txt'])#传参
#
# #打开网站
#webbrowser.open('https://www.google.com/')

#运行其他python脚本
# subprocess.Popen(['C:/Users/67551/AppData/Local/Programs/Python/Python36/python.exe','D:/project/python/test/web/task/subprocessTest1.py'])

#用默认应用程序打开文件
# fileObj = open('test.txt','wb')
# fileObj.write(bytes('Hello world!','UTF-8'))
# fileObj.close()
# subprocess.Popen(['start','test.txt'],shell=True) #windows 'start' OS X'open' Linux'see'  ,shell=True上需要
# OS X上使用：subprocess.Popen(['open','test.txt']) #windows 'start' OS X'open' Linux'see'

#倒计时播放音频文件
# timeLeft = 10
# while timeLeft >0:
#     print(timeLeft,end='')
#     time.sleep(1)
#     timeLeft -=1
#
# subprocess.Popen(['start','music.mp3'],shell=True)