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
        
    common_currencies = [
        "Divine Orb",
        "Exalted Orb",
        "Chaos Orb",
        "Ancient Orb",
        "Orb of Alchemy"
    ]
    
    print("\nCurrent Currency Values (in Chaos Orbs):")
    
    for currency in common_currencies:
        if currency in currency_rates:
            # Format the value to 2 decimal places for readability
            value = currency_rates[currency]
            print(f"{currency}: {value:.2f} chaos")
    
    return currency_rates

def convert_currency(amount, from_currency, to_currency, rates):
    # 1. Check if both currencies exist in our rates
    # 2. Convert from the starting currency to chaos
    # 3. Then convert from chaos to the target currency
    pass

def main():
    # 1. Get the current rates
    rates = get_current_rates()
    
    # 2. Get user input for:
    #    - Amount they want to convert
    #    - Currency they're converting from
    #    - Currency they're converting to
    
    # 3. Show the result

if __name__ == "__main__":
    get_current_rates()