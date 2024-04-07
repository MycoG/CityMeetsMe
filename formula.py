from reads import Person, Location, load_locations_from_csv, load_user_from_csv

tmp_user : Person
tmp_locationList = []

locNameList = []
scoreList = []

# End List of Locations example
# [name, ext1, ext2, ext3, attr1, attr2, attr3]

def setData():
    
    global tmp_locationList
    tmp_locationList = load_locations_from_csv("locations.csv")
    global tmp_user
    tmp_user = load_user_from_csv("user.csv")

# Using given user and list of locations calculate score for each location
def findRecc():
    
    tmpDiff = 0

    for loc in tmp_locationList:
        for x in range(0,3):
            tmpDiff += abs(float(tmp_user.preferences[x]) - float(loc.attributes[x]))
        scoreList.append(round(tmpDiff,2))
        tmpDiff = 0

def outputRecc():
    for y in range(len(tmp_locationList)):
        locNameList.append(tmp_locationList[y])
    reccList = list(zip(locNameList, scoreList))
    reccList.sort(key= lambda a: a[1])

    print("End: ", reccList)
    return reccList

def main():
    
    setData()
    findRecc()
    return outputRecc()

main()
