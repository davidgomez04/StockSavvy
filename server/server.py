from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from stock import Stock
from webdriver_manager.chrome import ChromeDriverManager
import requests

app = Flask(__name__)
CORS(app)

def extractEarnings(data):
    stocks = []
    for row in data:
        company_name = row.find('td', {'aria-label': 'Company'}).text.strip()
        symbol = row.find('td', {'aria-label': 'Symbol'}).text.strip()
        event_name = row.find('td', {'aria-label': 'Event Name'}).text.strip()
        earnings_call_time = row.find('td', {'aria-label': 'Earnings Call Time'}).text.strip()
        stock = Stock(company_name, symbol, event_name, earnings_call_time)
        stocks.append(stock)
    return stocks

#next.js, fast-api, typescript
@app.route('/api/getEarningsData', methods=['GET'])
def getEarningsData():
    selected_date = request.args.get('day')
    options = Options()
    options.add_argument("--headless")
    options.add_argument('log-level=3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yahoo_link = "https://finance.yahoo.com/calendar/earnings"
    date_string = "?day=" + selected_date
    url = yahoo_link + date_string
    driver.get(url)
    
    html_content = driver.find_element(By.ID, "cal-res-table")
    soup = BeautifulSoup(html_content.get_attribute("innerHTML"), 'html.parser')
    data = soup.find_all('tr', class_='simpTblRow')
    stocks = extractEarnings(data)
    
    driver.quit()
    return jsonify([stock.__dict__ for stock in stocks])

#create a dict for all the banner info
def getCurrentPrice(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("fin-streamer")
    for tag in elements:
        if tag.get("data-symbol") == ticker and tag.get("data-field") == "regularMarketPrice":
            return tag.get("value")
        
def getPriceChange(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("fin-streamer")
    for tag in elements:
        if tag.get("data-symbol") == ticker and tag.get("data-field") == "regularMarketChange":
            return tag.get("value")
        
def getPriceChangePercent(ticker):
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("fin-streamer")
    for tag in elements:
        if tag.get("data-symbol") == ticker and tag.get("data-field") == "regularMarketChangePercent":
            return tag.get("value")

@app.route('/api/getMarketData', methods=['GET'])
def getMarketData():
    try:
        sp500CurrentPrice = getCurrentPrice("^GSPC")
        nasdaqCurrentPrice = getCurrentPrice("^IXIC")
        dowCurrentPrice = getCurrentPrice("^DJI")
        
        sp500PriceChange = getPriceChange("^GSPC")
        nasdaqPriceChange = getPriceChange("^IXIC")
        dowPriceChange = getCurrentPrice("^DJI")
        
        sp500PriceChangePercent = getPriceChangePercent("^GSPC")
        nasdaqPriceChangePercent = getPriceChangePercent("^IXIC")
        dowPriceChangePercent = getCurrentPrice("^DJI")

        marketData = {
            'S&P 500': {
                'current_price': sp500CurrentPrice, 
                'price_change': sp500PriceChange,
                'price_change_percent': sp500PriceChangePercent
            },
            'Dow 30': {
                'current_price': dowCurrentPrice,
                'price_change': dowPriceChange,
                'price_change_percent': dowPriceChangePercent
            },
            'NASDAQ': {
                'current_price': nasdaqCurrentPrice,
                'price_change': nasdaqPriceChange,
                'price_change_percent': nasdaqPriceChangePercent
            },
        }

        return jsonify(marketData), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)