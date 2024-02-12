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
        }
        events.append(event)
    return events

def get_win_loss_record(events):
    wins = 0
    losses = 0
    for event in events:
        if 'W' in event['result']:
            wins += 1
        elif 'L' in event['result']:
            losses += 1
    total_games = wins + losses
    win_rate = (wins / total_games * 100) if total_games > 0 else 0
    return wins, losses, win_rate


# Updated team URLs with all teams added
team_urls = {
    "BVB": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/133",
    "BJVB": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/132",
    "GVB": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/135",
    "GJVB": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/134",
    "BVH": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/147",
    "BJVH": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/146",
    "GVH": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/149",
    "GJVH": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/148",
    "BVS": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/160",
    "BJVS": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/159",
    "GVS": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/162",
    "GJVS": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/161",
    "VW": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/170",
    "VS": "https://www.pomfret.org/athletics/team-pages/~athletics-team-id/176",
}

sport = input("Hello, which team are you interested in? (e.g., 'BVB' for boys varsity basketball): ").upper()
if sport in team_urls:
    url = team_urls[sport]
    events = scrape_data(url)

    choice = input("Do you want to see the whole schedule or the win/loss record? (Type 'schedule' or 'record'): ").lower()
    if choice == 'schedule':
        print(f"Schedule for {sport}:")
        for event in events:
            print(f"Opponent: {event['opponent']}, Date: {event['date']}, Result: {event.get('result', 'N/A')}")
    elif choice == 'record':
        wins, losses, win_rate = get_win_loss_record(events)
        print(f"For {sport}, Won {wins} games, lost {losses} games. Win rate: {win_rate:.2f}%.")
    else:
        print("Invalid choice. Please type 'schedule' or 'record'.")
else:
    print("Currently, information is not available for the selected team.")
