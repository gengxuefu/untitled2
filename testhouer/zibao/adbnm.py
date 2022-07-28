import os
import time

class Adbmoth():
    def adbexe(self,adb):
        adbpull ="adb shell {}".format(adb)
        os.system(adbpull)


    def adbpull(self,pull):
        adbpull1 = "adb pull {}".format(pull)
        os.system(adbpull1)

if __name__ == '__main__':

    adbm = Adbmoth()
    adbm.adbexe("input tap 141 1729")
    time.sleep(1)
    adbm.adbexe("input tap 444 1326")
    time.sleep(1)
    adbm.adbexe("input tap 882 494")

#   //*[@    and @text = '']