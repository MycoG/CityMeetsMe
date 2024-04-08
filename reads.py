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
    def __init__(self, name, exts, attributes):
        self.name = name
        self.exts = exts
        self.attributes = attributes

user : Person
locationList = []

#[name, ext1, ext2, ext3, ext4, ext5, attr1, attr2, attr3]
    
def load_locations_from_csv(csvfile):
    locations = []
    with open(csvfile, "r") as f:
        for line in f.readlines()[1:]:
            line = line.strip().split(",")
            name = line[0]
            exts = line[1:4]
            attrs = line[4:7]
            locations.append(Location(name, exts, attrs))
    return locations

def load_user_from_csv(csvfile):
    with open(csvfile, "r") as f:
        line = f.readline()
        line = line.strip().split(",")
        name = line[0]
        attrs = line[1:4]
        return Person(name, attrs)

def save_locations_to_csv(locations, csvfile: str):
    with open(csvfile, "w") as f:
        for loc in locations:
            f.write(",".join([loc.name] + [str(a) for a in loc.exts] + [str(a) for a in loc.attributes])+"\n")

def save_person_to_csv(person, csvfile: str):
    with open(csvfile, "w") as f:
        f.write(",".join([person.name] + [str(a) for a in person.attributes])+"\n")

def main():

    
    loc = load_locations_from_csv("locations.csv")
    user = load_user_from_csv("user.csv")
    for x in loc:
        print(x.name)
        print(x.exts)
        print(x.attributes)
    print(user.name)
    print(user.preferences)


if __name__ == "__main__":
    main()
