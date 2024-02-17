import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# Get info
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

# Function that calculates the win rate
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

# Show Results
def display_results():
    sport = team_var.get()
    if sport in team_urls:
        url = team_urls[sport]
        events = scrape_data(url)

        result_text = ""
        if choice_var.get() == 'schedule':
            result_text += f"Schedule for {sport}:\n"
            for event in events:
                result_text += f"Opponent: {event['opponent']}, Date: {event['date']}, Result: {event.get('result', 'N/A')}\n"
        elif choice_var.get() == 'record':
            wins, losses, win_rate = get_win_loss_record(events)
            result_text += f"For {sport}, They won {wins} games and lost {losses} games. \nWin rate: {win_rate:.2f}%."
    else:
        result_text = "Currently, information is not available for the selected team."

    results_textbox.config(state=tk.NORMAL)
    results_textbox.config(font = ('Arial', 22))
    results_textbox.delete("1.0", tk.END)  # To clear the textbox everytime the user presses display button
    results_textbox.insert(tk.END, result_text)
    results_textbox.config(state=tk.DISABLED)


# Tkinter setup Used Resources: https://realpython.com/python-gui-tkinter/#displaying-text-and-images-with-label
# https://www.youtube.com/watch?v=ibf5cx221hk

# Initialize the tkinter window
root = tk.Tk()
root.title("Pomfret School Sports Team Information")

# Load the image and create an image label widget
logo_path = "/Users/minseokim/PycharmProjects/FinalPJ/pomfretlogo.png" # Pomfret logo image file path
logo_image = PhotoImage(file=logo_path)
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()


team_var = tk.StringVar()
choice_var = tk.StringVar(value="schedule")

# URL dictionary
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

tk.Label(root, text="Select a team:").pack()
team_dropdown = ttk.Combobox(root, textvariable=team_var, values=list(team_urls.keys()), state="readonly")
team_dropdown.pack()

# User selects what type of info they want to get
tk.Label(root, text="Choose information type:").pack()
ttk.Radiobutton(root, text="Schedule", variable=choice_var, value="schedule").pack()
ttk.Radiobutton(root, text="Win/Loss Record", variable=choice_var, value="record").pack()
ttk.Button(root, text="Display Results", command=display_results).pack()

# Sizing the pop-up screen
results_textbox = tk.Text(root, fg="red", height=30, width=150, state=tk.DISABLED)
results_textbox.pack()

root.mainloop()
