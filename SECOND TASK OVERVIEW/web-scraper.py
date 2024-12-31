import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(base_url, pages=1):
    all_data = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        response = requests.get(f"{base_url}?page={page}")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Adjust selectors based on the website structure
        products = soup.select('.product-title')
        prices = soup.select('.product-price')
        images = soup.select('.product-image img')
        ratings = soup.select('.product-rating')

        for i in range(len(products)):
            product_name = products[i].text.strip()
            price = prices[i].text.strip()
            image_url = images[i]['src']
            rating = ratings[i].text.strip() if i < len(ratings) else "N/A"
            all_data.append({
                'Product Name': product_name,
                'Price': price,
                'Image URL': image_url,
                'Rating': rating
            })

    # Save the data
    df = pd.DataFrame(all_data)
    df.to_csv('scraped_data.csv', index=False)
    df.to_json('scraped_data.json', orient='records')
    print("Scraping complete! Data saved to 'scraped_data.csv' and 'scraped_data.json'.")

# User input
website_url = input("Enter the website URL (e.g., https://example.com/products): ")
number_of_pages = int(input("Enter the number of pages to scrape: "))
scrape_website(website_url, number_of_pages)