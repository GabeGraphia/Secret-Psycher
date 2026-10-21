import hashlib
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

#def generatePsycherList(Users):
    #ES
