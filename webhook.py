from pprint import pprint
import requests

bot_token = "419653899:AAHsjKQYihN6pHI4kEHGBWVoytozZMq14Do"
test_url = "https://4c03e1a9.ngrok.io".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))

pprint(r.status_code)
pprint(r.json())
