from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://127.0.0.1:5000/")

stock_field = driver.find_element_by_id("stock_name")
stock_field.clear()
start_date_field = driver.find_element_by_id("start_date")
start_date_field.clear()
end_date_field = driver.find_element_by_id("end_date")
end_date_field.clear()

stock_field.send_keys("msft")
start_date_field.send_keys("01/01/2017")
end_date_field.send_keys("01/01/2018")
stock_field.submit()

lists= driver.find_elements_by_class_name("stock_title")
list2 = driver.find_elements_by_class_name("current_stats")
list3 = driver.find_elements_by_class_name("report_buttons")
list4 = driver.find_elements_by_class_name("graph_frame")

lis = [lists,list2, list3, list4]
print("Found " + str(len(lists)))
print("Found " + str(len(list2)))
print("Found " + str(len(list3)))
print("Found " + str(len(list4)))

# iterate through each element and print the text that is
# name of the search
f = open("log.txt", 'w')
for lists in lis:
    for items in lists:
        f.write(items.get_attribute("innerHTML"))
