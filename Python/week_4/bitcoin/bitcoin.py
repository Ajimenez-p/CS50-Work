'''
Expects the user to specify as a command-line argument the number of Bitcoins,, that they would like to buy. If that argument cannot be
converted to a float, the program should exit via sys.exit with an error message.Queries the API for the CoinDesk Bitcoin Price Index
at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of
Bitcoin as a float. Be sure to catch any exceptions, as with code like:
'''

import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    try:
        number_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        price = float(data['bpi']['USD']['rate_float'])
    except:
        sys.exit()

    cost = number_bitcoins * price
    print(f'${cost:,.4f}')


if __name__ == "__main__":
    main()
