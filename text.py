import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

print('starting running...')
url = 'https://www2.aneel.gov.br/aplicacoes_liferay/editais_transmissao/edital_transmissao.cfm'

response = requests.get(url)
html_content = response.content

print(response.status_code)

soup=BeautifulSoup(html_content, 'html.parser')
first_table=soup.find('table', class_='table table-bordered table-striped')
content=[]
for row in first_table.find_all('tr'):
    for element in row.find_all('td'):
        if element.get == ('valign') == 'top':
            break
        content.append(str(element))

content = ''.join(content)

content=[]

filename= 'content.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(content)

print('completed')