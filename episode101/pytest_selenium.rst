
Demo: Testes de UI com Py.Test e selenium
------------------------------------------

Neste demo vamos escrever 2 testes para um formulário de cadastro de
notícias. No exemplo usaremos a aplicação do tutorial `What The Flask 
<http://bit.ly/whattheflask>`_ que  pode ser encontrada no  `Github  
<http://github.com/rochacbruno/wtf>`_ 

Alguns detalhes sobe o código.

- Precisamos garantir que a instância do browser seja fechada após o teste 
  e para isso usamos um gerenciador de contexto.
- O ideal é escrever o gerenciador de contexto em forma de `fixture` do pytest.
- O teste `negativo` testará um caso em que esperamos que ocorra um erro.
- O teste `positivo` testará um caso em que esperamos que a operação seja 
  completada com sucesso.
- É recomendado utilziar o seletor mais especifico sempre que possivel, neste 
  exemplo usaremos `xpath` para o botão e `id` para os titulos.

O codigo para o teste::

    # coding: utf-8
    import time
    from contextlib import contextmanager
    from selenium import webdriver


    @contextmanager
    def driver(url):
        _driver = webdriver.Firefox()
        _driver.get(url)

        try:
            yield _driver
        finally:
            _driver.close()


    def test_negative_add_empty_news():
        with driver('http://localhost:5000/noticias/cadastro') as browser:
            button = browser.find_element_by_xpath('/html/body/div/div/form/input')
            button.click()
            message = browser.find_element_by_xpath('/html/body/div/div/h1')
            assert 'Ocorreu um Erro!' in message.text


    def test_positive_add_news():
        with driver('http://localhost:5000/noticias/cadastro') as browser:
            title_field = browser.find_element_by_id('titulo')
            title_field.send_keys("Castalio epidosio 101")
            title_field = browser.find_element_by_id('texto')
            title_field.send_keys("<p>Castalio especial selenium</p>")

            time.sleep(5)

            button = browser.find_element_by_xpath('/html/body/div/div/form/input')
            button.click()
            message = browser.find_element_by_xpath('/html/body/div/div/h1')
            assert 'inserida com sucesso!' in message.text

Para executar o teste basta acessar o diretório root da aplicação `wtf` e rodar::

    py.test -s -vv tests/test_ui.py 
