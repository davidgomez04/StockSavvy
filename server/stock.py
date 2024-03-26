class Stock:
    def __init__(self, company_name, ticker_symbol, event_name, earnings_call_time):
        self.company_name = company_name
        self.ticker_symbol = ticker_symbol
        self.event_name = event_name
        self.earnings_call_time = earnings_call_time

    def __str__(self):
        return f"Stock Name: {self.company_name}\nTicker Symbol: {self.ticker_symbol}\nEarnings Call Time: {self.earnings_call_time}"