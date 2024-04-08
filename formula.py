from reads import Person, Location

tmp_user = Person("Person1", [0.30, 0.15, 0.40])
tmp_locationList = []

locNameList = []
scoreList = []

# End List of Locations example
# [name, ext1, ext2, ext3, ext4, ext5, attr1, attr2, attr3]

def setData():

    tmp_locationList.append(Location("Location1", [0,0,0,0,0,0.20, 0.20, 0.65]))
    tmp_locationList.append(Location("Location2", [0,0,0,0,0,0.50, 0.70, 0.80]))
    tmp_locationList.append(Location("Location3", [0,0,0,0,0,0.45, 0.60, 0.90]))
    tmp_locationList.append(Location("Location4", [0,0,0,0,0,0.25, 0.45, 0.20]))
    tmp_locationList.append(Location("Location5", [0,0,0,0,0,0.75, 0.30, 0.45]))

# Using given user and list of locations calculate score for each location
def findRecc():
    
    tmpDiff = 0

    for loc in tmp_locationList:
        for x in range(0,3):
            tmpDiff += round(abs(tmp_user.preferences[x]- loc.attributes[x + 5]),2)
        scoreList.append(tmpDiff)
        tmpDiff = 0

def outputRecc():
    for y in range(len(tmp_locationList)):
        locNameList.append(tmp_locationList[y].name)
    reccList = list(zip(locNameList, scoreList))
    reccList.sort(key= lambda a: a[1])

    print("End: ", reccList)

def main():
    setData()
    findRecc()
    outputRecc()

main()