# projeto automação de tarefa no linkedin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.linkedin.com/feed/")

navegador.find_element('xpath', '//*[@id="username"]').send_keys('teste@gmail.com')
navegador.find_element('xpath', '//*[@id="password"]').send_keys('123456')
navegador.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button').click()
input('')