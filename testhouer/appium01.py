# coding = UTF-8

from appium import webdriver
import time
from .zibao.farname import adbmo

desposet ={
    "platformName": "android",
    "deviceName": "5ad1b922",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".main.view.MainActivity",
    "noReset":True,
    "dontStopAppOnReset":True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desposet)




