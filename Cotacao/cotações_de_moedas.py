import requests
import matplotlib.pyplot as plt

#  Valores do USD, EUR, e BTC em 2022
USD = "https://economia.awesomeapi.com.br/USD-BRL/200?start_date=20220101&end_date=20221125"
EUR = "https://economia.awesomeapi.com.br/EUR-BRL/90?start_date=20220101&end_date=20221230"
BTC = "https://economia.awesomeapi.com.br/BTC-BRL/40?start_date=20220101&end_date=20221230"


#  Faz a cotação
def query_coin(coin):
    query = requests.get(coin)
    price = query.json()
    list_coin = [item['bid'] for item in price]
    list_coin.reverse()
    print(list_coin)
    return list_coin


#  Gráfico
plt.figure(figsize=(10, 10))
plt.plot(query_coin(EUR))
plt.show()
