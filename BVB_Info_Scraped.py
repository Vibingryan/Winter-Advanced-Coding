import requests
from bs4 import BeautifulSoup

url = "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/133"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# Find the table with sports event details
table = soup.find("table", class_="fsEventTable fsElementTable")

# Extract all rows from the table
rows = table.find_all("tr")

for row in rows[1:]:
    cells = row.find_all("td")

    # Extracting details from each cell
    opponent = cells[0].get_text(strip=True) if len(cells) > 0 else "N/A"
    date = cells[1].get_text(strip=True) if len(cells) > 1 else "N/A"
    time = cells[2].get_text(strip=True) if len(cells) > 2 else "N/A"
    location = cells[3].get_text(strip=True) if len(cells) > 3 else "N/A"
    result = cells[5].get_text(strip=True) if len(cells) > 5 else "N/A"
    score = cells[6].get_text(strip=True) if len(cells) > 6 else "N/A"

    print(f"Opponent: {opponent}, Date: {date}, Time: {time}, Location: {location}, Result: {result}, Score: {score}")

# When no data was found
if not rows:
    print("No sports event data found.")
