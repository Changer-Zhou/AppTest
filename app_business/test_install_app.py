#Coding:utf-8
#Author:MuTou<****@163.com>
#Time:2019/7/3 0003 上午 9:18
#File:test_install_app.py
#Project_Name:
#Content:文件说明
from AppTest_Day_02.app_common.get_session import get_Session
from AppTest_Day_02.get_apk_package import get_packageName
import time
class install_business(get_Session):
    #实现其他的app安装（两种方式：一种直接建立连接时传入app参数，
    # 一种启动模拟器或者设备组中任意一个程序，然后再通过调用其对应的api进行安装）
    def  install_apk(self,install_apk_path):
        get_dir=self.return_driver()
        get_dir.install_app(install_apk_path)
        #关闭当前运行的app
        get_dir.close_app()
        #如果是当前建立会话连接时将对应的app进行关闭后需要重启打开则可以使用start_activity
        #对应的方法是launch_app是与close_app函数相对应
        time.sleep(5)
        get_dir.launch_app()
        #关闭驱动器对象
        #get_dir.close()
        #print(get_dir.current_package)
        #print(get_dir.current_activity)
        #get_dir.start_activity(self.desired_cap['appPackage'],self.desired_cap['appActivity'])
        #pk=get_packageName(install_apk_path)
        #get_dir.start_activity(pk.get_appPackageName(),pk.get_appActivityName())


test=install_business("Android","5.1.1","127.0.0.1:62001",server_port=5656,appPackage="com.baidu.yuedu",appActivity=".base.ui.MainActivity")
test.install_apk("e:\\jinritoutiao.apk")
