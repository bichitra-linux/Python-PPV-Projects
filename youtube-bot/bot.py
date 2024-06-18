import requests
import random
import time

# Load proxies from file
def load_proxies(filename):
    with open(filename, 'r') as f:
        proxies = f.readlines()
    proxies = [proxy.strip() for proxy in proxies]
    return proxies

# Load user-agents from file
def load_user_agents(filename):
    with open(filename, 'r') as f:
        user_agents = f.readlines()
    user_agents = [ua.strip() for ua in user_agents]
    return user_agents

# Get a random proxy
def get_random_proxy(proxies):
    proxy = random.choice(proxies)
    return {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    }

# Get a random user-agent
def get_random_user_agent(user_agents):
    return random.choice(user_agents)

# Make a request using a random proxy and user-agent
def view_video(url, proxies, user_agents):
    proxy = get_random_proxy(proxies)
    user_agent = get_random_user_agent(user_agents)
    headers = {
        'User-Agent': user_agent
    }
    try:
        response = requests.get(url, proxies=proxy, headers=headers, timeout=10)
        print(f"Using proxy: {proxy}, User-Agent: {user_agent}, Status Code: {response.status_code}")
        if response.status_code == 200:
            watch_duration = random.uniform(60, 200)
            print(f"Watching video for {watch_duration} seconds")
            time.sleep(watch_duration)
            print("Video viewed successfully")
        else:
            print("Failed to view video")
    except requests.exceptions.RequestException as e:
        print(f"Error using proxy: {proxy}, {e}")

def main():
    video_url = 'https://www.youtube.com/watch?v=Zg-3bVRpkNo'
    proxies = load_proxies('proxies.txt')
    user_agents = load_user_agents('useragents.txt')
    for _ in range(20):  # Number of views you want
        view_video(video_url, proxies, user_agents)
        time.sleep(random.uniform(1, 5))  # Wait between requests

if __name__ == '__main__':
    main()
