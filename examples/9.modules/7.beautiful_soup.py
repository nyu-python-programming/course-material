#import the urllib request module
import urllib.request
from bs4 import BeautifulSoup

#ask a web server for the contents of a web page
f = urllib.request.urlopen('https://knowledge.kitchen')

#read the response that the web server has sent to us
page_data = f.read() # get a string that contains the web page html code

#print that data out
# print(page_data)

#...and you want to make some sense of that code... use Beautiful soup to parse it
soup = BeautifulSoup(page_data)

#... now you can do things like get the contents of HTML  tags...
print("The title of the document is", soup.title.string)

#... or find the contents of all paragraphs, for example ...

# loop through each paragraph
for p in soup.find_all('p'):
    # print out the text of each paragraph
    print(p.get_text())

#... or get all the text without the HTML code...
# print(soup.get_text())