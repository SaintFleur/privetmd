import requests
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

update_id = None
url = 'http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')

name_box = soup.find('table', attrs={'class': 'MsoTableWeb3'})
name = name_box.text.strip()
name = name[54:]
data =  list(name)
counter = 0
intermidiate = ''

for x in range(0, len(data)):
	if(data[x] == '\n'):
		counter = counter + 1
		if(counter == 4):
			intermidiate = intermidiate + '\n'
			counter = 0
		elif(counter == 3 and data[x+1]!='\n'):
			intermidiate = intermidiate + ','
			counter = 0
		elif(counter==1 and data[x+1]!='\n'):
			counter = 0
			
	else:
		intermidiate = intermidiate + data[x]

with open('csvfile.csv','wb') as file:
    for line in intermidiate:
        file.write(line)
        