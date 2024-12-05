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
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(3)
# Rolar X quantidade em pixels(descer)
driver.execute_script("window.scrollTo(0, 1600);")
sleep(1)
checkboxes = driver.find_elements(By.XPATH,'//section[@class="jumbotron desafios5"]//input[@type="checkbox"]')
sleep(2)
checkboxes[1].click()
sleep(2)
checkboxes[3].click()
sleep(2)
checkboxes[4].click()
sleep(2)
driver.execute_script("window.scrollTo(0, 1850);")
sleep(1)
for i in range(5,len(checkboxes)):
    checkboxes[i].click()
    sleep(1)
sleep(5)
#input('aperta uma tecla para fechar')
driver.close()