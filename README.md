~~# Agrox~~

~~Aula 04/10 Arquitetura de Software~~


Arquitetura de Software, Aula 15 - 2021
Ainda é Agrox, pelas origens :D

Além do exemplos de Hello World e uma operação matemática, este repo tem uma demo _bem_ simplória apresentada como parte de um trabalho (Gravei a tela em execução, acelerei o vídeo e coloquei na apresentação ;D).

Python, py.test e Selenium

---

```bash
# prepara uma pasta como ambiente de trabalho
mkdir selenium_teste
cd selenium_teste

# instala o utilitário de virtualenv do python e o driver para o Chrome
sudo apt install python3-venv chromium-chromedriver

# cria e ativa a virtualenv, espaço que os pacotes Python ficarão isolados
python3 -venv -m venv venv-selenium-teste
source venv-selenium-teste/bin/activate

# instala a biblioteca do selenium e a do pytest
pip install selenium pytest pytest-html
```

---

Descaradamente copiado (com créditos) do [AutomationPanda](https://blog.testproject.io/2019/07/16/installing-selenium-webdriver-using-python-chrome/), traduzido para o exemplo simples e acrescido de alguns testes para o exemplo longo.

--- 

Para rodar, play no PyCharm ou:

```bash
pytest --html=report.html
```


Para rodar só o exemplo simples:

```bash
pytest /tests/simplestest.py --html=report.html
```
```
