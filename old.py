'''
Tea_Price_Scrapper 
This code is specifically designed for an internship at BIPP,ISB
This is a older version. The updated version of the code can be accessed from this link: 

Name: Subhashis Kar
Degree: Bachelor of Technology
Field of Study: Computer Science and Engineering
Year of Study: Final 
'''

import os                           # Importing the os module for working with file and directory paths
import requests                     # Importing the requests library for making HTTP requests
import pandas as pd                 # Importing the pandas library for working with dataframes
from bs4 import BeautifulSoup       # Importing the BeautifulSoup class from the bs4 module for HTML parsing


def scrape_tea_prices():
    """
    Scrapes weekly tea prices from a website for the range of years 2008 to 2023.
    It retrieves the webpage content, extracts table data, normalizes it, and saves it to separate CSV files for each year.
    """

    # Iterate over each year from 2008 to 2023
    for year in range(2008, 2024):
        # Make a request to the webpage for the specific year
        url = "https://www.teaboard.gov.in/WEEKLYPRICES/"
        url = url + str(year)
        response = requests.get(url)

        # Create a BeautifulSoup object using the lxml parser
        soup = BeautifulSoup(response.text,"lxml")

        # Find all the tables on the webpage
        tables = soup.find_all("table")

        # Scrape data from tables
        table_data = scrape_tables(tables)

        # Consolidate and normalize the data from all tables
        consolidated_data = consolidate_data(table_data)

        # Create a DataFrame from the consolidated data
        df = create_dataframe(consolidated_data)

        # Save the DataFrame to a CSV file
        save_to_csv(df, year)

def scrape_tables(tables):
    """
    Scrapes data from the provided tables by iterating over each table, extracting rows, and their respective cells.
    It skips tables with no data rows and stores the extracted data for each table.

    Args:
        tables (list): A list of table objects from BeautifulSoup.

    Returns:
        list: A list of tuples, where each tuple contains the headers and data for a table.
    """

    # List to store the data for all tables
    table_data = []

    # Iterate over each table
    for table in tables:
        # Find all rows in the table
        rows = table.find_all("tr")

        # Skip tables with no data rows
        if len(rows) <= 1:
            continue

        # List to store the data for the current table
        data = []

        # Extract the column names from the first row
        headers = [header.text.strip() for header in rows[0].find_all(["th", "td"])]

        # Determine the maximum number of columns
        max_columns = len(headers)

        # Iterate over the remaining rows
        for row in rows[1:]:
            # Extract the cells in the row
            cells = row.find_all(["th", "td"])

            # Skip rows with a different number of columns
            if len(cells) != max_columns:
                continue

            # Extract the values from the cells
            values = [cell.text.strip() for cell in cells]

            # Append the values to the table data
            data.append(values)

        # Append the table data to the main list
        table_data.append((headers, data))

    return table_data

def consolidate_data(table_data):
    """
    Consolidates and normalizes the data from all tables.
    It extracts the column names for normalization and creates tuples with identifier, column, and price.

    Args:
        table_data (list): A list of tuples containing headers and data for each table.

    Returns:
        list: A list of tuples, where each tuple contains identifier, column, and price.
    """

    # List to store the consolidated data from all tables
    consolidated_data = []

    for headers, data in table_data:
        # Extract the column names for normalization
        column_names = headers[1:]

        # Normalize the table data
        for row in data:
            identifier = row[0]
            prices = row[1:]
            consolidated_data.extend([(identifier, column, price) for column, price in zip(column_names, prices)])

    return consolidated_data

def create_dataframe(consolidated_data):
    """
    Creates a DataFrame from the consolidated data.

    Args:
        consolidated_data (list): A list of tuples containing identifier, column, and price.

    Returns:
        pandas.DataFrame: The DataFrame created from the consolidated data.
    """

    # Create a DataFrame from the consolidated data
    df = pd.DataFrame(consolidated_data, columns=["week", "location", "average_price"])
    return df


def save_to_csv(df, year):
    """
    Save the DataFrame to a CSV file in a specific directory.
    If the directory already exists, a new folder with a version number will be created.
    The user will be notified about the saved file and its directory.

    Args:
        df (pandas.DataFrame): The DataFrame to save as a CSV file.
        year (int): The year for which the data is being saved.

    Returns:
        None
    """

    # Create the "scraped_data" folder if it doesn't exist
    if not os.path.exists("scraped_data"):
        os.makedirs("scraped_data")

    # Generate the output file path
    output_folder = "scraped_data"
    output_file = str(year) + ".csv"
    output_path = os.path.join(output_folder, output_file)

    # Check if the file already exists in the folder
    if os.path.exists(output_path):
        version = 1
        while os.path.exists(output_path):
            # Increment the version number and update the output path
            version += 1
            output_file = f"{year}_v{version}.csv"
            output_path = os.path.join(output_folder, output_file)

    # Save the DataFrame to the CSV file
    df.to_csv(output_path, index=False)

    # Notify the user about the saved file and its directory
    print(f"Saved {output_file} to {os.path.abspath(output_folder)}")
    
def main():
    scrape_tea_prices()

if __name__ == "__main__":
    main()
