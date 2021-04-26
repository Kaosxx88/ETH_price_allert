# ETH Price Allert (www.coinbase.com price reference)
# this program check the Ethereum cryptocurrency price and compare it with the lower and higher price input.
# requests and colorama modules needed 

import time
import requests
import argparse
from datetime import datetime

from colorama import init, Fore, Style

init()

fiat = 'GBP'
min_price_default = 600
max_price_default = 2000

def eth_price(fiat):
	

		url = f'https://api.coinbase.com/v2/prices/ETH-{fiat}/buy'
		response = requests.get(url)
		price = float(response.json()['data']['amount'])		

		if type(price) is not float:
			
			time.sleep(5)
			eth_price(fiat)

		else:
			return int(price)


def allert(fiat):

	print ( f'\nDefault allarms values:\n\n Min = {args.low} {fiat}\n Max = {args.high} {fiat}\n')

	lower  = eth_price(fiat)
	higher = eth_price(fiat)

	while True:
		now = datetime.now()
		price_ETH = eth_price(fiat)

		# updating value lower and higher price
		if lower > price_ETH : lower = price_ETH
		if higher < price_ETH : higher = price_ETH
	
		print (f'{now.strftime("%H:%M:%S")} ETH {Fore.CYAN + str(price_ETH) + Style.RESET_ALL } {fiat} (↓ {Fore.RED + str(lower) + Style.RESET_ALL } ↑ {Fore.GREEN + str(higher) + Style.RESET_ALL})') 

		if price_ETH >= args.high:
			print (f'\n\nETH higt price reached {price_ETH} {fiat}\n\n Time to sell!\n\n')

		elif price_ETH <= args.low:
			print (f'\n\nETH lower price reached {price_ETH} {fiat}\n\n Time to buy!\n\n')

		time.sleep(10)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='ETH Price Allert')
	parser.add_argument('-high', default=max_price_default, type=int, help= f'higher ETH price to reach for the notification (default value {max_price_default} {fiat})')
	parser.add_argument('-low', default=min_price_default, type=int, help=f'lower ETH price to reach for the notification (default value {min_price_default} {fiat})')
	parser.add_argument('-fiat', default=fiat, type=str, help=f'Currency to adopt (default value {fiat}) (Sample USD, EUR, AUD, CNY, ...) ')
	args = parser.parse_args()

	allert(args.fiat)

	


	

