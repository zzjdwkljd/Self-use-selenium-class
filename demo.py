from SELENIUM_ import SELENIUM
import time
selenium = SELENIUM('N')
selenium.get_url('https://www.baidu.com/')
print(selenium.driver.title)

#查找元素
su = selenium.finds_element(XPATH='//span/input[@id="su"]', element_to_be_clickable=True)
kw = selenium.finds_element(XPATH='//span/input[@id="kw"]', element_to_be_clickable=True)
kw.send_keys("123456789") if kw else print('未找到该元素')
su.click() if su else print('未找到该元素')

# 查找多个元素
cf = selenium.finds_elements(XPATH='//span/input[@id="kw"]' )
if cf:
    for _ in range(10):
        cf[0].send_keys("\ue003")
    cf[0].send_keys("大帅哥")

    # 模拟鼠标点击
    selenium.click_element(su)
else:
    print(cf)


# 保存截图
time.sleep(3)
selenium.save_screenshot()

#关闭
selenium.close_selenium()
