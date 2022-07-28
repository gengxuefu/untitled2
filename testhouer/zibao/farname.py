#coding=utf-8

import os
import time
import random

class adbmo():
    def execute(self,cmd):
       #shell 命令直接调用
       adbstr = "adb shell {}".format(cmd)
       print(adbstr)
       os.system(adbstr)

    def tapadb(self,tapzb):
        #根据坐标点击
        tapstar = "adb shell input tap {}".format(tapzb)
        print(tapstar)
        os.system(tapstar)

    def swipeadb(self,swipe):
        #滑动点击点击
        swipestar = "adb shell input swipe {}".format(swipe)
        print(swipestar)
        os.system(swipestar)

    def screecapadb(self,scerrcap):
        scrrcapstar ="adb shell screencap {}".format(scerrcap)
        print(scrrcapstar)
        os.system(scrrcapstar)

    def screenrecordadb(self,screenrecord=None):
        #判断是否自定义名称
        if not screenrecord is None:
            screenrecord = screenrecord
        else:
            screenrecord = random.random()
        print(screenrecord)
        #录屏取到本地
        screenrecordstar ="adb shell screenrecord /sdcard/{}.mp4".format(screenrecord)
        print(screenrecordstar)
        sp_list = screenrecordstar.split(" ")
        pulladb = "adb pull {} E:\\".format(sp_list[3])
        print(pulladb)
        os.system(screenrecordstar)




if __name__ == '__main__':
    adb = adbmo()
    # adb.execute("input tap 678.7 2077.3")
    # time.sleep(5)
    # adb.swipeadb("857 1700 857 1000")
    adb.screenrecordadb()