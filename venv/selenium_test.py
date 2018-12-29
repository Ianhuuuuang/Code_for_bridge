from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get(r'http://124.207.182.50:8234/bdas3.0_js')
browser.find_element_by_name(r'UserName').clear()
browser.find_element_by_name(r'UserName').send_keys('sq')
browser.find_element_by_name(r'PASSWORD').clear()
browser.find_element_by_name(r'PASSWORD').send_keys('1234')
# 主题框Xpath
ThemeBox = '/html/body/div[1]/div/div[2]/div[5]/div/span/input[1]'
# 搜索框Xpath
SearchBox = '/html/body/div[2]/div/div/div/div[1]/span[1]/input[1]'
SearchClick = "/html/body/div[2]/div/div/div/div[1]/span[1]/span/a"
# Xpath变量
str1 = "(//div[contains(.,'S245')])[10]"  # 勾选桥梁使用
# 等待页面加载完成
WebDriverWait(browser, 60, 0.5).until(ec.element_to_be_clickable((By.XPATH, ThemeBox)))
# 桥梁名称
bridgeName = '砂礓河大桥'
# 按桥梁名称搜索
browser.switch_to.frame('myframe')
browser.find_element_by_xpath(SearchBox).send_keys(bridgeName)
browser.find_element_by_xpath(SearchClick).click()
# 等待搜索出的桥梁加载(上限20秒，每0.5扫描一次)
WebDriverWait(browser, 20, 0.5).until(ec.element_to_be_clickable((By.XPATH, str1)))
TarGits = browser.find_elements_by_xpath(str1)
TarGits[0].cilck()
