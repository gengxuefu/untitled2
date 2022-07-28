# coding :utf-8

import pytest
from appium import webdriver


class Testdw():
    def setup(self):
        decset ={
            "platformName": "android",
            "deviceName": "5ad1b922",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".main.view.MainActivity",
            "noReset": True,
            "dontStopAppOnReset": True
        }
        self.drvier = webdriver.Remote("http://127.0.0.1:4723/wd/hub",decset)
        self.drvier.find_elements_by_xpath()

    def teardown(self):
        self.drvier.quit()
        

    def test_appu(self):
        print("测试用例")


if __name__ == '__main__':
    pytest.main()
