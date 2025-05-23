# case/test_nodes_list.py

import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("笔记模块用例")
@allure.feature("笔记列表相关功能")
class TestNodes:
    @allure.story("查找笔记")
    def test_find_node(self, driver):
        #
        wait = WebDriverWait(driver, 5)
        notes = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="笔记"]'))
        )
        notes.click()
