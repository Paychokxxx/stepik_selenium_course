import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_class_name("trollface").click()

first_window = browser.window_handles[0]
new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_field = browser.find_element_by_id("answer")
input_field.send_keys(y)

browser.find_element_by_class_name("btn-primary").click()
