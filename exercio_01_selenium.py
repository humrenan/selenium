from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)
sleep(3)
tag_h1 = browser.find_elements_by_tag_name('h1')
elementosp = browser.find_elements_by_tag_name('p')


atributos = []
textos_p = []
for textos in elementosp:
	atributos.append(textos.get_attribute('atributo'))
	textos_p.append(textos.text)

#cria o dicionario com 'atributo' e 'texto'
dicionario = {}
it = 0
for dic0 in textos_p:
	dicionario[atributos[it]] = dic0
	it = it + 1

#dicionario h1
h1 = {'h1': dicionario}
print(h1)

browser.quit()
