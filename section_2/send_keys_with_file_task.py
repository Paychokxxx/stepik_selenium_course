import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements_by_class_name("form-control")
for element in elements:
    element.send_keys("Мой ответ")

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

element = browser.find_element_by_id("file")
element.send_keys(file_path)

browser.find_element_by_tag_name("button").click()