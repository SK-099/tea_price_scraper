'''
Tea_Price_Scraper 

◉ This code is specifically designed for an internship at BIPP,ISB. 
◉ This is the modified code of the 'old.py' file which was updated in accordance with the conversation with the recruiting manager for the intended internship role.

Name: Subhashis Kar
Degree: Bachelor of Technology
Field of Study: Computer Science and Engineering
Year of Study: Final 
'''

import requests                  # Import the requests library, which allows us to make HTTP requests.
import pandas as pd              # Import the pandas library, which allows us to work with dataframes.
from bs4 import BeautifulSoup    # Import the BeautifulSoup library, which allows us to parse HTML.

class TeaPricesScraper:
    def __init__(self):
        self.consolidated_data = pd.DataFrame(columns=["week", "location", "average_price"])    # Initialize a pandas dataframe to store the scraped data.

    def scrape_data(self, year):
        """
        Scrapes the tea prices data from the website https://www.teaboard.gov.in/WEEKLYPRICES/ for the given year.

        Args:
            year: The year to scrape the data for.

        Returns:
            None.
        """
        url = "https://www.teaboard.gov.in/WEEKLYPRICES/" + str(year)    # Construct the URL for the year we want to scrape.
        response = requests.get(url)    # Make the HTTP request.

        soup = BeautifulSoup(response.text, "lxml")    # Parse the HTML response.

        tables = soup.find_all("table")    # Find all the tables on the page.

        if len(tables) < 2:
            """
            If there are less than two tables on the page, then there is no data for that year.
            """
            return    # If there are less than 2 tables, return.

        table = tables[1]    # The second table contains the tea prices data.

        rows = table.find_all("tr")    # Find all the rows in the table.

        if len(rows) <= 1:
            """
            If there is only one row on the table, then there is no data for that year.
            """
            return    # If there is only one row, return.

        data = []    # Initialize a list to store the scraped data.

        headers = [header.text.strip() for header in rows[0].find_all(["th", "td"])]    # Get the headers from the first row.

        max_columns = len(headers)    # Store the number of columns in the table.

        for row in rows[1:]:
            cells = row.find_all(["th", "td"])    # Find all the cells in the row.

            if len(cells) != max_columns:
                """
                If the number of columns in a row is not the same as the number of columns in the first row, then skip that row.
                """
                continue    # If the number of cells in the row is not the same as the number of columns, skip this row.

            values = [cell.text.strip() for cell in cells]    # Get the values from the cells.

            data.append(values)    # Add the values to the list.

        df = pd.DataFrame(data, columns=headers)    # Create a pandas dataframe from the list.

        df["week"] = df.iloc[:, 0]    # Set the first column as the week number.

        df_transformed = df.melt(id_vars="week", value_vars=headers[1:], var_name="location", value_name="average_price")    # Melt the dataframe to long format.

        self.consolidated_data = pd.concat([self.consolidated_data, df_transformed], ignore_index=True)    # Add the dataframe to the consolidated dataframe.

    def save_data(self, filename):
        """
        Saves the consolidated data to a CSV file.

        Args:
            filename: The name of the CSV file to save the data to.

        Returns:
            None.
        """
        self.consolidated_data.to_csv(filename, index=False)    # Save the dataframe to a CSV file.


if __name__ == "__main__":
    scraper = TeaPricesScraper()

    for year in range(2008, 2024):
        scraper.scrape_data(year)

    scraper.save_data("scraped_data.csv")
