from selenium.webdriver import Firefox
from time import sleep



browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser.get(url)
sleep(3)

def find_by_href(browser, link):
    grid = browser.find_element_by_id('grid')
    main = grid.find_element_by_id('main')
    li = main.find_element_by_tag_name('li')
    ancora = li.find_elements_by_tag_name('a')

    for elemento in ancora:
        if link in elemento.get_attribute('href'):
            return elemento
            elemento[0].click()
elementos_a = find_by_href(browser, 'page_' ).click()
sleep(3)
elementos_a = find_by_href(browser, 'page_2' ).click()
sleep(30)
elementos_a = find_by_href(browser, 'page_3' ).click()
sleep(3)
elementos_a = find_by_href(browser, 'page_4' ).click()
sleep(3)
browser.refresh()
sleep(3)
browser.quit()
