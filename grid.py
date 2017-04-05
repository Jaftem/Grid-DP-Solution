# Feature Complete & Unit Tested Grid Problem
# Solution by Jeremy Aftem (aftem@usc.edu)
# 3/24/2017
# See README.txt for more information

import sys    # For user input
import re     # Regex for parsing input

class Grid(object):
    def __init__(self):
        # Get user's input
        self.GetUserInput() # Calls SetupGrids

        # Compute the path counts for all nodes
        self.ComputePathCounts(self.mGridSize[0], self.mGridSize[1])

        # Account for jumping nodes and adjust affected nodes' path counts
        self.InsertJumpingPts()

        # Output
        self.PrintAnswer()

    def GetUserInput(self):
        # Too many cmd line arguments gets confusing! Let's just ask for input
        gridSize   = input("Grid size (eg. 5 5) : ")
        blockedPts = input("Blocked points      : ")
        jumpingPts = input("Jumping points      : ")

        # Parse size of the grid (width x height)
        gridSize = re.sub('[(),]', ' ', gridSize)
        gridSize = [int(n) for n in gridSize.split()]
        dimensions = (gridSize[0], gridSize[1]) # Width x Height

        # Parse blocked points
        blockedPts = re.sub('[(),]', ' ', blockedPts)         # Remove parenthesis
        blockedPtsList = [int(n) for n in blockedPts.split()] # Get all pts
        blockedPtsList = list(zip(blockedPtsList[0::2], blockedPtsList[1::2]))

        # Parse jumping points
        jumpingPts = re.sub('[(),]', ' ', jumpingPts)         # Remove parenthesis
        jumpingPtsTemp = [int(n) for n in jumpingPts.split()] # Get all pts
        jumpingPtsList = list(zip(jumpingPtsTemp[0::2], jumpingPtsTemp[1::2])) # Zip into pairs
        jumpingPtsList = list(zip(jumpingPtsList[0::2], jumpingPtsList[1::2])) # Zip into pairs of pairs

        # Setup Grids for computation
        self.SetupGrids(dimensions, blockedPtsList, jumpingPtsList)

    def SetupGrids(self, gridSize, blockedPtsList, jumpingPtsList):
        self.mGridSize = gridSize
        self.mBlockedList = blockedPtsList
        self.mJumpingPtsList = jumpingPtsList

        # Create Grid
        w, h = gridSize[0], gridSize[1]
        # Grid that displays open/blocked elements
        self.mGrid = [[0 for x in range(w)] for y in range(h)]
        # Grid that tracks number of paths from state to goal state at w-1, h-1 
        self.mPathCounts = [['O' for x in range(w)] for y in range(h)]

        # Add 'blocks' to grid
        for j,k in self.mBlockedList:
            self.mGrid[j][k] = 'X'

        # Add initial path counts
        for i in reversed(range(h-1)):
            if self.mGrid[i][w-1] != 'X':
                self.mPathCounts[i][w-1] = 1
        for j in reversed(range(w-1)):
            if self.mGrid[h-1][j] != 'X':
                self.mPathCounts[h-1][j] = 1
        # w-1, h-1
        self.mPathCounts[h-1][w-1] = 0

    def InsertJumpingPts(self):
        # If no jumping nodes, abort
        if not self.mJumpingPtsList:
            return
        # Set the jumping pt value to landing pt value 
        for i, k in self.mJumpingPtsList:
            self.mPathCounts[i[0]][i[1]] = self.mPathCounts[k[0]][k[1]]

        # Compute the new values for all nodes up and to the left of jumping pt
        for n in reversed(range(i[0]+1)):
            for m in reversed(range(i[1]+1)):
                if (n != i[0] or m != i[1]):
                    self.ComputePath(n, m)

    def ComputePathCounts(self, w, h):
        # Start at h-2, w-2 and iterate
        for i in reversed(range(h-1)):
            for k in reversed(range(w-1)):
                self.ComputePath(i, k)

    def ComputePath(self, i, k):
        # Check if blocked
        if self.mGrid[i][k] == 'X':
            self.mPathCounts[i][k] = 0
        # Check within bounds
        elif i + 1 < self.mGridSize[1] and k + 1 < self.mGridSize[0]:
            # Get size from nodes below and to the right
            self.mPathCounts[i][k] = self.mPathCounts[i+1][k] + self.mPathCounts[i][k+1] 

    def PrintAnswer(self):
        answer = self.mPathCounts[0][0]
        print("\nOut: " + str(answer))  
        
if __name__ == "__main__":
    grid = Grid()   
