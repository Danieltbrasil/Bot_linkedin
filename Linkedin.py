from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurando as opções do navegador Chrome
options = webdriver.ChromeOptions()

# Definindo o diretório do perfil do usuário para manter a sessão de login
options.add_argument("user-data-dir=C:/Users/Seu usuário/AppData/Local/Google/Chrome/User Data/Profile Selenium")

# Inicializando o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())
# Inicializando o WebDriver com as opções e o serviço configurados
driver = webdriver.Chrome(service=service, options=options)

# Abrindo o LinkedIn
driver.get("https://www.linkedin.com/feed/")

# Esperando o login ser efetuado
while len(driver.find_elements(By.CLASS_NAME, "search-global-typeahead__input")) == 0:
    print("Faça seu login no LinkedIn e espere o próximo passo")
    time.sleep(10)

# Solicitando ao usuário o filtro de pessoas para conexão
filtro = input("Escreva o filtro de pessoas que deseja se conectar: ")

# Acessando a barra de pesquisa e pesquisando pelo filtro fornecido
time.sleep(2)
driver.find_element(By.CLASS_NAME, "search-global-typeahead__input").send_keys(filtro, Keys.ENTER)
time.sleep(5)

# Filtrando os resultados para mostrar apenas pessoas
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()
time.sleep(5)

# Loop principal para navegação e conexões
while True:
    time.sleep(3)
    # Encontrando as listas de resultados de pesquisa
    listas = driver.find_elements(By.CLASS_NAME, "reusable-search__entity-result-list")
    if not listas:
        print("Nenhuma lista de conexões encontrada... Tente um filtro mais específico")
        break

    # Pegando a primeira lista de resultados
    primeira_lista = listas[0]

    # Iterando sobre os elementos dentro da primeira lista
    pessoas = primeira_lista.find_elements(By.CLASS_NAME, "reusable-search__result-container")
    for pessoa in pessoas:
        try:
            # Clicar no botão de conectar, se disponível
            botao_conectar = pessoa.find_element(By.CLASS_NAME, "artdeco-button--2")
            if "Conectar" in botao_conectar.text:
                botao_conectar.click()
                time.sleep(2)
                # Confirmando a conexão
                driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
                time.sleep(2)

                # Extraindo o nome da pessoa para personalizar a mensagem
                texto = pessoa.text
                texto_dividido = texto.split()
                nome = texto_dividido[0]

                # Clicando no botão "Adicionar nota"
                botao_adicionar_nota = driver.find_element(By.CLASS_NAME, "mr1")
                botao_adicionar_nota.click()
                time.sleep(1)

                # Escrevendo e enviando a mensagem personalizada
                area_texto = driver.find_element(By.ID, "custom-message")
                mensagem = f"Olá {nome}, me chamo Daniel e sou programador Python também. Adoraria me conectar para compartilhar conhecimentos e oportunidades. Obrigado!"
                area_texto.send_keys(mensagem)
                time.sleep(2)

                # Clicando no botão de enviar a mensagem
                botao_enviar = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[4]/button[2]')
                botao_enviar.click()
                time.sleep(2)

                # Verificando se apareceu o alerta de limite de conexões
                if len(driver.find_elements(By.CLASS_NAME, "ip-fuse-limit-alert__primary-action")) == 1:
                    if "limite" in driver.find_element(By.CLASS_NAME, "ip-fuse-limit-alert__header").text:
                        print("Limite de conexões alcançado")
                        break
                    else:
                        # Se não for o alerta de limite, clicar em "Entendi" e continuar
                        driver.find_element(By.CLASS_NAME, "ip-fuse-limit-alert__primary-action").click()
                        time.sleep(1)
                else:
                    time.sleep(1)
        except:
            print("Erro ao processar conexões")
            continue

    # Rolando a página para carregar mais resultados
    driver.execute_script("window.scrollTo(0, 1600)")
    
    # Verificando se há o botão de próxima página
    botoes = driver.find_elements(By.CLASS_NAME, "artdeco-pagination__button")
    botao_avancar = botoes[-1]

    if botao_avancar.get_attribute("disabled"):
        print("Última página")
        break
    else:
        botao_avancar.click()

# Fechando o navegador
driver.quit()
