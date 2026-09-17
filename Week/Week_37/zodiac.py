# Import libraries
import pandas as pd
from datetime import datetime


# Load the spam dataset from CSV file
data = pd.read_csv("data/zodiac_signs.csv", sep=";")

print(data.head())
print(data.columns)

# Set up to find zodiac using datetime 
def find_zodiac(bday):
    for _, row in data.iterrows():

        start, end = row["date_range"].split(" - ")

        start = datetime.strptime(start, "%B %d")
        end = datetime.strptime(end, "%B %d")

        start_date = (start.month, start.day)
        end_date = (end.month, end.day)

        if start_date <= end_date:
            if start_date <= bday <= end_date:
                return row
        else:
            if bday >= start_date or bday <= end_date:
                return row


# Set up to find you zodiac using bday, your compatibility and incompatiblity
bday = input("Enter your birthday (MM-DD): ")

bday = datetime.strptime(bday, "%m-%d")
bday = (bday.month, bday.day)

result = find_zodiac(bday)

print("Your zodiac sign is:", result["zodiac_sign"])
print("You are compatible with:", result["compatible"])
print("You are incompatible with:", result["incompatible"])