# 100 prisoners
# Each with a number from 1-100
# Each prisoners can pick 50 boxes numbered from 1-100.
# If they find their number inside a box, they succeed
# If all succeeds, they are all freed. If not, they are all executed. 
# What is the optimal strategy?

import random
import matplotlib.pyplot as plt 

class Box:
    number = 0
    def __init__(self, number):
        self.number = number

def getListOfPrisoners(N):
    return [n for n in range(1,N+1)]

def getListOfBoxes(N):
    boxes = []
    availableNumbers = [n for n in range(1,N+1)]
    random.shuffle(availableNumbers)
    for i in range(N):        
        boxes.append(
            Box(
                number = availableNumbers[i]
            )
        )
    return boxes

def getRandomBoxSelection(N,M):
    listOfOptions = [n for n in range(0,N)]
    random.shuffle(listOfOptions)
    return listOfOptions[0:M]

def randomStrategy(prisoners, boxes, N, M):
    successPrisoners = []
    for prisoner in prisoners:
        boxSelection = getRandomBoxSelection(N,M)
        for i,_ in enumerate(boxSelection):
            currBoxId = boxSelection[i]
            if boxes[currBoxId].number == prisoner:
                successPrisoners.append(prisoner)
                break
    return successPrisoners

def runRandomStrategy(N,M, runs=1000):
    avg = 0
    trueSuccess = 0
    nPrisonersSuccess = []
    for _ in range(0,runs):
        prisoners = getListOfPrisoners(N)
        boxes = getListOfBoxes(N)
        randomSuccess = randomStrategy(prisoners, boxes, N, M)
        avg += len(randomSuccess)/N
        if len(randomSuccess)==N:
            trueSuccess += 1
        nPrisonersSuccess.append(len(randomSuccess))
    randResult = int(avg/runs*100)
    print("Successfactor using random: %d%%"%randResult)
    print("After %d runs, %d runs was truely successful."%(runs,trueSuccess))
    return nPrisonersSuccess


def circleStrategy(prisoners, boxes, N, M):
    successPrisoners = []
    for prisoner in prisoners:
        for i in range(1,M+1):
            if i == 1:
                currBox = boxes[prisoner-1]
            else:
                currBox = boxes[currBox.number-1]
           
            if currBox.number == prisoner:
                successPrisoners.append(prisoner)
                break
    return successPrisoners

def runCircleStrategy(N, M, runs=1000):
    avg = 0
    trueSuccess = 0
    nPrisonersSuccess = []
    for _ in range(0,runs):
        circleSuccess = []
        prisoners = getListOfPrisoners(N)
        boxes = getListOfBoxes(N)

        circleSuccess = circleStrategy(prisoners, boxes, N, M)
        avg += len(circleSuccess)/N
        if len(circleSuccess)==N:
            trueSuccess += 1
        nPrisonersSuccess.append(len(circleSuccess))
    randResult = int(avg/runs*100)
    print("Successfactor using circle: %d%%"%randResult)
    print("After %d runs, %d runs was truely successful."%(runs,trueSuccess))
    return nPrisonersSuccess

def makeHistogram(lst):
    x = range(max(lst)+1)
    y = [0 for _ in x]
    for item in lst:
        y[item] += 1
    return x,y

N = 100
M = 50
runs = 1000

nPrisonersSuccessRandom = runRandomStrategy(N,M, runs)
xRand, yRand = makeHistogram(nPrisonersSuccessRandom)
nPrisonersSuccessCircle = runCircleStrategy(N,M, runs)
xCirc, yCirc = makeHistogram(nPrisonersSuccessCircle)

fig,axs = plt.subplots(2)

axs[0].bar(xRand, yRand)
axs[0].grid(True)

axs[1].bar(xCirc, yCirc)
axs[1].grid(True)

plt.show()