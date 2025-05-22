import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    deviceName='AINOTEA224042300042',  # adb devices获取的设备名
    automationName='UiAutomator2',  # 自动化框架名称
    appPackage='com.aispeech.tablet',  # app包名
    appActivity='com.aispeech.tablet.MainActivity',  # app启动页
    unlockType="pin",#pin 数字密码  password 字母+数字  pattern 九宫格
    unlockKey='0000',
    noReset=True,  # 是否重置app
    unicodeKeyboard=True,  # 是否支持中文输入
    resetKeyboard=True,  # 是否支持中文输入
)

app_sever_url = 'http://localhost:4723'  # appium服务器地址，本地启动的话就是默认地址


@pytest.fixture(scope='function')
def driver():
    options = UiAutomator2Options()
    options.load_capabilities(capabilities)
    driver = webdriver.Remote(app_sever_url, options=options)
    yield driver
    driver.quit()


def test_find_notes(driver):
    notes = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="笔记"]')
    notes.click()


if __name__ == '__main__':
    pytest.main()
