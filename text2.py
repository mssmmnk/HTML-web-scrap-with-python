

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://www2.aneel.gov.br/aplicacoes_liferay/editais_transmissao/edital_transmissao.cfm')

list_states = []
tbodies = driver.execute_script("return document.getElementsByTagName('tbody');")

for tbody in tbodies:
    trs = tbody.find_elements_by_tag_name('tr')
    for tr in trs:
        tr_data = []
        tds = tr.find_elements_by_tag_name('td')
        for td in tds:
            tr_data.append(td.text)
        list_states.append(tr_data)

for states in list_states:
    print(states)

driver.quit()




