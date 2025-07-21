from dotenv import load_dotenv # type: ignore
import os, requests  # type: ignore
from datetime import *
from twilio.rest import Client # type: ignore

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = os.environ.get("STOCK_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_KEY,
}
response = requests.get('https://www.alphavantage.co/query', stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']

stock_list = [value for (key, value) in stock_data.items()]

last_close = float(stock_list[0]['4. close'])
prev_close = float(stock_list[1]['4. close'])

percent_change = round(((last_close - prev_close) / prev_close) * 100, 2)

if (abs(percent_change) >= 2):
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    NEWS_KEY = os.environ.get("NEWS_KEY")

    news_params = {
        'apiKey': NEWS_KEY, 
        'q': COMPANY_NAME, 
        'language': 'en',
    }

    response = requests.get('https://newsapi.org/v2/everything', news_params)
    response.raise_for_status()
    news = response.json()['articles']
    first_3 = news[:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    TO_NUM = os.environ.get("TO_NUM")
    FROM_NUM = os.environ.get("FROM_NUM")
    
    client = Client(account_sid, auth_token)
    emoji = "📈" if percent_change >=0 else "📉"
    
    text = f"\033[1m{STOCK}:\033[0m {emoji}{abs(percent_change)}%\n\n"
    
    for article in first_3:
        headline = article['title']
        brief = article['description']
        
        text += f"\033[1mHeadline: \033[0m{headline}\n\033[1mBrief: \033[0m{brief}\n\n"
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body=text,
            to=TO_NUM,
            from_=FROM_NUM,
        )
    print(message.status)
