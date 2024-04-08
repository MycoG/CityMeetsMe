from reads import Person, Location, load_locations_from_csv, load_user_from_csv
import math

# End List of Locations example
# [name, ext1, ext2, ext3, attr1, attr2, attr3]

# Using given user and list of locations calculate score for each location
def findRecc(user, locationList):
    scoreList = []

    # Iterate through each location
    for loc in locationList:
        # attr1 diff
        k1 = abs(float(user.preferences[0]) - float(loc.attributes[0]))
        # attr val
        a1 = abs((math.exp(k1) - 1)/(1 - math.exp(1)))

        # attr2 diff
        k2 = abs(float(user.preferences[1]) - float(loc.attributes[1]))
        # attr2 val
        a2 = abs((math.exp(k2) - 1)/(1 - math.exp(1)))

        # attr3 diff
        k3 = abs(float(user.preferences[2]) - float(loc.attributes[2]))
        # attr3 val
        a3 = abs((math.exp(k3) - 1)/(1 - math.exp(1)))

        # total attr value
        aPoints = a1 + a2 + a3

        safeWT = 1
        cleanWT = 1
        serveWT = 1

        # Convert extras to weights
        # Safety Weight
        if (float(loc.exts[0]) <= 0.3):
            safeWT = 1.3
        elif (float(loc.exts[0]) <= 0.6):
            safeWT = 1.15

        # Cleanliness Weight
        if (float(loc.exts[0]) <= 0.3):
            cleanWT = 1.2
        elif (float(loc.exts[0]) <= 0.6):
            cleanWT = 1.1

        # Service Weight
        if (float(loc.exts[0]) <= 0.3):
            serveWT = 1.2
        elif (float(loc.exts[0]) <= 0.6):
            serveWT = 1.1

        total = aPoints * safeWT * cleanWT * serveWT
        scoreList.append(total)
        
    return scoreList


def outputRecc(locationlist, scoreList) -> list:
    locNameList = []
    for y in range(len(locationlist)):
        locNameList.append(locationlist[y])
    
    reccList = list(zip(locNameList, scoreList))
    reccList.sort(key= lambda a: a[1])

    print("End Output: ", reccList)
    return reccList


def get_recommendations(attr1, attr2, attr3):
    locations = load_locations_from_csv("locations.csv")
    user = Person("User", [attr1, attr2, attr3])
    scoreList = findRecc(user, locations)
    return outputRecc(locations, scoreList)


