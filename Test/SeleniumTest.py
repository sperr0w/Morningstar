from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://tickets.fifa.com/requestSummary")
driver.implicitly_wait(120)

category_link = driver.find_element_by_class_name('category.CategoryStyleClass')
category_link.click()