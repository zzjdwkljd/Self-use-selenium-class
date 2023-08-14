from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Locator:
    LOCATORS = {
        'CLASS_NAME':        By.CLASS_NAME,
        'XPATH':             By.XPATH,
        'ID':                By.ID,
        'NAME':              By.NAME,
        'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
        'TAG_NAME':          By.TAG_NAME,
        'LINK_TEXT':         By.LINK_TEXT,
    }
    EC_ = {
        'element_to_be_clickable':       'element_to_be_clickable',
        'visibility_of':                 'visibility_of',
        'presence_of_element_located':   'presence_of_element_located',
        'visibility_of_element_located': 'visibility_of_element_located'
    }

class SELENIUM():
    def __init__(self, argument='Y'):
        self.option = Options()
        self.option.page_load_strategy = 'none'
        self.option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.option.add_experimental_option('useAutomationExtension', False)
        self.option.add_argument('disable-blink-features')
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        if argument == 'Y':
            self.option.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.option)

    def get_url(self, u):
        try:
            self.driver.maximize_window()
            self.driver.get(u)
        except Exception as e:
            raise Exception(f"get_url()发生了错误: {e}")

    def get_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except Exception as e:
            raise Exception(f"get_window()发生了错误: {e}")

    def get_cookies(self, u=''):
        try:
            if u:
                self.get_url(u)
            return self.driver.get_cookies()
        except Exception as e:
            raise Exception(f"get_cookies()发生了错误: {e}")

    def set_cookies(self, c):
        try:
            for cookie in c:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        except Exception as e:
            raise Exception(f"set_cookies()发生了错误: {e}")

    def close_selenium(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise Exception(f"close_selenium()发生了错误: {e}")

    def click_element(self, element):
        try:
            ActionChains(self.driver).move_to_element(element).click(element).perform()
        except Exception as e:
            raise Exception(f"click_element()发生了错误: {e}")

    def click_key(self, key):
        try:
            key = str(key)
            ActionChains(self.driver).key_down(key).perform()
        except Exception as e:
            raise Exception(f"click_key()发生了错误: {e}")

    def move_element(self, element, x, y, speed=50, release=False):
        try:
            if not element.is_displayed():
                raise ValueError("元素不可见, 无法移动")
            actions = ActionChains(self.driver)
            actions.click_and_hold(on_element=element)
            actions.move_by_offset(xoffset=x, yoffset=y, duration=speed)
            if release:
                actions.release()
            actions.perform()
        except Exception as e:
            raise Exception(f"move_element()发生了错误: {e}")

    def finds_element(self, **kwargs):
        try:
            locator = ''
            way = ''
            wait = WebDriverWait(self.driver, kwargs["t"] if kwargs.get("t", False) else 10)

            for k, v in kwargs.items():
                if Locator.LOCATORS.get(k, False):
                    locator = (Locator.LOCATORS.get(k, False), v)
                way = Locator.EC_.get(k, False)
                if not locator:
                    return False
                if way:
                    if way == 'element_to_be_clickable':
                        element = wait.until(EC.element_to_be_clickable(locator))
                    elif way == 'visibility_of':
                        element = wait.until(EC.visibility_of(locator))
                    elif way == 'presence_of_element_located':
                        element = wait.until(EC.presence_of_element_located(locator))
                    elif way == 'visibility_of_element_located':
                        element = wait.until(EC.visibility_of_element_located(locator))
                    else:
                        element = wait.until(EC.presence_of_element_located(locator))
            else:
                locator = False

            if locator != False and way != False:
                return element
        except Exception as e:
            raise Exception(f"finds_element()发生了错误: {e}")

    def finds_elements(self, **kwargs):
        try:
            for k, v in kwargs.items():
                if Locator.LOCATORS.get(k, False):
                    return self.driver.find_elements(Locator.LOCATORS.get(k), v)
            return False
        except Exception as e:
            raise Exception(f"finds_elements()发生了错误: {e}")

