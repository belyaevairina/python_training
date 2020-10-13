import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    element = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
    element.send_keys('Name')
    element = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
    element.send_keys('Fam')
    element = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
    element.send_keys('E-mail')
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
    time.sleep(1)
    assert "Congratulations! You have successfully registered!" == browser.find_element_by_tag_name("h1").text
finally:
    time.sleep(5)
    browser.quit()

