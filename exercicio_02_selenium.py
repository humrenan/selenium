from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
sleep(2)
tag_h1 = browser.find_elements_by_tag_name('h1')
ancora = browser.find_element_by_id('ancora')

mensagem = ''

while 'Você ganhou' not in mensagem:
    ancora.click()
    mensagem = browser.find_elements_by_tag_name('p')[-1].text

print(mensagem)
browser.quit()
