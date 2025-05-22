#全局fixture管理
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from capabilities import get_capabilities, appium_server_url


@pytest.fixture(scope='function')
def driver():
    """为每个测试函数创建 Appium 会话"""
    caps = get_capabilities()
    driver = webdriver.Remote(
        command_executor=appium_server_url,
        options=UiAutomator2Options().load_capabilities(caps)
    )
    yield driver
    driver.quit()



