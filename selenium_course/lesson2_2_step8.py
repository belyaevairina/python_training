from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем форму
    browser.find_element_by_name('firstname').send_keys("Ivan")
    browser.find_element_by_name('lastname').send_keys("Rybakov")
    browser.find_element_by_name('email').send_keys("email@mail.ru")

    # загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Для lesson2_2_step8.txt')           # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    # нажимаем кнопку
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


