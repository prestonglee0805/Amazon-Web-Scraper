import sys
import os

# Dynamically add `src/` to Python’s import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Now you can import modules correctly
from scraper import fetch_amazon_page
from parser import parse_amazon_products
from database import save_to_csv

def main():
    print("Amazon Product Scraper")
    amazon_url = input("Enter an Amazon search results URL: ").strip()

    if not amazon_url.startswith("https://www.amazon."):
        print("Invalid Amazon URL! Please enter a valid Amazon search results page link.")
        return
    
    soup = fetch_amazon_page(amazon_url)
    if soup:
        df = parse_amazon_products(soup)

        if df is None or df.empty:
            print("⚠️ No products found! Ensure you're entering a valid Amazon search results page.")
        else:
            print("\n Scraped Product Data:")
            print(df)

            # Save to CSV
            save_to_csv(df, "data/Amazon_Products.csv")
            print("\n💾 Data saved to 'data/Amazon_Products.csv'")

if __name__ == "__main__":
    main()
