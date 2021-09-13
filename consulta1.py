import requests 


url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
apikey = "05915253-A982-431B-87AA-55C645B31B41"
cabecera = {"X-CoinAPI-Key": apikey}

seguir = 's'
while seguir == 's':
    de = input("Moneda de origen ")
    a = input("Moneda de destino ")
    respuesta = requests.get(url.format(de, a), headers=cabecera)
    
    if respuesta.status_code == 200:
        print(respuesta.json()["rate"])    
    else:
        print(respuesta.status_code)
        print(respuesta.json())
        
    seguir = input("Quieres más? (S/N) ").lower()