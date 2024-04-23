import requests
from bs4 import BeautifulSoup
import os

def scrape_website():
    # Take user input for the URL
    url = input("Enter the URL of the website you want to scrape: ")

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve page:", e)
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Take user input for the HTML tag to search for
    tag = input("Enter the HTML tag you want to search for (e.g., 'a', 'p', 'div'): ")

    # Find elements based on the user-specified tag
    elements = soup.find_all(tag)

    if len(elements) == 0:
        print("No elements found with the specified tag.")
        return

    # Take user input for the attributes to extract (comma-separated)
    attributes = input("Enter the attribute(s) you want to extract (e.g., 'href', 'src'): ").split(',')

    # Create a dictionary to store extracted data
    extracted_data = {}

    # Extract data from the elements
    for attribute in attributes:
        extracted_data[attribute] = []

    for element in elements:
        for attribute in attributes:
            if attribute in element.attrs:
                extracted_data[attribute].append(element[attribute])
            else:
                print(f"No '{attribute}' attribute found for the element:", element)

    # Print extracted data
    print("Extracted data:")
    for attribute, values in extracted_data.items():
        print(f"{attribute}: {values}")

    # Generate a default filename based on the URL
    default_filename = "extracted_data.txt"
    if '/' in url:
        default_filename = url.split('/')[-1].split('.')[0] + "_extracted_data.txt"

    # Ask user if they want to save the extracted data to a file
    save_to_file = input(f"Do you want to save the extracted data to '{default_filename}'? (yes/no): ").lower()

    if save_to_file == 'yes':
        filename = input("Enter the filename (with extension) to save the data (or press Enter to use default): ")
        if not filename:
            filename = default_filename
        try:
            with open(filename, 'w') as f:
                for attribute, values in extracted_data.items():
                    f.write(f"{attribute}:\n")
                    for value in values:
                        f.write(f"\t{value}\n")
            print(f"Extracted data saved to {filename}")
        except Exception as e:
            print("Failed to save extracted data:", e)


scrape_website()
