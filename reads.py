# SFHACKS2024 Project
# Reccomender Prototype
import pandas as pd

# TODO Input using csv files
# TODO Max attributes: 5

class Person:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences

class Location:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


user : Person
locationList = []
    
def load_locations_from_csv(csvfile):
    locations = []
    csv_df = pd.read_csv(csvfile)
    for x in range(0, len(csv_df)):
        row = csv_df.iloc[x].tolist()
        name = row[0]
        attributes = row[1:6]
        locations.append(Location(name, attributes))
    return locations

def load_user_from_csv(csvfile):
    csv_df = pd.read_csv(csvfile)
    for x in range(0, len(csvfile)):
        row = csv_df.iloc[x].tolist()
        name = row[0]
        preferences = row[1:6]
        return Person(name, preferences)

def save_locations_from_csv(csvfile: str):
    
    return


def main():

    # setData()
    # findRecc()
    
    loc = load_locations_from_csv("locations.csv")
    user = load_user_from_csv("user.csv")
    print(user.name)


    

if __name__ == "__main__":
    main()
