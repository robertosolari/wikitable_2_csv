from bs4 import BeautifulSoup
import csv
import requests

url = "<wiki url>"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

title = soup.find('span', {'class': 'mw-page-title-main'}).get_text()
# Find the table
table = soup.find('table', {'class': 'wikitable'})

# Fetch each row
rows = table.find_all('tr')

# Open a CSV file to write to
with open(title+".csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")

    # Write data to CSV
    for row in rows:
        csv_row = []
        for cell in row.find_all(['td', 'th']):
            csv_row.append(cell.get_text().strip())
        writer.writerow(csv_row)
