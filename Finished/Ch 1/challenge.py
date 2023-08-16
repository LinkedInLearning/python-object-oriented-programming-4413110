# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol


class StockSymbol:
    def __init__(self, ticker, price, company) -> None:
        self.ticker = ticker
        self.price = price
        self.company = company

    def get_description(self):
        pass
    