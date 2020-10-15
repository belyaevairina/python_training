from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

#функция для y = calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #нажимаем на кнопку
    browser.find_element_by_css_selector("button.trollface").click()

    #Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #решить капчу для роботов
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Вводим полученное значение в поле для ввода
    browser.find_element_by_id("answer").send_keys(str(y))

    # нажимаем на кнопку submit
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



