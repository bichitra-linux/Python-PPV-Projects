import requests
from bs4 import BeautifulSoup
import os

# List of governmental websites in Nepal
websites = [
    'https://mohp.gov.np/news/latest-news-notice-and-circulars/en/',
    # Add more websites here
]

# Function to scrape notices from a website
def scrape_notices(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception if the request was unsuccessful
    except (requests.RequestException, ValueError):
        print(f"Failed to connect to {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the elements containing notices
    notices = soup.find_all('a', class_='notice-link')
    
     # Download and save each notice
    for notice in notices:
        notice_title = notice.text.strip()
        notice_url = notice['href']
        
        # Create a directory for each website if it doesn't exist
        website_name = url.split('//')[1].split('.')[0]
        if not os.path.exists(website_name):
            os.makedirs(website_name)
        
        # Download and save the notice
        try:
            response = requests.get(notice_url)
            response.raise_for_status()  # Raise exception if the request was unsuccessful
        except (requests.RequestException, ValueError):
            print(f"Failed to download notice from {notice_url}")
            continue

        with open(f'{website_name}/{notice_title}.pdf', 'wb') as file:
            file.write(response.content)
        
        print(f'Saved notice: {notice_title}')
    
# Scrape notices from each website
for website in websites:
    scrape_notices(website)