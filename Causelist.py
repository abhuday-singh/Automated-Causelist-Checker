import selenium
from selenium import webdriver
chromedriver=r"C:\Users\ABHUDAY SINGH\Desktop\Web Automation\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chromedriver)
driver.get("http://www.allahabadhighcourt.in/causelist")
a=driver.find_element_by_xpath("/html/body/h4[2]")
a.click()
b=driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[3]/input")
b.submit()
#c=driver.find_element_by_xpath("/html/body/form/table[1]/tbody/tr/td[1]/select")
#c.click()
d=driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[3]/input")
d.submit()

