from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.smartprix.com/mobiles")
time.sleep(1)

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "sm-load-more").click()
time.sleep(2)

old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.find_element(By.CLASS_NAME, "sm-load-more").click()
    time.sleep(1)

    new_height=driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    old_height=new_height


# html=driver.page_source
# with open('smartprix.html', 'w', encoding='utf-8') as f:
#     f.write(html)