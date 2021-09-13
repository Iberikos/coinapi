import requests as req


url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"
apikey = "05915253-A982-431B-87AA-55C645B31B41"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = req.get(url, headers=cabecera)

print(respuesta.status_code)
midiccionario = respuesta.json()
print(midiccionario['rate'])

print(respuesta.json()["rate"])
