from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
###https://www.discuvver.com/
driver.get('https://sleepyti.me/')
title = driver.title
print(title)
assert title == 'sleepyti.me bedtime calculator'
driver.close()
