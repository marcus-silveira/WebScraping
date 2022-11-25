import requests
from bs4 import BeautifulSoup
import locale
import tabulate
from Fundos_imobiliarios.models import FundoImobiliario

locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')


def tratar_porcentagem(porcentagem):
    return locale.atof(porcentagem.split('%')[0])


def tratar_decimal(decimal):
     return locale.atof(decimal)


headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.fundamentus.com.br/fii_resultado.php", headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

linhas = soup.find(id="tabelaResultado").find('tbody').find_all('tr')

for linha in linhas:
    dados = linha.find_all('td')
    codigo = dados[0].text
    segmento = dados[1].text
    cotacao = tratar_decimal(dados[2].text)
    ffo_yield = tratar_porcentagem(dados[3].text)
    dividend_yield = tratar_porcentagem(dados[4].text)
    p_vp = tratar_decimal(dados[5].text)
    valor_mercado = tratar_decimal(dados[6].text)
    liquidez = tratar_decimal(dados[7].text)
    qt_imoveis = int(dados[8].text)
    preco_m2 = tratar_decimal(dados[9].text)
    aluguel_m2 = tratar_decimal(dados[10].text)
    cap_rate = tratar_porcentagem(dados[11].text)
    vacancia = tratar_porcentagem(dados[12].text)

    fundo_imobiliario = FundoImobiliario(codigo, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado,
                                         liquidez, qt_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia)
