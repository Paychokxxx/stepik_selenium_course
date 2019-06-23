import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


treasure_image = browser.find_element_by_id("treasure")

x_value = treasure_image.get_attribute("valuex")

y = calc(x_value)

browser.find_element_by_id("answer").send_keys(y)

browser.find_element_by_id("robotCheckbox").click()

browser.find_element_by_id("robotsRule").click()


browser.find_element_by_class_name("btn-default").click()