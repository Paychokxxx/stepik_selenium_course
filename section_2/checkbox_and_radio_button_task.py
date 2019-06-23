import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_field = browser.find_element_by_id("answer")
input_field.send_keys(y)

browser.find_element_by_id("robotCheckbox").click()

browser.find_element_by_id("robotsRule").click()


browser.find_element_by_class_name("btn-default").click()