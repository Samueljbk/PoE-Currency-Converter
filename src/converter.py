import requests
import json
from pprint import pprint
from .constants import POE_NINJA_URL, LEAGUE_NAME

def get_current_rates():
    params = {
        "league": LEAGUE_NAME,
        "type": "Currency"
    }
    
    response = requests.get(POE_NINJA_URL, params=params)
    response_data = response.json()
    
    currency_rates = {}
    
    for currency in response_data['lines']:
        currency_name = currency['currencyTypeName']
        chaos_value = currency['chaosEquivalent']
        currency_rates[currency_name] = chaos_value
    return currency_rates

    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
if __name__ == "__main__":
    get_current_rates()