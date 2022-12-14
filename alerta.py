import yfinance as yf
from datetime import date, datetime
from time import sleep

# If you will use in your machine, uncomment line below and lines that started with notification
# from win10toast import ToastNotifier 


# notification = ToastNotifier() 
hora_atual = datetime.strftime(datetime.now(), '%H:%M')

## Checar se horário atual está dentro do horário de negociações da bolsa. 10h as 17:55

stock_pair = []
quinze_minutos = 60*15

def checa_horario(time):
    abertura = '10:00'
    fechamento = '17:55'
    
    if (time > abertura) and (time < fechamento):
        return True
    else:
        return False

PRECO_ABAIXO = 'O valor do spread atual está abaixo do selecionado, pode abrir ordem.'
PRECO_ACIMA = 'O valor do spread atual está acima do selecionado, pode abrir ordem.'

def checar_precos(spread, pos):

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
    print('A diferença de preços entre os dois ativos é de: R$ ', diferenca_preco)
    
    if pos == 'acima' and spread < diferenca_preco:
        # notification.show_toast('ALERTA DE PREÇO', PRECO_ACIMA, duration=10)
        print(PRECO_ACIMA)
    elif pos != 'acima' and spread > diferenca_preco:
        # notification.show_toast('ALERTA DE PREÇO', PRECO_ABAIXO, duration=10)
        print(PRECO_ABAIXO)


ticker1 = input('Digite o ticker do primeiro par (de preço mais alto) ')+'.SA'
stock_pair.append(ticker1)
ticker2 = input('Digite o ticker do segundo par (de preço mais baixo) ')+'.SA'
stock_pair.append(ticker2)

spread = float(input('Digite o valor do spread que deseja ser alertado, separando os centavos com ponto ao invés de vírgula. Ex: 0.50 '))
pos = input('Digite se deseja ser alertado quando o spread esteja acima ou abaixo do valor digitado anteriormente ')


print('Checando preços...')

while checa_horario(hora_atual):

    checar_precos(spread, pos)
    sleep(quinze_minutos)
