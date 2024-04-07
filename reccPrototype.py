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

personList = []
locationList = []

def setData():
    # starter data
    personList.append(Person("Person1", [0.20, 0.75, 0.60]))
    personList.append(Person("Person2", [0.40, 0.20, 0.50]))
    personList.append(Person("Person3", [0.90, 0.80, 0.35]))

    locationList.append(Location("Location1", [0.20, 0.20, 0.65]))
    locationList.append(Location("Location2", [0.50, 0.70, 0.80]))
    locationList.append(Location("Location3", [0.45, 0.60, 0.90]))
    locationList.append(Location("Location4", [0.25, 0.45, 0.20]))
    locationList.append(Location("Location5", [0.75, 0.30, 0.45]))

def findRecc():
    
    # starter formula
    reccLocation = "NONE"
    reccDiff = 100

    currDiff = 0
    user = personList[2]

    for loc in locationList:
        for att in range(len(loc.attributes)):
            currDiff += round(abs(user.preferences[att] - loc.attributes[att]),2)
        
       # print(loc.name, round(currDiff,2))
        if (currDiff < reccDiff):
            reccLocation = loc.name
            reccDiff = currDiff

        currDiff = 0
        

    print("User:", user.name)
    print("Reccomended Location:", reccLocation)
    
def load_locations_from_csv(csvfile):
    locations = []
    csv_df = pd.read_csv(csvfile)
    for x in range(0, len(csv_df)):
        row = csv_df.iloc[x].tolist()
        name = row[0]
        attributes = row[1:6]
        locations.append(Location(name, attributes))
    return locations

def main():

    # setData()
    # findRecc()
    
    a = load_locations_from_csv("locations.csv")
    print([b.attributes for b in a ])


    

if __name__ == "__main__":
    main()
