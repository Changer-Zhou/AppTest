#Coding:utf-8
#Author:MuTou<****@163.com>
#Time:2019/7/3 0003 下午 2:28
#File:KeyCode_App.py
#Project_Name:
#Content:
from AppTest_Day_02.app_common.get_session import get_Session
import time
class search_text(get_Session):
    def  click_cancle(self):
        get_driver=self.return_driver()
        get_driver.close_app()
        time.sleep(5)
        #get_driver.find_element_by_android_uiautomator(
        #    'resourceId("com.baidu.yuedu:id/normalUpgradeBtn").fromParent(text("取消"))').click()
        #time.sleep(10)
        #get_driver.find_element_by_id("com.baidu.yuedu:id/tab_search").click()
        #time.sleep(10)
        #get_driver.find_element_by_id("com.baidu.yuedu:id/full_text_search_bar_input").send_keys("长安十二时辰")
        get_driver.long_press_keycode(25)

#resetKeyboard与unicodeKeyboard通常联合使用
sa=search_text("Android","5.1.1","127.0.0.1:62001",server_port=5656,appPackage="com.baidu.yuedu",appActivity=".base.ui.MainActivity",unicodeKeyboard=True,resetKeyboard=True)
sa.click_cancle()



















