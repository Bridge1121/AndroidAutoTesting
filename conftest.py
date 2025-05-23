#全局fixture管理
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from capabilities import get_capabilities, appium_server_url


#一个用例文件共用一个driver
@pytest.fixture(scope='module')
def driver():
    """为每个测试文件创建 Appium 会话"""
    caps = get_capabilities()
    driver = webdriver.Remote(
        command_executor=appium_server_url,
        options=UiAutomator2Options().load_capabilities(caps)
    )
    yield driver
    driver.quit()



