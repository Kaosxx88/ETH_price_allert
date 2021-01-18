# ETH Price Allert (www.coinbase.com price reference)
# this program check the Ethereum cryptocurrency price and compare it with the lower and higher price input.
# requests module needed 

import time
import requests
import argparse
from datetime import datetime

fiat = 'GBP'
min_price_default = 600
max_price_default = 1200

def eth_price(fiat):
	

		url = f'https://api.coinbase.com/v2/prices/ETH-{fiat}/buy'
		response = requests.get(url)
		price = float(response.json()['data']['amount'])		

		if type(price) is not float:
			
			time.sleep(5)
			eth_price(fiat)

		else:
			return price


def allert(fiat):

	print ( f'\nDefault allarms values:\n\n Min = {args.low} {fiat}\n Max = {args.high} {fiat}\n')

	while True:
		now = datetime.now()
		price_ETH = eth_price(fiat)
	
		print (f'{now.strftime("%d/%m %H:%M:%S")} ETH value -> {price_ETH} {fiat}')

		if price_ETH >= args.high:
			print (f'\n\nETH higt price reached {price_ETH} {fiat}\n\n Time to buy!\n\n')

		elif price_ETH <= args.low:
			print (f'\n\nETH lower price reached {price_ETH} {fiat}\n\n Time to sell!\n\n')

		time.sleep(5)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='ETH Price Allert')
	parser.add_argument('-high', default=max_price_default, type=int, help= f'higher ETH price to reach for the notification (default value {max_price_default} {fiat})')
	parser.add_argument('-low', default=min_price_default, type=int, help=f'lower ETH price to reach for the notification (default value {min_price_default} {fiat})')
	parser.add_argument('-fiat', default=fiat, type=str, help=f'Currency to adopt (default value {fiat}) (Sample USD, EUR, AUD, CNY, ...) ')
	args = parser.parse_args()

	allert(args.fiat)

	


	

