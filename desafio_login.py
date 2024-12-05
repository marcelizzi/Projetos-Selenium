from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
    arguments = ['--lang=pt-BR','--window-size=800,600','--incognito']
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = iniciar_driver()
# Navegar até um site
driver.get('https://cursoautomacao.netlify.app/login')
sleep(5)
campo_email = driver.find_element(By.XPATH,'//div[@class="form-group loginForm"]/input')
sleep(2)
campo_email.send_keys("elonmusk@xtwitter.com")
sleep(2)
campo_senha = driver.find_element(By.XPATH,'//div[@class="form-group"]/input')
sleep(2)
campo_senha.send_keys("lapdog")
sleep(2)
botao_enviar = driver.find_element(By.XPATH,'//div[@class="container"]/button')
sleep(2)
botao_enviar.click()

input('aperta uma tecla para fechar')
driver.close()