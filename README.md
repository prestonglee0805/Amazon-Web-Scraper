# Amazon Web Scraper

## Description
This project is a web scraper for extracting product data from Amazon using Python. It allows users to fetch product details such as title, price, rating, and availability by providing a product URL. The scraper is designed to navigate Amazon's structure, extract relevant information, and output it in a structured format.

## Features
- Extracts product title, price, rating, and availability
- Supports multiple products by iterating through a list of URLs
- Saves extracted data to a CSV file for further analysis
- Uses BeautifulSoup and Requests for efficient web scraping

## Technologies Used
- **Python**: Core programming language
- **BeautifulSoup**: HTML parsing and data extraction
- **Requests**: Handling HTTP requests
- **Pandas**: Storing and processing scraped data

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/prestonglee0805/Amazon-Web-Scraper.git
   ```
2. Navigate into the project directory:
   ```sh
   cd Amazon-Web-Scraper
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you include your own **User-Agent** in the request headers to prevent getting blocked by Amazon. You can find your User-Agent by visiting [WhatIsMyUserAgent](https://www.whatismybrowser.com/detect/what-is-my-user-agent).
2. Update the `headers` dictionary in `scraper.py` with your User-Agent:
   ```python
   headers = {
       "User-Agent": "your-user-agent-here"
   }
   ```
3. Run the script by providing the product URL(s):
   ```sh
   python scraper.py
   ```
4. The extracted data will be saved in `output.csv`.

## Example Output
```
Product Name: Apple iPhone 13
Price: $799
Rating: 4.5
Availability: In Stock
```

## Notes
- Amazon frequently updates its site structure, so the scraper may need periodic updates.
- Ensure you comply with Amazon's terms of service when scraping data.
- Consider adding headers or using proxies to avoid being blocked.

## Future Enhancements
- Implement headless browsing with Selenium for dynamic content scraping
- Support for scraping multiple pages
- Integration with a database for better data management

## License
This project is licensed under the MIT License.

## Contact
For questions or improvements, feel free to reach out or submit a pull request!

GitHub: [prestonglee0805](https://github.com/prestonglee0805)
