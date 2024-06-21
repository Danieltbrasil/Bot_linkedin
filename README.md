# Bot linkedIn 🤖

Este projeto tem como objetivo automatizar o processo de envio de solicitações de conexão no LinkedIn utilizando Selenium WebDriver. Ele navega pelas páginas de resultados de busca de pessoas, envia uma solicitação de conexão personalizada e continua para a próxima página até que todas as páginas tenham sido processadas.

## Requisitos

- Python 3.7 ou superior
  (link para instalação do python - https://www.python.org/downloads/)
- Google Chrome
  (link para a instalação do google chrome - https://www.google.com/intl/pt-BR/chrome/)
- ChromeDriver
- Selenium
- WebDriver Manager

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Danieltbrasil/Bot_linkedin

2. Crie um ambiente virtual no terminal (pressione as teclas Windows + r e digite "cmd" e depois aperte em "OK") e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate
   # No Windows: venv\Scripts\activate

3. Instale as dependências necessárias para este projeto, uma de cada vez:
   ```bash
   pip install selenium
   pip install webdriver-manager

4. Atualize o caminho para o perfil do Chrome no script 'Linkedin.py' linha 12:
   ```bash
   options.add_argument("user-data-dir=C:/Users/Seu usuário/AppData/Local/Google/Chrome/User Data/Profile Selenium")

## Uso
1. Navegue até o diretório do projeto (use o comando cd "diretório do projeto") e execute o script:
   ```bash
   python Linkedin.py

2. O script irá abrir uma nova janela do Chrome e solicitará que você faça login manualmente no LinkedIn (se não estiver logado).
3. Após o login, o script vai pedir um filtro de pessoas que você deseja filtrar (exemplo: "python") e automaticamente irá para a página de busca de pessoas e começará a enviar solicitações de conexão com a mensagem personalizada.

## Personalização
Você pode personalizar a mensagem que será enviada com cada solicitação de conexão. No script Linkedin.py linha 77, edite a variável mensagem dentro do loop principal:
   ```bash
   mensagem = f"Olá {nome}, me chamo Daniel e sou programador Python também. Adoraria me conectar para compartilhar conhecimentos e oportunidades. Obrigado!"
