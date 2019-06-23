from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

number_one = browser.find_element_by_id("num1").text
number_two = browser.find_element_by_id("num2").text
sum_of_numbers = int(number_one) + int(number_two)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum_of_numbers))

browser.find_element_by_tag_name("button").click()