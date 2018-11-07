from selenium import webdriver
import time
user=''
passwd=''
driver=webdriver.Chrome()
driver.get("https://www.hostloc.com/forum.php")
driver.find_element_by_xpath("//input[@id='ls_username']").send_keys(user)
driver.find_element_by_xpath("//input[@id='ls_password']").send_keys(passwd)
driver.find_element_by_xpath("//button[@class='pn vm']").click()
driver.get("https://www.hostloc.com/misc.php?mod=ranklist&type=member&view=credit")
all=driver.find_elements_by_xpath("//DIV[@class='xld xlda hasrank']/dl/dd[@class='m avt']/a")
for i in range(len(all)):
    url=all[i].get_attribute('href')
    driver.get(url)
    time.sleep(2)
    driver.back()
    all=driver.find_elements_by_xpath("//DIV[@class='xld xlda hasrank']/dl/dd[@class='m avt']/a")
