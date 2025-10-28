import requests

url = 'http://localhost:9696/predict'
#url = 'https://shy-paper-7016.fly.dev/predict'

customer = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

response = requests.post(url, json = customer)
churn = response.json()

print('response: ', churn)

if churn['churn'] >= 0.5:
    print('sending email with promo')
else:
    print('dont do anything')
