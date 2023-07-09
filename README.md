
# Tea Price Scraper

This Python script scrapes weekly tea prices from a website and saves the data to separate CSV files for each year. Tea Price Scraper: A Python script to scrape and save weekly tea prices from a website. This repository is for the first round of the selection process for the role of Intern - Data Engineering at BIPP, ISB.

## Requirements

- Python3 [Recommended](https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe)
- requests library [Pypi](https://pypi.org/project/requests/)
- pandas library [Pypi](https://pypi.org/project/pandas/)
- BeautifulSoup library [Pypi](https://pypi.org/project/beautifulsoup4/)
- Lxml [Pypi](https://pypi.org/project/lxml/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tea-price-scraper.git
   ```

2. Change to the project directory:

   ```bash
   cd tea-price-scraper
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Maintain the following project structure
   ```plaintext
      tea_price_scraper/
      ├── tea_price_scraper.py
      ├── README.md
      ├── requirements.txt
      └── scrapped_data/
      ```

## Usage

1. Open the `scrape_tea_prices.py` file.

2. Modify the range of years if needed:

   ```python
   # Iterate over each year from 2008 to 2023
   for year in range(2008, 2024):
   ```

3. Run the script:

   ```bash
   python scrape_tea_prices.py
   ```

4. The script will scrape the tea prices for the specified years and save the data to separate CSV files.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please create an issue.
