from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
FIRSTNAME = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
FIRSTNAME.send_keys("Ivan")
LASTNAME = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
LASTNAME.send_keys("Petrov")
EMAIL = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
EMAIL.send_keys("ivan.petrov@mail.ru")

# Отправляем заполненную форму
SUBMIT = browser.find_element_by_xpath("//button[text()='Отправить']")
SUBMIT.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
browser.quit()