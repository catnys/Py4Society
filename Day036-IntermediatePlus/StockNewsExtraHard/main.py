import requests
from datetime import datetime, timedelta
from twilio.rest import Client

API_KEY = 'VJK9F5FJPPAZBTXD'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY = "2024-07-19"
TODAY_AS_DATE = datetime.strptime(TODAY, "%Y-%m-%d")
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
NEWS_API_KEY = 'your_news_api_key_here'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)



def get_top_headlines(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json()['articles'][:3]  # Get the first 3 articles
    return articles


def send_sms(message_body):
    client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to='your_phone_number'
    )


# Assuming the variables API_KEY, STOCK, COMPANY_NAME, and TODAY are defined as shown previously

# Step 1: Fetch stock data
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': API_KEY,
}
r = requests.get(url=url, params=parameters)
data = r.json()
days = data['Time Series (Daily)']

# Initialize variables for the loop
previous_day_date = TODAY - timedelta(days=1)
previous_day_str = previous_day_date.strftime("%Y-%m-%d")
closing_price_today = None
closing_price_previous_day = None

# Loop through the days to find the significant change
for day in reversed(list(days.keys())):
    if day <= TODAY:
        closing_price_today = float(data[TODAY]["4. close"])
        closing_price_previous_day = float(data[day]["4. close"])
        break

# Calculate percentage change
if closing_price_today and closing_price_previous_day:
    percentage_change = ((closing_price_today - closing_price_previous_day) / closing_price_previous_day) * 100
else:
    percentage_change = 0

# Step 2: Fetch news articles
if abs(percentage_change) >= 5:
    articles = get_top_headlines(COMPANY_NAME)
    news_messages = []
    for article in articles:
        headline = article['title']
        brief = article['description']
        news_message = f"{STOCK}: {percentage_change:.2f}%\nHeadline: {headline}\nBrief: {brief}\n\n"
        news_messages.append(news_message)

    # Step 3: Send SMS
    message_body = "\n".join(news_messages)
    send_sms(message_body)
else:
    print("No significant change.")
