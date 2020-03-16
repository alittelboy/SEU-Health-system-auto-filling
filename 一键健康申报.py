#使用前，请安装Firefox和geckodriver，后者请放在path系统路径
#author:
#https://github.com/alittelboy/SEU-Health-system-auto-filling
from selenium import webdriver
import time

url = "https://newids.seu.edu.cn/authserver/login?service=http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do"
with open("user.ini",'r',encoding='gbk') as f1:
    ini = f1.readlines()

#用文本文件"user.ini"设定用户名和密码
user = ini[0]
psw = ini[1]

driver = webdriver.Firefox()
#driver.minimize_window()
driver.get(url)
time.sleep(7)

user_input = driver.find_element_by_xpath('//*[@id="username"]')
psw_input = driver.find_element_by_xpath('//*[@id="password"]')
user_input.send_keys(user)
psw_input.send_keys(psw)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[4]/button').click()
time.sleep(20)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/button[1]').click()
time.sleep(7)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/button').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
time.sleep(5)
#driver.close()
