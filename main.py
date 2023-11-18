import requests
import sys
import csv

from interfaces import BalanceResponse

# Normally I'd create a .env file and secrets from there
# but this is a test token
API_KEY = 'D6HFJ69KZZ23JN8EP86KJPBVE3NKHP5BSR'
BASE_URL = 'https://api.etherscan.io/api'


def get_crypto_balance_by_address(address: str, tag: str="latest") -> BalanceResponse:
    """
    Get the ethereum balance for a specific address
    https://docs.etherscan.io/api-endpoints/accounts
    """
    
    endpoint = f'{BASE_URL}?module=account&action=balancemulti&address={address}&apikey={API_KEY}&tag={tag}'
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()

def write_to_csv(data: BalanceResponse, csv_filename: str, address: str):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['address', 'balance']  # Add more fields as needed
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data["result"]:
            writer.writerow({
                'address': item['account'],
                'balance': item['balance'],
            })

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <crypto_address>")
        sys.exit(1)

    crypto_address = sys.argv[1]
    crypto_data = get_crypto_balance_by_address(crypto_address)

    if crypto_data:
        csv_filename = 'ethereum.csv'
        write_to_csv(crypto_data, csv_filename, crypto_address)
        print(f"Data written to {csv_filename}")
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    # It's best practice in Python to have a main() function
    # to isolate code from the global scope
    # and initialize it with the thunder name check
    # if it's not used as a module
    main()
