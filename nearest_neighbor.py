import math
import operator
import os
import random
import sys
import time

def distance(dot1, dot2):
    """Calculates the distance between two points in R^2.
    
    Keyword arguments:
    dot1 -- A point, an ordered pair e.g. [x,y].
    dot2 -- See dot1.
    """
    return math.sqrt(math.pow(dot1[0]-dot2[0], 2) + math.pow(dot1[1]-dot2[1],2))



def giveMePoints(filename):
    """Reads and returns a list of points in R^2 as 2-tuples.
    
    Keyword arguments:
    filename -- Name of the txt file being read.
                File should contain lines of the form "3.243 56.213".
    """
    try:
        file = open(filename, 'r')
    except IOError:
        raise IOError("Could not read or find %r." % filename)
    
    dots = []

    for line in file:
        dot = line.split()
        if len(dot) != 2: 
            raise ValueError("A bad input was found in %r" % filename)
        dots.append((float(dot[0]), float(dot[1])))

    file.close()

    if len(dots) < 2:
        raise ValueError("Less than two points were given.")
    
    return sorted(dots)



def bruteForceNeighbor(points):
    """Finds the smallest distance possible between two dots via brute force.

    Keyword arguments:
    points -- A list of points in R^2 as 2-tuples.
    """
    
    minDist = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            if minDist == 0:
                minDist = distance(points[i], points[j])            
            minDist = min(distance(points[i], points[j]), minDist)
            
    
    return minDist



def dividedNeighbor(points):
    """Finds smallest distance possible between two dots via divide-and-conquer.

    Keyword arguments:
    points -- A list of points in R^2 as 2-tuples.
    """
    #Returns the smallest distance for 2 or 3-point sets.
    if len(points) == 2 or len(points) == 3:
        return bruteForceNeighbor(points)

    #Splits the list into two similarly sized parts.
    midline = int(len(points)/2+0.5)
    pointsL, pointsR = [], []
    for dot in points:
        midline -= 1
        if midline >= 0:
            pointsL.append(dot)
        else:
            pointsR.append(dot)
    
    #Marks dots to be removed and then remove then with another loop.
    minDist = min(dividedNeighbor(pointsL), dividedNeighbor(pointsR))
    toBeRemoved = []
    for dot in points:
        if math.fabs(dot[0]-points[midline][0]) > minDist:
            toBeRemoved.append(dot)
    for dot in toBeRemoved: points.remove(dot)
    
    #Return if there's not enough points in the middle section.
    if len(points) < 2: return minDist
    
    #Sort points by y-coordinate, and compare them sequentially.
    points.sort(key=lambda x: x[1])
    for i in range(0, len(points)-1):
        minDist = min(minDist, distance(points[i], points[i+1]))

    return minDist



def writeDistance(dist, argv):
    """Writes a distance into [argv-".txt"]_distance.txt

    Keyword arguments:
    dist -- A number to be written into text file.
    argv -- Prefix string of the text file.
    """
    file = open(os.path.splitext(argv)[0]+"_distance.txt", "w")
    file.write(str(dist))
    file.close()



def createInputs():
    """Creates a text file of 111 random points named "111.txt"
    """
    file = open("111.txt","w")
    random.seed(time.time())
    for i in range(0,111):
        file.write(str(100*random.random())+" "+str(100*random.random())+"\n")
    file.close()



def test(argv = "111.txt"):
    """Runs 100 trials with randomly created sets of 111 dots in R^2.

    Keyword arguments:
    argv -- File name to be used in tests. 
            Default set as a randomly generated file.
    """
    successCount = 0
    for x in range(0,100):
        if argv == "111.txt": createInputs()
        points = giveMePoints(argv)
        minDist = dividedNeighbor(points)
        print(minDist)

        points = giveMePoints(argv)
        minDist1 = bruteForceNeighbor(points)
        print(minDist1)
        if minDist == minDist1:
            print("It's a match!")
            successCount += 1
        else:
            print("Falied")
        print("\n")
    print("Successful trials: %r/100\n" % successCount)
    if argv == "111.txt": os.remove("111.txt")



def main(argv):
    #test()
    #if os.path.isfile("count.txt"): os.remove("count.txt")
    points = giveMePoints(argv)
    minDist = dividedNeighbor(points)
    #minDist = bruteForceNeighbor(points)
    #print("Minimum distance:", minDist)
    writeDistance(minDist, argv)



if __name__ == "__main__":
   main(sys.argv[1])