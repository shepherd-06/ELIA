import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for the NSF REU Sites search page
base_url = "https://www.nsf.gov/funding/initiatives/reu/search"

# Parameters to filter by "Computing" research area
params = {
    "f[0]": "reu_research_area:25737",
    "page": 0
}

# List to store all the scraped data
data = []

# Function to scrape a single page
def scrape_page(url, params):
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all REU site entries
    entries = soup.find_all('article', class_='reu-search__teaser')
    
    for entry in entries:
        title = entry.find('h3').text.strip()
        institution = entry.find('div', class_='reu-search-result__institution').text.strip()
        location = entry.find('div', class_='reu-search-result__location').text.strip()
        research_topics = entry.find('div', class_='reu-search-result__research_topics').text.strip()
        award_link = entry.find('a', text='Abstract of award')['href']
        
        # Extract contact information
        contacts = []
        contact_divs = entry.find_all('div', class_='reu-search-result__contact')
        for contact in contact_divs:
            name = contact.find('div', class_='reu-search-result__contact-name').text.strip()
            email = contact.find('a', href=True)
            email = email['href'].replace('mailto:', '') if email else ''
            contacts.append(f"{name} ({email})")
        
        # Append the data to the list
        data.append({
            'Title': title,
            'Institution': institution,
            'Location': location,
            'Research Topics': research_topics,
            'Award Link': award_link,
            'Contacts': ', '.join(contacts)
        })
    
    # Check if there is a next page
    next_page = soup.find('a', class_='pager__item--next')
    if next_page:
        next_page_url = base_url + next_page['href']
        scrape_page(next_page_url, {})

# Start scraping from the first page
scrape_page(base_url, params)

# Convert the data to a DataFrame and save it to a CSV file
df = pd.DataFrame(data)
df.to_csv('reu_computing_opportunities.csv', index=False)

print("Scraping completed and data saved to reu_computing_opportunities.csv")