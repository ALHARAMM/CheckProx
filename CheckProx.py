import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

print(r"""
# +================================================+
# |  ____ _               _    ____                |
# | / ___| |__   ___  ___| | _|  _ \ _ __ _____  __|
# || |   | '_ \ / _ \/ __| |/ / |_) | '__/ _ \ \/ /|
# || |___| | | |  __/ (__|   <|  __/| | | (_) >  < |
# | \____|_| |_|\___|\___|_|\_\_|   |_|  \___/_/\_\|
# +================================================+
v1.4
Copyright: @ALHARAM
""")

# Path to the file containing proxies
proxy_file_path = input("Enter The Proxies File Path: ")
# URL to test the proxies
test_url = 'http://www.google.com'

def read_proxies(file_path):
    """Read proxies from a file and return a list."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def test_proxy(proxy):
    """Test if a proxy is valid by making a request to the test URL."""
    try:
        response = requests.get(test_url, proxies={'http': proxy, 'https': proxy}, timeout=3)
        if response.status_code == 200:
            return proxy  # Return the valid proxy
    except requests.RequestException:
        return None  # Return None if the proxy fails

def main():
    proxies = read_proxies(proxy_file_path)
    valid_proxies = []

    if not proxies:
        return  # Exit if no proxies were loaded

    # Use ThreadPoolExecutor for concurrent requests
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_proxy = {executor.submit(test_proxy, proxy): proxy for proxy in proxies}
        
        for future in as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            result = future.result()
            if result:
                valid_proxies.append(result)
                print(f'Proxy is valid: {result}')
            else:
                print(f'Proxy is invalid: {proxy}')

    # Output results
    print("\nValid proxies:")
    if valid_proxies:
        for valid_proxy in valid_proxies:
            print(valid_proxy)
    else:
        print("No valid proxies found.")

    # Save valid proxies to a new file
    if valid_proxies:
        with open('Valid_Proxies.txt', 'w') as file:
            file.write("\n".join(valid_proxies) + '\n')

if __name__ == "__main__":
    main()
