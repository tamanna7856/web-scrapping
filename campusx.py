from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Bing
driver.get("https://www.bing.com")

time.sleep(2)

# Find Bing search box
user_input = driver.find_element(By.ID, "sb_form_q")

# Click the search box
user_input.click()

# Type CampusX
user_input.send_keys("CampusX")

time.sleep(1)

# Press Enter
user_input.send_keys(Keys.ENTER)

# Wait for Bing results
time.sleep(2)

link=driver.find_element(By.XPATH, '//*[@id="b_results"]/li[1]/div[1]/a')
link.click()

time.sleep(3)

# ⭐ SWITCH TO THE NEW TAB
driver.switch_to.window(driver.window_handles[-1])

# Find Login button
link2 = driver.find_element(
    By.CLASS_NAME,
    "loginBtn"
)

# Click Login
link2.click()


time.sleep(3)

time.sleep(3)

input("Press Enter to close...")

# Keep browser open
input("Press Enter to close the browser...")

driver.quit()