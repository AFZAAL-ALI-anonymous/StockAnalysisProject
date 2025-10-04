import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# Extract Tesla stock data
tesla_data = yf.download('TSLA', start='2020-01-01', end='2025-01-01')

# Reset index and display first 5 rows
tesla_data.reset_index(inplace=True)
tesla_data.head()

# Extract GameStop stock data
gme_data = yf.download('GME', start='2020-01-01', end='2025-01-01')

# Reset index and display first 5 rows
gme_data.reset_index(inplace=True)
gme_data.head()
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

# Find the table
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace('$', '').replace(',', '')
        tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

# Display last 5 rows
tesla_revenue.tail()
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == 2:
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace('$', '').replace(',', '')
        gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)

gme_revenue.tail()
def make_graph(df, title, xlabel="Date", ylabel="Close Price"):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()
make_graph(tesla_data, "Tesla Stock Price")
make_graph(gme_data, "GameStop Stock Price")

def make_graph(stock_data, title):
    plt.figure(figsize=(12,6))
    plt.plot(stock_data['Date'], stock_data['Close'], marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Closing Price ($)')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent label cutoff
    plt.show()

