# ETH_price_allert
Python scrypt to check the Ethereum cryptocurrency price and compare it with the lower and higher price input.

#### Usage

```
python ETH_price_allert.py
```
or
```
python ETH_price_allert.py -low 700 -high 1000 -fiat GBP
```
#### Help 

```
usage: ETH_price_allert.py [-h] [-high HIGH] [-low LOW] [-fiat FIAT]

ETH Price Allert

optional arguments:
  -h, --help  show this help message and exit
  -high HIGH  higher ETH price to reach for the notification (default value 1200 GBP)
  -low LOW    lower ETH price to reach for the notification (default value 800 GBP)
  -fiat FIAT  Currency to adopt (default value GBP) (Sample USD, EUR, AUD, CNY, ...)
```

#### Saple of the running application

<p align="center">
  <img src="https://raw.githubusercontent.com/Ryuk-dev75/ETH_price_allert/main/screenshots/1.png?raw=true">
</p>


#### Future work

implementation in the discord bot as external module
