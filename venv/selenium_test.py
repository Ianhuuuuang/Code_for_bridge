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
time.sleep(30)
# Xpath变量
str1 = "(//div[contains(.,'S245')])[10]"  # 勾选桥梁使用
# 桥梁名称
bridgeName = '砂礓河大桥'
# 切换当前网页框架
browser.switch_to.frame('myframe')
# 按桥梁名称搜索
browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/span[1]/input[1]").send_keys(bridgeName)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/span[1]/span/a").click()
WebDriverWait(browser, 20, 0.5).until(ec.elements_to_be_clickable((By.XPATH, str1))).click()
# wait.until(ExceptedConditions.elementToBeClickable(By.xpath(
#     "/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div/input")))
# browser.find_element_by_xpath(
#     "/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div/input").click()
# browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/a[9]/span/span[1]").click()
