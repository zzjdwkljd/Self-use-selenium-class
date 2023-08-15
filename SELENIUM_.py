# -*- coding: utf-8 -*-
'''

selenium 4.10
python 3.10

'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
    NoSuchWindowException,
    ElementNotInteractableException,
    WebDriverException,
)


class Locator:
    LOCATORS = {
        'CLASS_NAME':        By.CLASS_NAME,
        'XPATH':             By.XPATH,
        'ID':                By.ID,
        'NAME':              By.NAME,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'TAG_NAME':          By.TAG_NAME,
        'LINK_TEXT':         By.LINK_TEXT,
        'CSS_SELECTOR':      By.CSS_SELECTOR,
    }
    EC_ = {
        'element_to_be_clickable':       'element_to_be_clickable',
        'visibility_of':                 'visibility_of',
        'presence_of_element_located':   'presence_of_element_located',
        'visibility_of_element_located': 'visibility_of_element_located',
        'presence_of_all_elements_located': 'presence_of_all_elements_located',
    }


class SELENIUM():
    # 初始化,防检测
    def __init__(self, argument='Y'):
        self.option = Options()
        self.option.page_load_strategy = 'none'
        self.option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.option.add_experimental_option('useAutomationExtension', False)
        self.option.add_argument('disable-blink-features')
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        if argument == 'Y':
            self.option.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.option)

    # 访问网址
    def get_url(self, url: str) -> str:
        try:
            self.driver.maximize_window()
            self.driver.get(url)
        except Exception as e:
            raise Exception(f"get_url()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 获取当前窗口句柄
    def get_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except Exception as e:
            raise Exception(f"get_window()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 获取cookie
    def get_cookies(self, url: str = '') -> str:
        try:
            if url:
                self.get_url(url)
            return self.driver.get_cookies()
        except Exception as e:
            raise Exception(f"get_cookies()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 传入cookie
    def set_cookies(self, c):
        try:
            for cookie in c:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        except Exception as e:
            raise Exception(f"set_cookies()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 结束 selenium
    def close_selenium(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise Exception(f"close_selenium()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 单击元素[ 模拟鼠标 ]
    def click_element(self, element):
        try:
            ActionChains(self.driver).move_to_element(element).click(element).perform()
        except Exception as e:
            raise Exception(f"click_element()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 单击键盘
    def click_key(self, key: str) -> str:
        try:
            ActionChains(self.driver).key_down(key).perform()
        except Exception as e:
            raise Exception(f"click_key()发生了错误: {e}")

    # 拖动元素
    def move_element(self, element, x=0, y=0, speed=50, release=False):
        try:
            if not element.is_displayed():
                raise ValueError("元素不可见, 无法移动")
            actions = ActionChains(self.driver)
            if element:
                actions.click_and_hold(on_element=element)
            if x and y:
                actions.move_by_offset(xoffset=x, yoffset=y, duration=speed)
            if release:
                actions.release()
            actions.perform()
        except Exception as e:
            raise Exception(f"move_element()发生了错误: {e}")

    # 查找单个元素
    def finds_element(self, **kwargs):
        try:
            locator = None
            way = None
            wait = WebDriverWait(self.driver, kwargs["t"] if kwargs.get("t", False) else 10)
            for k, v in kwargs.items():
                if Locator.LOCATORS.get(k, None):
                    locator = (Locator.LOCATORS.get(k, None), v)
                if Locator.EC_.get(k, None):
                    way = Locator.EC_.get(k, None)
            if locator and way:
                if way == 'element_to_be_clickable':
                    element = wait.until(EC.element_to_be_clickable(locator))
                elif way == 'visibility_of':
                    element = wait.until(EC.visibility_of(locator))
                elif way == 'presence_of_element_located':
                    element = wait.until(EC.presence_of_element_located(locator))
                elif way == 'visibility_of_element_located':
                    element = wait.until(EC.visibility_of_element_located(locator))
                elif way == 'presence_of_all_elements_located':
                    element = wait.until(EC.presence_of_all_elements_located(locator))
                else:
                    element = wait.until(EC.presence_of_element_located(locator))

                return element

            return False
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

        except Exception as e:
            raise Exception(f"finds_element()发生了错误: {e}")

    # 查找多个元素
    def finds_elements(self, **kwargs):
        try:
            for k, v in kwargs.items():
                if Locator.LOCATORS.get(k, False):
                    return self.driver.find_elements(Locator.LOCATORS.get(k), v)
            return False
        except Exception as e:
            raise Exception(f"finds_elements()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise

    # 截图
    def save_screenshot(self, n: str = 'error') -> str:
        try:
            self.driver.save_screenshot(f"{n}.png")
        except Exception as e:
            raise Exception(f"save_screenshot()发生了错误: {e}")
        except (
                                TimeoutException,
                                NoSuchElementException,
                                ElementClickInterceptedException,
                                StaleElementReferenceException,
                                TimeoutException,
                                NoSuchWindowException,
                                ElementNotInteractableException,
                                WebDriverException,
        ):
            raise
