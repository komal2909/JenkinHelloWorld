from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Users\Sanjay\PycharmProjects\pythonProject\Driver\chromedriver.exe")
browser = webdriver.Chrome(service = service_obj)
browser.get("https://shopping.google.com/")
browser.maximize_window()
search = browser.find_element(By.NAME, "q").send_keys("Apple phones")
ActionChains(browser)\
    .send_keys(Keys.ENTER)\
    .perform()
browser.execute_script("window.scrollBy(0,200)")
browser.find_element(By.XPATH, "//span[contains(text(), 'Accept all')]").click()
browser.implicitly_wait(10)
#browser.find_element(By.CLASS_NAME,"nZbkuc")
browser.find_element(By.XPATH,"//div[@class='sh-dr__restricts']/div[2]//div[@class='EQ4p8c CyAbL']//span[@class='nZbkuc']").click()
print ("hello")
