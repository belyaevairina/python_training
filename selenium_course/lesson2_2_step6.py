from selenium import webdriver
import time
import math

#функция для y = calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для переменной х и высчитываем мат.функцию от х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # проскролить страницу вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    # Отмечаем чекбокс
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # отмечаем радиобаттон
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    # нажимаем на кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


