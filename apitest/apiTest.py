import requests
import json

quotation = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
quotation = quotation.json()
quotation_dolarstr = quotation['USDBRL']["bid"]
quotation_dolarFloat = float(quotation_dolarstr)
print(f'Dolar quotation: {quotation_dolarFloat:.2f}')

value = float(input('USD to convert to BRL: $'))
brlConvert = quotation_dolarFloat * value
print(f'${value:.2f} converted to BRL: R${brlConvert:.2f}')