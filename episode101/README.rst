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
