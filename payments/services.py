import requests
from decouple import config

ZARINPAL_MERCHANT_ID = config('ZARINPAL_MERCHANT_ID') 
ZARINPAL_REQUEST_URL = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZARINPAL_VERIFY_URL = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZARINPAL_START_URL = "https://www.zarinpal.com/pg/StartPay/"

CALLBACK_URL = "http://127.0.0.1:8000/api/payments/verify/"  

def request_payment(amount, description, email, mobile):
    """ Request payment from ZarinPal """
    data = {
        "merchant_id": ZARINPAL_MERCHANT_ID,
        "amount": int(amount) * 10,  # Convert to Toman
        "description": description,
        "callback_url": CALLBACK_URL,
        "metadata": {"email": email, "mobile": mobile}
    }
    
    response = requests.post(ZARINPAL_REQUEST_URL, json=data)
    response_data = response.json()

    if response_data.get("data") and response_data["data"].get("authority"):
        return response_data["data"]["authority"]
    return None

def verify_payment(authority, amount):
    """ Verify payment status """
    data = {
        "merchant_id": ZARINPAL_MERCHANT_ID,
        "amount": int(amount) * 10,
        "authority": authority
    }

    response = requests.post(ZARINPAL_VERIFY_URL, json=data)
    return response.json()
