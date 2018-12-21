#Python script to retrieve Top 10 performing Cryptocurrencies, ranked by Market capitalization

#Import relevant modules to query API 
import requests, json


#Define variables used to query API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
             'Accept': 'application/json',
             'Accept-Encoding': 'deflate, gzip',
             'X-CMC_PRO_API_KEY': '4831410c-b174-4908-819a-bb923176a2d7',
         }

qs = {'start':'1','limit':'10','convert':'USD'}


#Definte preogram variables
counter = 0

topNum = range(0,10)

table_title = " TOP 10 PERFORMING CRYPTOCURRENCIES  -Ranked: Market capitalization-"
table_header = ['#', 'Name', 'Market Cap ($)', 'Price ($)', 'Volume-24h ($)', 'Change-24h (%)', 'Circulating Supply']

data_keys = ['cmc_rank', 'name', 'quote', 'circulating_supply']
quote_keys = ['market_cap', 'price', 'volume_24h','percent_change_24h']



#Request data from CoinMarketCap API using GET function
cmc_data = requests.get(url, headers=headers, params=qs)


if cmc_data.status_code == 200: #Check if status is ok

    response = cmc_data.json() #use built-in json decoder to get json response content

    data = response['data'] 

    if all(k in data[0] for k in data_keys): #Check if all 2nd level keys exist
        if all(k in data[0]['quote']['USD'] for k in quote_keys): #Check if all 3rd level keys exist

            print('All requested keys exist\n\n')
            
            print("{:^150}".format(table_title))
            print('='*150)

            for i in table_header:
                print("{:<20s}".format(i),end='')

            print('\n')
            print('='*150)

            #Print # cryptocurrencies defined in topNum
            for x in topNum:
                for y in data_keys:
                    
                    if y == 'quote':
                        for z in quote_keys:
                            print("{:<20.2f}".format(data[x][y]['USD'][z]), end='')
                    elif y == 'circulating_supply':
                        symbol = data[x]['symbol']
                        print("{:>.2f}".format(data[x][y]), symbol, end='')
                    else:
                        print("{:<20}".format(data[x][y]), end='')

                print('\n')
        else:
            print('ERROR - check "qoute" keys')
    else:
        print('ERROR - check "data" keys')

       
else :
 print('ERROR: Check status code: ',cmc_data.status_code)
