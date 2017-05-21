Selenium IDE
============

Instalando o Selenium IDE
-------------------------

Lembrando-se que o somente o navegador **Firefox** possui a opçao de usar o `Selenium IDE`_ 
como um `add-on`_, uma vez instalado, você terá uma entrada no menu de **Ferramentas** para 
iniciar o `Selenium IDE`_. Uma vez iniciado, uma nova janela se abrirá onde você poderá 
entao gravar suas ações no Firefox.

![Janela do Selenium IDE](https://github.com/CastalioPodcast/playground/blob/master/episode101/selenium_ide.png)

**NOTA**: Nao se esqueça de pressionar o botão de gravar para iniciar ou reproduzir a gravação.

A interface do `Selenium IDE`_ te permite criar um ou vários testes, reproduzí-lo(s) ou ate mesmo exportá-lo(s) para outras linguagens de programação, como o exemplo abaixo em **Python**::

    # -*- coding: utf-8 -*-
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import NoAlertPresentException
    import unittest, time, re

    class TestCastalio(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "http://castalio.info/"
            self.verificationErrors = []
            self.accept_next_alert = True

        def test_castalio(self):
            driver = self.driver
            driver.get("http://castalio.info/")
            driver.find_element_by_id("tipue_search_input").send_keys("6 anos")
            driver.find_element_by_id("tipue_search_input").send_keys(Keys.ENTER)
            driver.find_element_by_link_text(u"Episódio 88: Episódio Especial de 6 Anos").click()
            self.assertEqual(u"Episódio 88: Episódio Especial de 6 Anos - Castálio Podcast", driver.title)

        def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e: return False
            return True

        def is_alert_present(self):
            try: self.driver.switch_to_alert()
            except NoAlertPresentException as e: return False
            return True

        def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally: self.accept_next_alert = True

        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()



Selenium via Python
===================

Instalando as dependências
--------------------------

Primeiro garanta que o ``chromedriver`` esta instalado em seu sistema, por
exemplo, no Fedora::

    sudo dnf install chromedriver

Em seguida instale o selenium utilizando o pip::

    pip install selenium

Depois disso inicie uma sessão interativa do Python e comece a brincar::


    from selenium import webdriver

    # Create a browser and open a website
    browser = webdriver.Chrome()
    browser.get('http://castalio.info')

    # Find the search input and search for the episode
    browser.find_element_by_id('tipue_search_input')
    element = browser.find_element_by_id('tipue_search_input')
    element.send_keys('6 anos')
    element.send_keys(webdriver.common.keys.Keys.RETURN)

    # Find the proper result link by either the entire or partial link text and
    # click on the link
    element = browser.find_element_by_link_text('Episódio 88: Episódio Especial de 6 Anos')
    element = browser.find_element_by_partial_link_text('6 Anos')
    element.click()

    # Check the browser shows the proper page title
    browser.title

    browser.quit()

.. Links:
.. _Selenium IDE: http://docs.seleniumhq.org/projects/ide/
.. _add-on: https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/
