from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

links = []
with open("links", "r") as f:
    for line in f:
        links.append(line.replace("\n", ""))

for link in links:
    url = link
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    wait = WebDriverWait(browser, 100)
    browser.get(url)
    while browser.title.find("50") != -1:
        browser.refresh()
        time.sleep(2)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Filtersstyled__Container-sc-126zqc3-0")))
    el = browser.find_elements(By.CLASS_NAME, "CitySelectionConfWrapper-sc-u8gbge-0")
    if len(el) > 0:
        el[0].find_elements(By.TAG_NAME, "button")[0].click()
        # el[0].click()
        time.sleep(2)
    el = browser.find_elements(By.CLASS_NAME, "Filtersstyled__FiltersCategoryBtnShow-sc-126zqc3-2")[0]
    el.click()

    a_links = []
    els = browser.find_elements(By.CLASS_NAME, "Filtersstyled__FiltersCategory-sc-126zqc3-1")[0].find_elements(By.TAG_NAME, "a")
    for i in els:
        a_links.append(i.get_attribute("href"))
    for i in a_links:    
        browser.get(i)
        while browser.title.find("50") != -1:
            browser.refresh()
            time.sleep(2)

        print(browser.find_elements(By.TAG_NAME, "h1"))
    browser.quit()

    


# Filtersstyled__Container-sc-126zqc3-0

# url = 'https://kobor.com'
# browser = webdriver.Chrome()
# browser.set_window_size(1920, 1080)
# wait = WebDriverWait(browser, 100)
# browser.get(url)

# while browser.title.find("50") != -1:
#     browser.refresh()
#     time.sleep(20)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "HeaderCatalog-sc-bsxz1t-0")))
# el = browser.find_elements(By.XPATH, "/html/body/div[9]/div/div/div[2]/div[2]/button[1]")
# if len(el):
#     el[0].click()

# time.sleep(2)

# el = browser.find_elements(By.CLASS_NAME, "HeaderCatalog-sc-bsxz1t-0")[1]
# el.click()

# time.sleep(2)

# cats = browser.find_elements(By.CLASS_NAME, "CatalogPopupstyled__CatalogPopupFirstList-sc-1pxt7f0-5")[0].find_elements(By.TAG_NAME, "a")
# cats = cats[:-1]
# for i in range(len(cats)):
#     print(cats[i].get_attribute("href"))
#     browser.execute_script("window.open('" + cats[i].get_attribute("href") + "')")
# # 
# browser.close()
# time.sleep(5)

# all_cats = browser.window_handles
# for i in all_cats:
#     browser.switch_to.window(i)
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Filtersstyled__Container-sc-126zqc3-0")))
#     print("sas")
#     time.sleep(5)



# # Filtersstyled__FiltersCategory-sc-126zqc3-1
# print("load?")