from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
message = input('Enter your message: ')
count = int(input('Enter the count: '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3uMse')

for i in range(count):
	msg_box.send_keys(message)
	button = driver.find_element_by_class_name('_1U1xa')
	button.click()


#im testing my new branch
