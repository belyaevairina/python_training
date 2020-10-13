from selenium import webdriver
import time
import math

#функция для y = calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент-картинку, который является изображением сундука с сокровищами.
    # Взять у этого элемента значение атрибута valuex, которое является значением x
    # и высчитываем мат.функцию от х
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Вводим полученное значение в поле для ввода
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


