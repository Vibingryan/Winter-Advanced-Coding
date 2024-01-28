import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    table = soup.find("table", class_="fsEventTable fsElementTable")
    rows = table.find_all("tr") if table else []
    events = []

    for row in rows[1:]:
        cells = row.find_all("td")
        event = {
            "opponent": cells[0].get_text(strip=True) if len(cells) > 0 else "N/A",
            "date": cells[1].get_text(strip=True) if len(cells) > 1 else "N/A",
            "result": cells[5].get_text(strip=True) if len(cells) > 5 else "N/A",
            # Add other details as needed
        }
        events.append(event)
    return events

def filter_events(events, past_or_future):
    filtered_events = []
    for event in events:
        if 'result' in event:
            if past_or_future == "1" and event['result'] != "N/A":  # Past events
                filtered_events.append(event)
            elif past_or_future == "2" and event['result'] == "N/A":  # Future events
                filtered_events.append(event)
    return filtered_events

def search_event(events, search_term):
    search_term_lower = search_term.lower()
    for event in events:
        if search_term_lower in event['opponent'].lower() or search_term_lower in event['date'].lower():
            return event
    return None

# Main program
url = "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/133"
events = scrape_data(url)

sport = input("Hello, what information are you accessing? (Type 'BVB' for boys varsity basketball): ")
if sport.lower() == 'bvb':
    choice = input("What information are you trying to find? 1. Past events 2. Future events: ")
    filtered_events = filter_events(events, choice)

    search_query = input("Type in the opponent school's name or the date: ")
    result = search_event(filtered_events, search_query)
    if result:
        print("Event Details:", result)
    else:
        print(f"No matching event found for search term: '{search_query}'.")
else:
    print("Currently, only information about boys varsity basketball (BVB) is available.")
