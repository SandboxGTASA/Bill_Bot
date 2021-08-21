from googlesearch import search
counter = 0

web_search = input('What do you want to search: ')
number_of_searches = input('how many URLs do you want to receive? ')

if number_of_searches.isdigit():
      number_of_searches = int(number_of_searches)
      for url in search(f'"{web_search}" Google', stop=number_of_searches):
            counter += 1
            print(f'{counter}º URL: {url}')
else:
      print('The reply is not a number')