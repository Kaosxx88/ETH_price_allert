# ETH Price Allert (www.coinbase.com price reference)
# this program check the Ethereum cryptocurrency price and compare it with the lower and higher price input.
# requests module needed 

import time
import requests
import argparse
from datetime import datetime

fiat = 'GBP'
min_price_default = 800
max_price_default = 1200

def eth_price(fiat):	

	url = f'https://api.coinbase.com/v2/prices/ETH-{fiat}/buy'
	response = requests.get(url)
	price = (response.json()['data']['amount'])
	return float(price)

def allert(fiat):

	print ( f'\nDefault allarms values:\n\n Min = {min_price_default} {fiat}\n Max = {max_price_default} {fiat}\n')

	while True:
		now = datetime.now()
		print (f'{now.strftime("%d/%m %H:%M:%S")} ETH value on www.coinbase.com -> {eth_price(fiat)} {fiat}')

		if eth_price(fiat) >= args.high:
			print (f'\n\nETH higt price reached {eth_price(fiat)} {fiat}\n\n Time to buy!\n\n')

		elif eth_price(fiat) <= args.low:
			print (f'\n\nETH lower price reached {eth_price(fiat)} {fiat}\n\n Time to sell!\n\n')

		time.sleep(10)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='ETH Price Allert')
	parser.add_argument('-high', default=max_price_default, type=int, help= f'higher ETH price to reach for the notification (default value {max_price_default} {fiat})')
	parser.add_argument('-low', default=min_price_default, type=int, help=f'lower ETH price to reach for the notification (default value {min_price_default} {fiat})')
	parser.add_argument('-fiat', default=fiat, type=str, help=f'Currency to adopt (default value {fiat}) (Sample USD, EUR, AUD, CNY, ...) ')
	args = parser.parse_args()

	allert(args.fiat)

	


	

