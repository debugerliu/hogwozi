# from appium import webdriver
# import time
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'  # 或者IOS
# desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机设备名或者型号
# desired_caps['platformVersion'] = '7.1'  # 安卓系统版本
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = 'com.android.settings.Settings'
# desired_caps['automationName'] = 'uiautomator1'
# # desired_caps["ignoreHiddenApiPolicyError"] = True
# # 同时连接模拟器和真机时，必须有udid,里边的值写真机的adb devices
# # desired_caps['udid']='d32ec644'
# # 如果手机还未安装APP，则需要写入路径
# # desired_caps['app']=r'C:\Users\admin\Desktop\kaoyan3.1.0.apk'
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(2)


import time

from appium import webdriver

desired_caps = {'platformName': 'Android',
                'platformVersion': '12.0',
                'deviceName': '83386b34',
                'appPackage': 'com.android.settings',
                'appActivity': 'com.android.settings.MainSettings',
                'automationName': 'uiautomator2',
                'ignoreHiddenApiPolicyError': True
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.quit()

# from appium import webdriver
# import time
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'  # 或者IOS
# desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机设备名或者型号
# desired_caps['platformVersion'] = '7.0'  # 安卓系统版本
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = 'com.android.settings.Settings'
# desired_caps['automationName'] = 'uiautomator1'
# # 同时连接模拟器和真机时，必须有udid,里边的值写真机的adb devices
# # desired_caps['udid']='d32ec644'
# # 如果手机还未安装APP，则需要写入路径
# # desired_caps['app']=r'C:\Users\admin\Desktop\kaoyan3.1.0.apk'
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(2)