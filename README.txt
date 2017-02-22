README file for "nearest_neighbor.py".

The main program of this script takes the first command line argument as the 
name to the input text file. 
(E.g. Entering "python nearest_neighbor.py input.txt" recursively finds the 
nearest distance between two points and outputs the distance to 
input_distance.txt)

Includes the following functions:
	-bruteForceNeighbor(points)
	-countComparison()
	-createInputs()
	-distance(dot1, dot2)
	-dividedNeighbor(points)
	-giveMePoints(filename)
	-test(argv = "111.txt")
	-writeDistance(dist, argv)
which one can find details by accessing their respective docstrings.

Created by Tung Lin Hsieh, Oct, 2016, for CS141 at UC Riverside.