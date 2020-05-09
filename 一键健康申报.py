#使用前，请安装Firefox和geckodriver，后者请放在path系统路径
#author:
#https://github.com/alittelboy/SEU-Health-system-auto-filling
from selenium import webdriver
import time
print("正常")
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
driver.find_element_by_xpath('//*[@type="submit"]').click()
time.sleep(20)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/button[1]').click()#新增
time.sleep(7)
#体温 产生一个随机体温
temp = driver.find_element_by_xpath('//*[@placeholder="请输入当天晨检体温"]')
import random
#查资料得知正常体温用额温枪，在36.1℃到37℃之间
tm = random.randint(1,11)
tm = 36 + tm/10
temp.send_keys(format(tm,".1f"))#保留一位输出
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/button').click()#确认并提交
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()#确定
time.sleep(5)
#driver.close()
