#Coding:utf-8
#Author:MuTou<****@163.com>
#Time:2019/7/3 0003 上午 9:20
#File:get_session.py
#Project_Name:
#Content:文件说明
from appium import webdriver
import time
class get_Session():

    def __init__(self,platformName,platformVersion,deviceName,server_ip="127.0.0.1",server_port="4723",**kwargs):
        self.server_ip=server_ip
        self.server_port=server_port
        self.desired_cap = {
            "platformName": platformName,
            "platformVersion": platformVersion,
            "deviceName": deviceName,
        }
        for (key,value) in kwargs.items():
            self.desired_cap[key]=value
    def return_driver(self):
        get_driver = webdriver.Remote(command_executor="http://%s:%s/wd/hub"%(self.server_ip,self.server_port), desired_capabilities=self.desired_cap)
        return get_driver