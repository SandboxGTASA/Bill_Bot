from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import time
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os

print(
    '\nOptions Menu'
    '\n[1] Talk to Bill bot'
    '\n[2] Web Search with Bot'
    '\n[3] Send Message on WhatsApp with Bot'
    '\n[4] Finish the Program\n'
    )

while True:

    choice_menu = input('\nEnter the chosen number: ')

    if not choice_menu.isdigit():
        print('Error, Your input is not a number.\n')
        time.sleep(1)
        break

    elif choice_menu.isdigit():
        choice_menu = int(choice_menu)
        if choice_menu == 1:

            bot = ChatBot('Bot Bill')
            trainer = ChatterBotCorpusTrainer(bot)
            trainer.train("chatterbot.corpus.english.conversations")

            print('\nTo finish type: "ok".\n')
            time.sleep(1)
            print("Bill: Hello, i'm Bill the Bot!")
            while True:
                quest = input('You: ').lower()
                response = bot.get_response(quest)
                print(f'Bill: {response}')
                if quest == 'ok':
                    print('Bill: See you soon! ;)')
                    os.system("cls") 
                    break
                
        
        elif choice_menu == 2:
            counter = 0
            web_search = input('What do you want to search: ')
            number_of_searches = input('how many URLs do you want to receive? ')

            if number_of_searches.isdigit():
                number_of_searches = int(number_of_searches)
                for url in search(f'"{web_search}" Google', stop=number_of_searches):
                        counter += 1
                        print(f'{counter}º URL: {url}')
                clear_term = input('\nClear Terminal? [Y]es / [N]o: ').upper()
                if clear_term == 'Y':
                    os.system("cls") 
            else:
                print('The reply is not a number')
                break
        elif choice_menu == 3:
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
            os.system("cls") 
        elif choice_menu == 4:
            print(
                'Thanks to use my program! ;)'
                '\nSubriscribe on my channel on Ytb: Assalim Coder')
            break