# Winter-Advanced-Coding Work log
Week 0 
Reviewed Python watching youtube video (It is in Korean)
- https://www.youtube.com/watch?v=zAkAZjmnS3c&list=PLU9-uwewPMe05-khW3YcDEaHMk_qA-7lI&index=3
- https://www.youtube.com/watch?v=09KG7YsGuv4&list=PLU9-uwewPMe05-khW3YcDEaHMk_qA-7lI&index=4
Watched and practiced variables, list, tuple, dictionary, etc. 
Brainstormed projects I can start working on next week
Some candidates were..
- Recipe book(you can add/edit/recommend recipes.
- Personal blog utilizing Flask
- Expense tracker(input expenses, categorize, and generate report)
Week 1
Reviewed the use of Class in Python with Youtube videos (https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
Finished the first version of my recipe book app (I might add some more features)

Week 2
For 3 hours, I tried to play around with while and if functions while making it. I created a simple hangman game that allows players to guess the word or the letter. I created a separate word list that I would import to the main file. 

Week 3
I started watching youtube video (https://youtu.be/yQ20jZwDjTE?si=R5s7R_JyxZRangFC)that explains webscraping and learned what it is and the fundamentals behind it. I learned how to use BeautifulSoup to do the webscraping. I also tried short practice code that would get info from Pomfret School website. I am trying to use the informations I gained to create code that would get informations from the school website that could be useful.

Week 4
I started off with continuing to watch the youtube video over again to grasp more concept of how to utilize the Beautifulsoup, and started to add on to the basic structure of Beautiful Soup method. 
My code faced two problems:
1. When I first ran the code at the beginning(when I didn't set up the for loops yet) the code executed an error saying: "requests.exceptions.connectionerror"
After some research, I found that one way to solve this problem is to add "User Agent" so the website will acknoledge this code as an actual user connecting to it. I could just serach up on google to find what my User Agent was and added a line that indicated my User Agent to the code: "headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}"
Problem 1 was resolved.
2. Second problem was to figure out how to form a for loop that would extract information from each setions(ex) Date, Time, Location, etc..) So in the for loop, I decided to use ternary operator and separated each sections to assign each sections values. So for example for code "opponent = cells[0].get_text(strip=True) if len(cells) > 0 else "N/A""
cell[0] accesses the first cell in this list, .get_text() is Beautiful soupd method, and lens(cells) is a conditional check of having at least one cell in the row.
Problem 2 was resolved. 

The result was successfully executed as the following: 

Opponent: vs.Victory Christian, Date: SatNov18, Time: 1:45PM, Location: Pomfret School - Main Lewis Gym, Result: , Score: 
Opponent: vs.Frederick Gunn School, Date: SatDec2, Time: 3:00PM, Location: Frederick Gunn School, Result: Win, Score: 76-59
Opponent: Scholar Round Ball v. Newman AA, Date: FriDec8, Time: 2:00PM, Location: Eastern Nazarene College, Result: Win, Score: 74-63
Opponent: vs.Millbrook School, Date: SatDec9, Time: 5:00PM, Location: Pomfret School - Main Lewis Gym, Result: Loss, Score: 66-68
Opponent: Hotchkiss @ Hoopsfest, Date: WedDec13, Time: 4:30PM, Location: , Result: Loss, Score: 61-63
Opponent: IMG Academy @ Hoopsfest, Date: ThuDec14, Time: 1:15PM, Location: , Result: Win, Score: 74-72
Opponent: vs.Roxbury Latin School, Date: FriJan5, Time: 6:00PM, Location: Roxbury Latin, Result: Win, Score: 67-49
Opponent: vs.Governor's Academy, Date: SatJan6, Time: 3:45PM, Location: Governor's Academy, Result: Loss, Score: 66-68
Opponent: TopFlight (CA) @ Hoophall Prep Shpwcase, Date: FriJan12, Time: 5:45PM, Location: American International College, Result: Win, Score: 69-67
Opponent: vs.Kingswood-Oxford School, Date: SatJan13, Time: 1:00PM, Location: Pomfret School - Main Lewis Gym, Result: Loss, Score: 49-54
Opponent: vs.Groton School, Date: WedJan17, Time: 3:30PM, Location: Groton School, Result: Win, Score: 98-47
Opponent: vs.Marianapolis Preparatory, Date: FriJan19, Time: 7:00PM, Location: Marianapolis Preparatory, Result: Win, Score: 77-66
Opponent: vs.Frederick Gunn School, Date: SatJan20, Time: 2:30PM, Location: Pomfret School - Main Lewis Gym, Result: Win, Score: 73-55
Opponent: vs.St. Mark's School, Date: WedJan24, Time: 5:00PM, Location: St. Mark's School, Result: , Score: 
Opponent: vs.Canterbury School, Date: SatJan27, Time: 3:00PM, Location: Pomfret School - Main Lewis Gym, Result: , Score: 
Opponent: vs.Williston Northampton, Date: WedJan31, Time: 2:30PM, Location: Williston Northampton, Result: , Score: 
Opponent: vs.Westminster School, Date: WedFeb7, Time: 3:15PM, Location: Pomfret School - Main Lewis Gym, Result: , Score: 
Opponent: vs.Marianapolis Preparatory, Date: FriFeb9, Time: 7:00PM, Location: Pomfret School - Main Lewis Gym, Result: , Score: 
Opponent: vs.Portsmouth Abbey, Date: SatFeb10, Time: 2:30PM, Location: Pomfret School - Main Lewis Gym, Result: , Score: 
Opponent: vs.Beaver Country Day School, Date: WedFeb14, Time: 4:00PM, Location: Beaver Country Day School, Result: , Score: 
Opponent: vs.Rivers School, Date: SatFeb17, Time: 3:00PM, Location: Pomfret School - Main Lewis Gym, Result: , Score: 
Opponent: vs.Suffield Academy, Date: MonFeb19, Time: 5:00PM, Location: Suffield Academy, Result: , Score: 
Opponent: vs.Cheshire Academy, Date: WedFeb21, Time: 3:30PM, Location: Cheshire Academy, Result: , Score: 
Opponent: vs.New York Military Academy, Date: SatFeb24, Time: 2:00PM, Location: New York Military Academy, Result: , Score: 

However, this code only scrapes from a single page of BVB team. And my optimal goal is to create a code that scrapes from multiple webpages, which would include all the sports team, and would return information that the users want to know about. So I am planning to learn how to scrape info from multiple pages and utlize them accordingly. 

Week 5

1. The initial version of the script was a basic implementation, solely focused on extracting and displaying sports event data from a specific webpage. Recognizing the potential for enhanced functionality, I used data retrieval process within a `scrape_data` function. This not only streamlined the code but also improved its maintainability. I now sectionalized the code via functions so the code is now more straighforward. I also added features for users to actively engage with the script, specifying their interests, particularly in boys varsity basketball events.(Other teams are going to be added soon but atm I'm just dealing with the info scraped from BVB) 

2. For the search functionality lots of changes were made. Initially, the script required exact matches for user inputs, which proved to be limiting. To address this, I implemented a more flexible search algorithm, capable of understanding case-insensitive inputs and partial name matches. I wanted to make the code understand the user input like "millbrook" referring to its full name "Millbrook School." 

Following are the results: 
/Users/minseokim/PycharmProjects/Findgame/venv/bin/python /Users/minseokim/PycharmProjects/Findgame/main.py
Hello, what information are you accessing? (Type 'BVB' for boys varsity basketball): bvb
What information are you trying to find? 1. Past events 2. Future events: 1
Type in the opponent school's name or the date: Millbrook School
Event Details: {'opponent': 'vs.Millbrook School', 'date': 'SatDec9', 'result': 'Loss'}

Process finished with exit code 0

My future goal is 1. Add more teams for the options. 2. Implement datetime module to use the real time as a parameter to determine whether the event is in the past or the future. 3. Make the returning values more concise and straightforward output. 4. Stress test the code and debug



Week 6 - 7

First thing I focused on was to add other team’s info since it could only grab info from one page about the boys' varsity basketball team in the previous version. My goal was to make this tool way more useful by getting it to work for all the sports teams at our school. So, I got to work on making the scraper smart enough to go through a bunch of different pages, each for a different sports team. That is why I created a dictionary full of urls that the code will retrieve info from:

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

I made sure the code will pick up the right thing from the user’s response to get from team_urls dictionary, so I added .upper function to ensure it picks up when the user answered in the lower case form. 

I had to figure out how to make the scraper visit each team's page one by one and grab all the info we needed. This step was super important because it meant our tool could give us details on not just basketball but every sport. It was lucky that the logic I all ready created in the preivous version applies same with other team's pages, so I only had to add the urls in order for the code to figure out what page to get the information from.

Besides adding new features, I also spent time making sure the tool worked better overall. I wrote a special part of the code (`get_win_loss_record`) that calculates how many games a team won or lost and their winning percentage. This was a neat addition because it summarized a team's performance in a simple way. I also made sure the code was clean and easy to understand, so if we need to add more stuff later, it won't be a headache.

Now, it could get info on any sports team at our school, not just basketball. This was a big win because it meant our tool was way more helpful than before. Now only thing left is the stress test it and debug. 
 
