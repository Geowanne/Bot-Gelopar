#link que mostra como fazer https://www.youtube.com/watch?v=8AMNaVt0z_M&t=862s
from senhas import login, senha
from selenium import webdriver # O navedagador
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd 
from selenium.common.exceptions import NoSuchElementException

arquivo = "CONTROLE_MKT_GELOPAR.xlsx"
df = pd.read_excel(arquivo)
url_gelopar = 'https://loja.gelopar.com.br/flexyadmin/user/login'
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get(url_gelopar)

navegador.find_element('xpath','//*[@id="login_username"]').send_keys(login)
navegador.find_element('xpath','//*[@id="login_pass"]').send_keys(senha)
navegador.find_element('xpath', '//*[@id="login_toggle"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="main-menu"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="main-menu"]/ul/li[3]/a/span').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="main-menu"]/ul/li[3]/ul/li[7]').click()
time.sleep(1)


for index, row in df.iterrows():
    if row["CODGELOPAR"] == int(1111):
        break
    #campo pesquisa
    pesquisa = navegador.find_element('xpath','//*[@id="reportSearch"]/div/div/div/div/div/input[1]')
    #o que mandar no elemento pesquisa
    pesquisa.send_keys(row["CODGELOPAR"])
    print(f'Atualizando o código {row["CODGELOPAR"]}')
    pesquisa = navegador.find_element('xpath', '//*[@id="reportSearch"]/div/div/div/div/div/span/button').click()
    time.sleep(1.5)
    #limpar campo estoque
    navegador.find_element('xpath','//*[@id="categories"]/tbody/tr[1]/td[4]/input').clear()
    #envia o novo valor do estoque
    estoque = navegador.find_element('xpath','//*[@id="categories"]/tbody/tr[1]/td[4]/input')
    estoque.send_keys(row["ESTOQUE"])
    #clica no campo estoque minimo para atualizar o estoque
    navegador.find_element('xpath','//*[@id="categories"]/tbody/tr/td[5]/input').click()
    #limpar campo pesquisa
    pesquisa = navegador.find_element('xpath','//*[@id="reportSearch"]/div/div/div/div/div/input[1]').clear()
    print(f'Código {row["CODGELOPAR"]} atualizado')

print('Atualização de estoqueque concluida')
input("Pressione Enter para sair")



