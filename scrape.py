from lxml import html
import requests

page = open("Disease.html")
tree = html.fromstring(page.content)

#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
#print(buyers)
#print(prices)

#page = requests.get('http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html')
#tree = html.fromstring(page.content)
#table//MsoTableWeb3
tr = tree.xpath('//table[@class="MsoTableWeb3"]//tbody//tr/text()')

print(tr)