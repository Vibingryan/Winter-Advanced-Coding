month_conversion = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "July",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "Decemeber"
}
fav_month = input("What is your favorite month? (Write in abbreviation): ")
print("I agree that " + month_conversion.get(fav_month) + " is a good month!")