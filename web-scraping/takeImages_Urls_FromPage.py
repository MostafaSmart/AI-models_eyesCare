from selenium import webdriver
from selenium.webdriver.common.by import By
from pyautogui import hotkey
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clickFromJS(div_count,driver):
    
    script = f"""
    const button = document.evaluate('//*[@id="browsePageContainer"]/div/div[1]/div[4]/ul/div[{div_count}]/div[2]/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    button.click();
 
    
"""
    driver.execute_script(script)



driver = webdriver.Chrome()
driver.get("https://universe.roboflow.com/project-qhjkw/eyedisease-3tnz0/browse?queryText=class%3AUv&pageSize=100&startingIndex=200&browseQuery=true")
wait = WebDriverWait(driver, 10)
time.sleep(5)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.far.fa-list-ul")))

button = driver.find_element(By.CSS_SELECTOR, "button.far.fa-list-ul")

button.click()

time.sleep(5)


urls = []
for i in range(1,100):
    clickFromJS(i,driver)
    time.sleep(1)
    
    img_element = driver.find_element(By.CSS_SELECTOR, "img.h-full.transform.object-contain")
    image_source = img_element.get_attribute("src")
    urls.append(image_source)
    close = driver.find_element(By.CSS_SELECTOR, "button.absolute.-right-12.-top-0")
    close.click()
    print(i)




with open('EyeDisease_Dedaction/Uv.txt', 'a') as file:
    for url in urls:
        file.write(url + '\n')  
time.sleep(5)


