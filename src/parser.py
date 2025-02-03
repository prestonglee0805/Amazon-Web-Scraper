import pandas as pd
from bs4 import BeautifulSoup

def parse_amazon_products(soup):
    """Extract product details from Amazon search page"""
    if not soup:
        return None
    
    products = []
    items = soup.find_all('div', {'data-component-type': 's-search-result'})  

    for item in items:
        # Product Name Extraction
        name_tag = item.find('h2')
        product_name = name_tag.get_text(strip=True) if name_tag else "N/A"

        # Price Extraction (Amazon often splits price into two spans)
        whole_price = item.find('span', {'class': 'a-price-whole'})
        fraction_price = item.find('span', {'class': 'a-price-fraction'})
        price_num = (whole_price.get_text(strip=True) + "." + fraction_price.get_text(strip=True)) if whole_price and fraction_price else "N/A"

        # Rating Extraction
        rating_tag = item.find('span', {'class': 'a-icon-alt'})
        rating_num = rating_tag.get_text(strip=True).split()[0] if rating_tag else "N/A"

        # Review Count Extraction
        review_count_tag = item.find('span', {'class': 'a-size-base'})
        review_count = review_count_tag.get_text(strip=True) if review_count_tag else "0 Reviews"

        # Product URL Extraction
        link_tag = item.find('a', {'class': 'a-link-normal'}, href=True)
        product_link = "https://www.amazon.com" + link_tag['href'] if link_tag else "N/A"

        # Availability Check
        availability_tag = item.find('span', {'class': 'a-declarative'})
        availability = "In Stock" if availability_tag else "Out of Stock"

        products.append({
            'Product Name': product_name,
            'Price': price_num,
            'Rating': rating_num,
            'Review Count': review_count,
            'Availability': availability,
            'Product Link': product_link
        })
    
    return pd.DataFrame(products)
