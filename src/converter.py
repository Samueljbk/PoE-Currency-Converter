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
    
    currency_rates = {}
    
    response_data = response.json()
    
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    get_current_rates()