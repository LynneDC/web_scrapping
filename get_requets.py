import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Debugging: print out the first 500 characters of the HTML content
print(soup.prettify()[:500])

s = soup.find('div', class_='entry-content')
if s is not None:
    content = s.find_all('p')
    for p in content:
        print(p.get_text())
else:
    print("The specified div with class 'entry-content' was not found.")
# content = s.find_all('p')

# print(content)

# import requests
# from bs4 import BeautifulSoup

# # making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# # check status code for response received
# # success code - 200
# print(r)

# # parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')

# s = soup.find('div', class_='entry-content')
# content = s.find_all('p')

# print(content)