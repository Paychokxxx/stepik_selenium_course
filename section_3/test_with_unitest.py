from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector("div.first_block .first").send_keys("Text")

        browser.find_element_by_css_selector("div.first_block .second").send_keys("Text")

        browser.find_element_by_css_selector("div.first_block .third").send_keys("Text")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(
            "div.first_block .first").send_keys("Text")

        browser.find_element_by_css_selector(
            "div.first_block .second").send_keys("Text")

        browser.find_element_by_css_selector(
            "div.first_block .third").send_keys("Text")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            "Поздравляем! Вы успешно зарегистировались!", welcome_text)


if __name__ == "__main__":
    unittest.main()
