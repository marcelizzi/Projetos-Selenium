from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import random

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


def digitar_naturalmente(texto, elemento):

    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 8)/45)

driver = iniciar_driver()
# Navegar até um site
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(3)
# Rolar X quantidade em pixels(descer)
driver.execute_script("window.scrollTo(0, 1000);")
sleep(1)
paragrafo = driver.find_element(By.ID,'campoparagrafo')
texto = """
Did you know that octopuses have three hearts? Two pump blood to the gills for oxygen, while the third pumps it to the rest of the body. When they swim, the heart that delivers blood to the body actually stops, which is why they prefer to crawl rather than swim – it’s less tiring! If you’re curious about octopuses or any other fascinating biology facts, feel free to ask!"""
sleep(1)
digitar_naturalmente(texto, paragrafo)
#input('aperta uma tecla para fechar')
driver.close()