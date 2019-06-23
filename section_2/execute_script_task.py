import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_value = int(browser.find_element_by_id("input_value").text)

y = calc(x_value)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element_by_id("answer").send_keys(y)

browser.find_element_by_id("robotCheckbox").click()

browser.find_element_by_id("robotsRule").click()

browser.find_element_by_class_name("btn-default").click()
