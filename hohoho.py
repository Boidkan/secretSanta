import smtplib, ssl
import sys, json, random, copy

class SantaPair:
    def __init__(self, santa, givee):
        self._santa = santa
        self._givee = givee

class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

filePath = "secrets.json"
file = open(filePath)
secrets = json.load(file)

myEmail = secrets["email"]
password = secrets["password"]
port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

givers = secrets["emailList"]
givees = copy.deepcopy(givers)

santas = []

def getRandomGiveeIndex(groupIndex):
    randomIndex = groupIndex
    while randomIndex == groupIndex:
        randomIndex = random.randrange(len(givees))

    return randomIndex

def dropGiveeIndexFromGroup(randIndex):
    group = givees[randIndex]
    if len(group) == 1:
        givees.pop(randIndex)
    else:
        givees[randIndex].pop(0)

def getSantaFor(groupIndex, randIndex, giver):

    randGroup = givees[randIndex]
    randomPerson = randGroup[0]

    selectedGivee = Person(randomPerson["name"], randomPerson["email"])
    selectedGiver = Person(giver["name"], giver["email"])

    return SantaPair(selectedGiver, selectedGivee)

def addSanta(groupIndex, giver):
    randIndex = getRandomGiveeIndex(groupIndex)
    santa = getSantaFor(groupIndex, randIndex, giver)
    santas.append(santa)
    dropGiveeIndexFromGroup(randIndex)

def generateSantas():
    for groupIndex, group in enumerate(givers):
        for giver in group:
            addSanta(groupIndex, giver)

def resetDataStructs():
    santas = []
    givees = copy.deepcopy(givers)

def sendEmails():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(myEmail, password)
        for santa in santas:
            sendMailFor(santa, server)

def sendMailFor(santa, server):
    name = santa._santa._name
    santaEmail = santa._santa._email
    givee = santa._givee._name

    message = "Hi, %s you are the secret santa of %s! The gift is $25 max."%(name, givee)
    print(message)
    server.sendmail(myEmail, santaEmail, message)

def run():
    giversCount = sum(len(group) for group in givers)
    while len(santas) != giversCount:
        resetDataStructs()
        generateSantas()
    sendEmails()

run()
