
import os.path
import cashtagSet


def submitJob(stock, exchange):
    logFile = 'log'+stock+'.txt'
    cmdTotal = cmd+"'"+stock+"'"+' '+"'"+exchange+"'"+' > '+logFile+suffix
    print cmdTotal
    os.system(cmdTotal)


def doWork():
    exchange = 'O'
    stocks = cashtagSet.cashtagSet('NASDAQ100')
    for stock in stocks:
        ticker = stock.split('$')[1]
        submitJob(ticker, exchange)

    exchange = 'N'
    stocks = cashtagSet.cashtagSet('NYSE100')
    for stock in stocks:
        ticker = stock.split('$')[1]
        submitJob(ticker, exchange)

    exchange = 'N'
    stocks = cashtagSet.cashtagSet('COMPANIES')
    for stock in stocks:
        ticker = stock.split('$')[1]
        submitJob(ticker, exchange)


if __name__ == '__main__':
    doWork()
