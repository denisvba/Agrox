import pytest  # Bibilioteca de testes
from selenium.webdriver import Chrome  # Abstração para o Driver do navegador
from selenium.webdriver.common.keys import Keys  # Método para envio de eventos como cliques


@pytest.fixture
def navegador():
    driver = Chrome()  # Instancia o Driver
    driver.implicitly_wait(10)  # Estabelece um espera de 10s antes de qualquer interação
    yield driver  # Retorna o Driver ao fim do setup
    driver.quit()  # Fecha o Driver, para evitar processos fantasmas


def test_pesquisa_basica_duckduckgo(navegador):
    # Prepara os dados para o teste
    URL = 'https://www.duckduckgo.com'
    TEXTO = 'IFSP'

    # Navega até a página principal do DuckDuckGo
    navegador.get(URL)

    # Encontra o elemento 'search input' que é um campo de texto
    # Pelo DOM, há um atributo 'id' definido como 'search_form_input_homepage'
    campo_de_pesquisa_tela_inicial = navegador.find_element_by_id('search_form_input_homepage')

    # Insere um texto na pesquisa e aperta ENTER no fim
    campo_de_pesquisa_tela_inicial.send_keys(TEXTO + Keys.RETURN)

    # Verifica se os resultados aparecem na tela
    link_divs = navegador.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0

    # Verifica que pelo menos um dos resultados contém o texto buscado
    xpath = f"//div[@id='links']//*[contains(text(), '{TEXTO}')]"
    resultados_de_texto = navegador.find_elements_by_xpath(xpath)
    assert len(resultados_de_texto) > 0

    # Verifica que o texto buscado é o mesmo
    campo_de_texto_pesquisado = navegador.find_element_by_id('search_form_input')
    assert campo_de_texto_pesquisado.get_attribute('value') == TEXTO
