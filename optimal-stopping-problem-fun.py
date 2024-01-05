import random
import time
import numpy as np


def main():
    #print("default testing")
    #for i in range(99):
    #    print("stop:", i+1, "finalinfo", default_test(100,100,i+1))

    #print("This is the default criteria for the Optimal Stopping Problem, we show the top 5 tests and average them as well, just because sometimes it's not exact.")
    #tests=10000
    #analysis=[]
    #for i in range(99):
    #    result=originaltest(100,100,i+1,tests)
    #    print("stop:", i+1, f"average of {tests} tests", result)
    #    analysis.append([i+1,result])

    #print("The top 5 stop points in order are:")
    #print(sorted(analysis,key=lambda x: x[1],reverse=True)[:5])

    #print("The average of these top 5 stop points is:")
    #print(np.mean([x[0] for x in sorted(analysis,key=lambda x: x[1],reverse=True)[:5]]))

    print("Trying to obtain the highest score on average with just stopping and leaping")
    tests=10000
    analysis=[]
    for i in range(99):
        result=avgxtests(100,100,i+1,tests,False)
        print("stop:", i+1, f"average of {tests} tests", result)
        analysis.append([i+1,result])

    print("The top 5 stop points in order are:")
    print(sorted(analysis,key=lambda x: x[1],reverse=True)[:5])

    print("The average of these top 5 stop points is:")
    print(np.mean([x[0] for x in sorted(analysis,key=lambda x: x[1],reverse=True)[:5]]))

    #print("norm tests")
    #tests=1000
    #analysis=[]
    #for i in range(99):
    #    result=normtests(100,100,i+1,tests)
    #    print("stop:", i+1, f"average of {tests} tests", result)
    #    analysis.append(result)

    #print("The best stop point is:", analysis.index(max(analysis))+1)

def default_test(options,max_value,stop,infpool=True):
    # options: number of options
    # max_value: maximum value of an option
    # stop: stop point for observing before leaping
    # returns: the optimal value
    if infpool==True:
        collecting = []
        for i in range(stop):
            collecting.append(random.randint(0,max_value))
        best=max(collecting)
        for i in range(options-stop):
            newOption=random.randint(i,max_value)
            if newOption>best:
                return i,newOption
        return i,newOption
    else:
        assert max_value>=options
        randomlist=[range(max_value)]
        random.shuffle(randomlist)
        collecting = []
        for i in range(stop):
            collecting.append(randomlist.pop(0))
        best=max(collecting)
        for i in range(options-stop):
            newOption=randomlist.pop(0)
            if newOption>best:
                return i,newOption
        return i,newOption

def originaltest(options,max_value,stop,tests,tmp=True):
    assert max_value>=options
    maxcount=0
    for i in range(tests):
        randomlist=[*range(max_value)]
        random.shuffle(randomlist)
        collecting = []
        for i in range(stop):
            collecting.append(randomlist.pop(0))
        best=max(collecting)
        for i in range(options-stop):
            newOption=randomlist.pop(0)
            if newOption>best:
                if newOption == max_value-1:
                    maxcount+=1
                break
    return maxcount/tests

def avgxtests(options,max_value,stop,tests,infpool=True):
    # options: number of options
    # max_value: maximum value of an option
    # stop: stop point for observing before leaping
    # returns: the optimal value
    if infpool==True:
        allTestScores=[]

        for i in range(tests):
            collecting = []
            for i in range(stop):
                collecting.append(random.randint(0,max_value))
            best=max(collecting)
            for i in range(options-stop):
                newOption=random.randint(i,max_value)
                if newOption>best:
                    allTestScores.append(newOption)
            allTestScores.append(newOption)
        return sum(allTestScores)/len(allTestScores)
    else:
        assert max_value>=options
        allTestScores=[]
        for i in range(tests):
            randomlist=[*range(max_value)]
            random.shuffle(randomlist)
            collecting = []
            for i in range(stop):
                collecting.append(randomlist.pop(0))
            best=max(collecting)
            for i in range(options-stop):
                newOption=randomlist.pop(0)
                if newOption>best:
                    allTestScores.append(newOption)
            allTestScores.append(newOption)
        return sum(allTestScores)/len(allTestScores)

def normtests(options,max_value,stop,tests,infpool=True):
    # options: number of options
    # max_value: maximum value of an option
    # stop: stop point for observing before leaping
    # returns: the optimal value
    allTestScores=[]
    for i in range(tests):
        genvals=np.random.normal(loc=0, scale=0.2, size=max(max_value,options))
        randomlist=[]
        for i in range(max(options,max_value)):
            randomlist.append(estNumber(float(genvals[i]),max_value))
        collecting = []
        for i in range(stop):
            collecting.append(randomlist.pop(0))
        best=max(collecting)
        for i in range(options-stop):
            newOption=randomlist.pop(0)
            if newOption>best:
                allTestScores.append(newOption)
        allTestScores.append(newOption)
    return sum(allTestScores)/len(allTestScores)

def estNumber(numberin,multiplier):
    # takes in a long decimal, multiplies it by 100, and rounds it to the nearest integer
    # returns: the rounded integer
    numberin=float(numberin)
    return int(round(numberin*multiplier))

if __name__ == "__main__":
    main()
