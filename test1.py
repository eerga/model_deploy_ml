import requests

url = 'http://localhost:9696/predict'
#url = 'https://shy-paper-7016.fly.dev/predict'

customer = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json = customer)
churn = response.json()

print('response: ', churn)

if churn['churn'] >= 0.5:
    print('sending email with promo')
else:
    print('dont do anything')
