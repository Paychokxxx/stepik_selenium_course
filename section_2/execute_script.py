from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
assert True

# selenium.common.exceptions.WebDriverException: Message: unknown error:
# Element <button type="submit" class="btn btn-default"
# style="margin-bottom: 1000px;">...</button> is not clickable at
# point (87, 420). Other element would receive the click: <p>...</p>

# "return arguments[0].scrollIntoView(true);"


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


browser.execute_script("window.scrollBy(0, 100);")
