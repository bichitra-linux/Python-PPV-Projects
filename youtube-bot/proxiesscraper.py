import requests

def fetch_proxies():
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=no&anonymity=all'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch proxies. Status code: {response.status_code}")
        return []

    proxies = response.text.split('\n')
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return proxies

if __name__ == "__main__":
    proxies = fetch_proxies()
    if proxies:
        with open('proxies.txt', 'w') as f:
            for proxy in proxies:
                f.write(proxy + '\n')
        print(f"Fetched {len(proxies)} proxies and saved to proxies.txt")
    else:
        print("No proxies found.")
