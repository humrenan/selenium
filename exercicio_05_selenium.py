from selenium.webdriver import Firefox
from time import sleep



browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_05.html'
browser.get(url)
sleep(3)


def preenche():
    nomes = browser.find_elements_by_css_selector('input[name="nome"]')
    nome = 'renan'
    senhas = browser.find_elements_by_css_selector('input[name="senha"]')
    senha = 'xxx'
    nomes[0].send_keys(nome)
    senhas[0].send_keys(senha)

    nomes[1].send_keys(nome)
    senhas[1].send_keys(senha)

    nomes[2].send_keys(nome)
    senhas[2].send_keys(senha)


    nomes[3].send_keys(nome)
    senhas[3].send_keys(senha)



preenche()

preenche()
envia = browser.find_element_by_css_selector('input[name="l0c1"]')
envia.click()
sleep(5)
preenche()
envia = browser.find_element_by_css_selector('input[name="l1c0"]')
envia.click()
sleep(5)
preenche()
envia = browser.find_element_by_css_selector('input[name="l1c1"]')
envia.click()
sleep(5)

browser.quit()
