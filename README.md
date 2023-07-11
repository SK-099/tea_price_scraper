<h1 align="center">Hi 👋, I'm Subhashis Kar</h1>
<p align="center">
<picture>
<img src="https://github.com/SK-099/tea_price_scraper/assets/93715697/93dd7f1a-fa39-4b2f-9a0b-945257b28156" width=15%>
</picture>
</p>
<h3 align="center">A passionate research oriented student from Howrah</h3>
<p align="center">
<picture>
<img src="https://komarev.com/ghpvc/?username=sk-099&label=Profile%20views&color=0e75b6&style=flat" alt="sk-099" />
</picture>
</p>




- 🌱 I’m currently learning **Data Science, Quantum Computing**

- 👯 I’m looking to collaborate on any project on **Quantum Computing or Image Processing.**

- 💬 Ask me about **Scikit-Image,Seaborn,Pandas,Matplotlib,Scipy,Numpy**

- 📫 How to reach me **subhashiskar454@gmail.com**

---

<h3 align="center">About this Repository</h3> 

# Tea Price Scraper

This Python script scrapes weekly tea prices from a website and saves the data to separate CSV files for each year. Tea Price Scraper: A Python script to scrape and save weekly tea prices from a website. This repository is for the first round of the selection process for the role of Intern - Data Engineering at BIPP, ISB.

## Requirements
* [`Python3`](https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe)
* [`requests` library](https://pypi.org/project/requests/)
* [`pandas` library](https://pypi.org/project/pandas/)
* [`beautifulsoup` library](https://pypi.org/project/beautifulsoup4/)
* [`lxml` parser](https://pypi.org/project/lxml/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SK-099/tea-price-scraper.git
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
      └── requirements.txt
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
