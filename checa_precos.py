import yfinance as yf

stock_pair = []

def checar_precos():

    first_pair = []
    second_pair = []

    for i in range(0, len(stock_pair),1):
        if i == 0:
            ticker = yf.Ticker(stock_pair[i])
            price = ticker.info['regularMarketPrice']
            name = ticker.info['symbol']
            first_pair.append(name)
            first_pair.append(price)
        else:        
            ticker = yf.Ticker(stock_pair[i])
            price = ticker.info['regularMarketPrice']
            name = ticker.info['symbol']     
            second_pair.append(name)
            second_pair.append(price)

    diferenca_preco = round(first_pair[1] - second_pair[1], 2)

    ativo1 = first_pair[0].split('.')
    ativo2 = second_pair[0].split('.')

    print('A diferença de preços entre os dois ativos é de: R$ ', diferenca_preco)
    print(f'O ticker {ativo1[0]} está no preço de R$ {first_pair[1]}')
    print(f'O ticker {ativo2[0]} está no preço de R$ {second_pair[1]}')

ticker1 = input('Digite o ticker do primeiro par (de preço mais alto) ')+'.SA'
stock_pair.append(ticker1)
ticker2 = input('Digite o ticker do segundo par (de preço mais baixo) ')+'.SA'
stock_pair.append(ticker2)

checar_precos()