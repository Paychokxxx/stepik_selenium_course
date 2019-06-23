import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_guest_should_see_login_link(browser, url):
    answer = str(math.log(int(time.time())))
    link = url
    browser.get(link)
    browser.find_element_by_css_selector(".textarea").send_keys(answer)

    browser.find_element_by_class_name("submit-submission").click()

    text_hint = browser.find_element_by_class_name("smart-hints__hint").text

    assert text_hint == "Correct!"




