import hashlib
import random
womensTeam = []
mensTeam = []

def participantsToList(teamName):
    with open("participants.txt", "r", encoding="utf-8") as file:
        section = False
        if "".join(teamName.split()).lower() == "womensteam":
            for line in file:
                if "}" in line:
                    return womensTeam
                if section:
                    womensTeam.append(("".join(line.split())).split(","))
                if "Womens team" in line:
                    section = True
            return None
        if "".join(teamName.split()).lower() == "mensteam":
            for line in file:
                
                if "}" in line:
                    return mensTeam
                if section:
                    mensTeam.append(("".join(line.split())).split(","))
                if "Mens team" in line:
                    section = True
            return None
        return None              

def generatePsycherOrder(UsersList):
    orderList = []
    for i in range(len(UsersList)):
        index = random.randint(0, len(UsersList) - 1)
        while index in orderList:
            index = random.randint(0, len(UsersList) - 1)
        orderList.append(index)
    return orderList

def hasUser(hashedPsycherList, userId):
    for user in hashedPsycherList:
        if user[0] == userId:
            return hashlib.sha256(user[3].encode()).hexdigest()
    return None

def userHas(hashedPsycherList, userId):
    for user in hashedPsycherList:
        if user[0] == userId:
            return hashlib.sha256(user[4].encode()).hexdigest()
    return None
    
def getUserName(hashedPsycherList, userId):
    for user in hashedPsycherList:
        if user[0] == userId:
            return user[1]
    return None

def generatePartialPsycherList(UsersList, orderList):
    partialPsycherList = []
    for index in orderList:
        fullUser = UsersList[index]
        partialPsycherList.append(fullUser)
    return partialPsycherList

def generatePsycherList(partialPsycherList):
    psycherList = []
    for i in range(len(partialPsycherList)):
        fullUser = partialPsycherList[i]
        if i == 0:
            fullUser.append(partialPsycherList[-1][0])
            fullUser.append(partialPsycherList[i + 1][0])
        elif i == len(partialPsycherList) - 1:
            fullUser.append(partialPsycherList[i - 1][0])
            fullUser.append(partialPsycherList[0][0])
        else:
            fullUser.append(partialPsycherList[i - 1][0])
            fullUser.append(partialPsycherList[i + 1][0])
        psycherList.append(fullUser)
    return psycherList

def hashPsycherList(psycherList):
    hashedPsycherList = []
    for user in psycherList:
        hashedUser = []
        hashedUser.append((hashlib.sha256((hashlib.sha256(user[0].encode()).hexdigest()).encode())).hexdigest())
        hashedUser.append(user[1])
        hashedUser.append(hashlib.sha256(user[2].encode()).hexdigest())
        hashedUser.append(hashlib.sha256(user[3].encode()).hexdigest())
        hashedUser.append(hashlib.sha256(user[4].encode()).hexdigest())
        hashedPsycherList.append(hashedUser)
    return hashedPsycherList

def removeUser(hashedPsycherList, userEmail):
    userId = hashlib.sha256((hashlib.sha256(userEmail.encode()).hexdigest()).encode()).hexdigest()
    for user in hashedPsycherList:
        if user[0] == userId:
            previousUser = hashlib.sha256(user[3].encode()).hexdigest()
            nextUser = hashlib.sha256(user[4].encode()).hexdigest()
            newHashedPsycherList = hashedPsycherList.copy()
            for user2 in newHashedPsycherList:
                if user2[0] == previousUser:
                    user2[4] = user[4]
                if user2[0] == nextUser:
                    user2[3] = user[3]
            newHashedPsycherList.remove(user)
            return newHashedPsycherList
    return False

def addUser(hashedPsycherList, userEmail, userName, userPassword):
    pass

def saveList(listname, hashedPsycherList):
    with open("psycherList.txt", "a", encoding="utf-8") as file:
        file.write(f"{listname}: {{")
        for user in hashedPsycherList:
            file.write(f"({user[0]},{user[1]},{user[2]},{user[3]},{user[4]}), ")
        file.write("}\n")
        
wTeam = participantsToList("Womens team")
print(wTeam)
order = generatePsycherOrder(wTeam)
print(order)
partialPsycherList = generatePartialPsycherList(wTeam, order)
print(partialPsycherList)
psycherList = generatePsycherList(partialPsycherList)
print(psycherList)
hashedPsycherList = hashPsycherList(psycherList)
print(hashedPsycherList)
saveList("test team", hashedPsycherList)

#listname1 {(doublyHashedUsername1, name1, hashedPassword1, hashedPreviousUsername1, hashedNextUsername1), (doublyHashedUsername2, name2, hashedPassword2, hashedPreviousUsername2, hashedNextUsername2)}