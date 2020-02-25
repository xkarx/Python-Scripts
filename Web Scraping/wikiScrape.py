# This script scrapes the headings,links and tables from a given wikipedia link

# Before importing, open the terminal and install the packages
# pip install --user bs4
# python -m pip install --user requests
# python -m pip install --user lxml


# importing the required libraries

# Beutiful Soup is used for extracting data from the webpage, documentation available on https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import bs4

# requests is used dor fetching URL's documentation available on https://requests.readthedocs.io/en/master/
import requests

# creating and object of type requests, used for making a request
res = requests.get('https://en.wikipedia.org/wiki/Web_scraping')
# print(type(res)) #prints res typle
# print(res.text)  #prints the contents of the webpage in html format

soup = bs4.BeautifulSoup(res.text, 'lxml')  # taking res.text and converting it in lxml format, lxml is a parser that allows for easy handling of XML and HTML files
# print(type(soup))
# print(soup.prettify())

# print(soup.select('.mw-headline')) #prints along with html tags

# prints the headlines
for i in soup.select('.mw-headline'):
    print(i.text)

# prints all links
for link in soup.find_all('a', href=True):
    if link['href'][0] == '#':
        pass
    elif link['href'][0] == '/':
        pass
    else:
        print(link['href'])

# try this
# elif link['href'][0] == './':
# new_link = link['href'][0].replace('./', ' ') + link['href']


res = requests.get('https://en.wikipedia.org/wiki/List_of_island_countries')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# for scraping tables
all_tables = soup.find_all('table')
print(all_tables)

right_table = soup.find('table', class_='wikitable sortable jquery-tablesorter')
print(right_table)

table_links = right_table.findAll('a')  #.find_all('a', href=True)
print(table_links)

islands = []
for links in table_links:
    islands.append(link.get('title'))

print(islands)


