#Python script to retrieve Top 10 performing Cryptocurrencies, ranked by Market capitalization

#Import relevant modules to query API 
import requests, json


#Define variables
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
             'Accept': 'application/json',
             'Accept-Encoding': 'deflate, gzip',
             'X-CMC_PRO_API_KEY': '4831410c-b174-4908-819a-bb923176a2d7',
         }

qs = {'start':'1','limit':'10','convert':'USD'}

counter = 0

table_header = [['#', 'Name', 'Market Cap ($)', 'Price ($)', 'Volume-24h ($)', 'Circulating Supply', 'Change-24h']]


#Request data from CoinMarketCap API using GET function
cmc_data = requests.get(url, headers=headers, params=qs)


if cmc_data.status_code == 200: #Check if status is ok

    response = cmc_data.json() #use built-in json decoder to get json response content
    
    print('\n\n          TOP 10 PERFORMING CRYPTOCURRENCIES      -Ranked: Market capitalization- \n')

    print('='*110)
    print("{:^10s}".format(table_header[0][0]),end='')
    print("{:<10s}".format(table_header[0][1]),end='')
    print("{:>20s}".format(table_header[0][2]),end='')
    print("{:>12s}".format(table_header[0][3]),end='')
    print("{:^20s}".format(table_header[0][4]),end='')
    print("{:^25s}".format(table_header[0][5]),end='')
    print("{:^10s}".format(table_header[0][6]),end='')
    print('\n')
    print('='*110)
    

    for counter in range(0, 10):

        symbol = response['data'][counter]['symbol']        

        print("{:^10}".format(response['data'][counter]['cmc_rank']), end='')
        print("{:<15}".format(response['data'][counter]['name']), end='')
        print("{:>16.2f}".format(response['data'][counter]['quote']['USD']['market_cap']), end='')
        print("{:>10.2f}".format(response['data'][counter]['quote']['USD']['price']), end='')
        print("{:>18.2f}".format(response['data'][counter]['quote']['USD']['volume_24h']), end='')
        print("{:>20.2f}".format(response['data'][counter]['circulating_supply']),symbol, end='')
        print("{:>10.2f}".format(response['data'][counter]['quote']['USD']['percent_change_24h']),'%', end='')
        print('\n')

    
else :
 print('ERROR: Check status code: ',cmc_data.status_code)
