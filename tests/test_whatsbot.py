from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

contacts_wa = []

print('Open your whatsapp and scan the QR code will appear in your screen!\n')
time.sleep(1)
contacts = input('Group or Contact you want to send the message (separete each one eith ",":\n->')
contacts = contacts.split(',')

for ctt in contacts:
    contacts_wa.append(ctt)

message_before = input('Message before the name: ')
message_after = input('Message after the name: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') 
time.sleep(15)

def search_contact(contact):
    field_research = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    field_research.click()
    field_research.send_keys(contact)
    field_research.send_keys(Keys.ENTER)

def send_message(message_before,message_after):
    field_msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    field_msg[1].click()
    time.sleep(3)
    field_msg[1].send_keys(f'{str(message_before)} {str(contact)} {str(message_after)}')
    field_msg[1].send_keys(Keys.ENTER)

for contact in contacts_wa:
    search_contact(contact)
    send_message(message_before,message_after)       
    time.sleep(1)