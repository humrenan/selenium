from selenium.webdriver import Firefox
from time import sleep



browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser.get(url)
sleep(3)


def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


sleep(2)

estrutura = {
    'nome': 'renan',
    'email': 'rerere@bug.com',
    'senha': 'qwerty',
    'telefone': '08006735454'
}
preenche_form(browser, **estrutura)






url_parseada = urlparse(browser.current_url)

sleep(2)

texto_resultado = browser.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)


assert dic_result == estrutura

browser.quit()
