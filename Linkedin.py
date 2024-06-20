from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Seu usuário/AppData/Local/Google/Chrome/User Data/Profile Selenium")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# Abrindo o linkedin
driver.get("https://www.linkedin.com/feed/")

# esperar o login
while len(driver.find_elements(By.CLASS_NAME, "search-global-typeahead__input")) == 0:
    print("faça seu login no linkedin e espere o próximo passo")
    time.sleep(10)

# Escreva pelo que deseja filtrar
filtro = input("Escreva o filtro de pessoas deseja se conectar: ")

# Acessando a barra de pesquisa e pesquisando por python
time.sleep(2)
driver.find_element(By.CLASS_NAME, "search-global-typeahead__input").send_keys(filtro, Keys.ENTER)
time.sleep(5)

# Filtrando por pessoas
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()
time.sleep(5)


while True:
    time.sleep(3)
    # Encontrar as listas de resultados
    listas = driver.find_elements(By.CLASS_NAME, "reusable-search__entity-result-list")
    if not listas:
        print("Nenhuma lista de conexões encontrada... Tente um filtro mais específico")
        break

    primeira_lista = listas[0]

    # Iterar sobre os elementos dentro da primeira lista
    pessoas = primeira_lista.find_elements(By.CLASS_NAME, "reusable-search__result-container")
    for pessoa in pessoas:
        try:
            # Clicar no botão de conectar
            botao_conectar = pessoa.find_element(By.CLASS_NAME, "artdeco-button--2")
            if "Conectar" in botao_conectar.text:
                botao_conectar.click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
                time.sleep(2)
                
                # Extrair o nome da pessoa
                texto = pessoa.text
                texto_dividido = texto.split()
                nome = texto_dividido[0]
                    
                # Clicar no botão "Adicionar nota"
                botao_adicionar_nota = driver.find_element(By.CLASS_NAME, "mr1")
                botao_adicionar_nota.click()
                time.sleep(1)
                    
                # Escrever e enviar a mensagem
                area_texto = driver.find_element(By.ID, "custom-message")
                mensagem = f"Olá {nome}, me chamo Daniel e sou programador Python também. Adoraria me conectar para compartilhar conhecimentos e oportunidades. Obrigado!"
                area_texto.send_keys(mensagem)
                time.sleep(2)
                    
                # Clicar no botão de enviar
                botao_enviar = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[4]/button[2]')
                botao_enviar.click()
                time.sleep(2)
                if len(driver.find_elements(By.CLASS_NAME, "ip-fuse-limit-alert__primary-action")) == 1:
                    time.sleep(1)
                    driver.find_element(By.CLASS_NAME, "ip-fuse-limit-alert__primary-action").click()
                    time.sleep(1)
                else:
                    time.sleep(1)
                    pass
        except:
            print("Erro ao processar conexões")
            continue

    driver.execute_script("window.scrollTo(0, 1600)")
    
    # Verificar se há o botão de próxima página
    botoes = driver.find_elements(By.CLASS_NAME, "artdeco-pagination__button")
    botao_avancar = botoes[-1]

    if botao_avancar.get_attribute("disabled"):
        print("Última página")
    else:
        botao_avancar.click()

driver.quit()
