# Key value pairs

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a valid key"))