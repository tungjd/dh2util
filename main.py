import random, math
min = 0
max = 9
dd = (random.randint(min, max))
reroll = "yes"

characterName = ''
statNames = []
statNums  = []

def roll100():
#    while reroll == "yes" or reroll == "y":
    print ("Dank rolls:")
    tens = random.randint(min, max)
    ones = random.randint(min, max)
    total = tens*10+ones
    print ("{:0<2}".format(tens))
    print (ones)
    print (total)
    return total
    #reroll = input("ReDankRoll?")


def readDH2File(path):
    f = open(path, 'r')
    global characterName
    global statNums
    global statNames

    characterName = f.readline()
    for line in f:
        tuple = line.split(':')
        statNames.append(tuple[0])
        statNums.append(tuple[1])

def getDegreesSuccess(statIndex):
    # WSK:0
    # BSK:1
    # STR:2
    # AGI:3
    # TGH:4
    # INT:5
    # PER:6
    # WIL:7
    # FEL:8
    # IFL:9
    # roll 5 on STR 20 = -15 = 1 degree of success
    result = roll100()
    degrees = (result - int(statNums[statIndex]))/10
    degrees = math.ceil(degrees) if degrees < 0 else math.floor(degrees)
    # [on_true] if [expression] else [on_false]
    print ('Rolled a ', result, '. My stat: ', statNames[statIndex], ':', statNums[statIndex])
    print ('Roll against ', statNames[statIndex], ' succeeded ' if degrees < 0 else ' failed ', 'with ', math.fabs(degrees), ' degrees')

readDH2File('samplechar.dh2')
print(characterName)
print(statNames[0], ':', statNums[0])

while(1):
    statIndex = input('What stat (idx) would you like to roll for?')
    statIndex = int(statIndex)
    if (statIndex >= 0) and (statIndex < 10):
        getDegreesSuccess(statIndex)
    else:
        break
#sample roll against BSK
