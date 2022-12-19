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

    if round(first_pair[1],2) > round(second_pair[1],2):
        diferenca_preco = (first_pair[1] - second_pair[1])
        diferenca_preco = '{:.2f}'.format(float(diferenca_preco))
    else:
        diferenca_preco = (second_pair[1] - first_pair[1])
        diferenca_preco = '{:.2f}'.format(float(diferenca_preco))


    ativo1 = first_pair[0].split('.')
    ativo2 = second_pair[0].split('.')

    diferenca_preco = str(diferenca_preco).replace('.', ',')

    print(f'A diferença de preços entre {ativo1[0]} e {ativo2[0]} é de R$ {diferenca_preco}')

ticker1 = input('Digite o ticker do primeiro par: ')+'.SA'
ticker2 = input('Digite o ticker do segundo par: ')+'.SA'
stock_pair.append(ticker1)
stock_pair.append(ticker2)

checar_precos()