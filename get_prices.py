import requests

import requests

url = 'https://apiv2.nobitex.ir/v3/orderbook/USDTIRT'

try:
    # sending GET request
    response = requests.get(url)
    
    # Check if the request was successfull
    response.raise_for_status()
    
    # Formatting the answer
    data = response.json()
    
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Connection Error: {e}")
