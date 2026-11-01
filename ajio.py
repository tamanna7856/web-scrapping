from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://scrapingsandbox.com/infinite-scroll")

old_height = driver.execute_script(
    "return document.body.scrollHeight"
)

counter = 1


while True:

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight)"
    )

    time.sleep(2)

    new_height = driver.execute_script(
        "return document.body.scrollHeight"
    )

    print(counter)
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height
    counter += 1

html=driver.page_source
with open('infinite_scroll.html', 'w', encoding='utf-8') as f:
    f.write(html)