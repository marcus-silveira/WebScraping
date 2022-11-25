from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

servico_chrome = Service(ChromeDriverManager().install())

#  Link do site da Nota Fiscal Gaúcha
path = "https://nfg.sefaz.rs.gov.br"

#  Inicia o Driver e leva pro site
browser = webdriver.Chrome(service=servico_chrome)
browser.get(path)

#  Entra na área de Login
login = browser.find_element(By.CLASS_NAME, "linkLogin").find_element(By.TAG_NAME, "a")
login.click()
sleep(1)

#  Inicia o preenchimento dos dados para fazer Login
browser.find_element(By.ID, "nro_cpf_loginNfg").send_keys("CPF")
browser.find_element(By.ID, "senha_loginNfg").send_keys("password")
#  Tentativa de verificar o CAPTCHA, se falhar usar a linha 28
browser.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/div/iframe').click()
sleep(1)
#  sleep(10)  # RECAPTCHA precisa ser manual, mas às vezes ele falha
browser.find_element(By.CLASS_NAME, "botaoLoginNfg").click()  # Faz o Login
sleep(1)

#  Clica no aba das sua NFs
my_notes = browser.find_element(By.ID, "menuMinhasNotasClick")
my_notes.click()
sleep(1)

#  Preenche as datas de quando você quer as notas
initial_date = browser.find_element(By.ID, "txtDtInicial")
initial_date.send_keys(Keys.CONTROL, 'a')
initial_date.send_keys('01/01/2022')
final_date = browser.find_element(By.ID, "txtDtFinal")
final_date.send_keys(Keys.CONTROL, 'a')
final_date.send_keys('30/12/2022')

#  Seleciona todos os botões azuis e pega o que faz a consulta
for i in browser.find_elements(By.CLASS_NAME, "botaoAzul"):
    if i.get_attribute('value') == 'Consultar':
        i.click()
        sleep(1)

#  Faz o download em PDF
browser.find_element(By.CLASS_NAME, "buttons-pdf").click()

sleep(5)
