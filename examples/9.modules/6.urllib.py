#import the urllib request module
import urllib.request

#ask the python web server for the home page data
f = urllib.request.urlopen('https://knowledge.kitchen')

#read the response that the web server has sent to us
page_data = f.read()

#print that data out
print(page_data)
