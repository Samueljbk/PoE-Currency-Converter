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
    
    pprint(f"Status Code: {response.status_code}")
    pprint(f"Response Content: {response.json()}")

if __name__ == "__main__":
    get_current_rates()