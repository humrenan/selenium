from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads



browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_06.html'
browser.get(url)
sleep(3)

span = browser.find_element_by_css_selector('span').text
print(span)

form = browser.find_element_by_css_selector(f'.form-{span}')



def preenche():
    nome = 'renan'
    senha = 'xxx'

    inputs = {
        'nome': form.find_element_by_css_selector('[name="nome"]'),
        'senha': form.find_element_by_css_selector('[name="senha"]'),
        'enviar': form.find_element_by_css_selector('[type="submit"]')
    }

    inputs['nome'].send_keys(nome)
    inputs['senha'].send_keys(senha)
    inputs['enviar'].click()


for i in range(7):

    preenche()
    sleep(3)

    span = browser.find_element_by_css_selector('span').text
    form = browser.find_element_by_css_selector(f'.form-{span}')
