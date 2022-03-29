from get_server_data import GetServerData

if __name__=='__main__':
    server_data = GetServerData(url='https://www.coinbase.com/price')
    server_data.run()
    print(len(server_data.html_docs))