#  File: MagicSquares.py
#  Description: HW13: Magic Squares
#  Student's Name: Mengyuan Dong
#  Student's UT EID: md42252
#  Identifier: BadyElephant
#  Course Name: CS 303E 
#  Unique Number: 51205
#
#  Date Created: 11/15
#  Date Last Modified: 11/16



class MagicSquare():

    def __init__(self,sideLength,grid):
        self.sideLength = sideLength
        self.grid = grid

        for row in range(sideLength):
            r = []
            for col in range(sideLength):
                r.append(0)
            self.grid.append(r)
            
        i = 1
        row = 0
        col = sideLength // 2
        
        for i in range(1,sideLength**2+1):

            self.grid[row][col] = i
            
            if i % sideLength == 0:     
                row = row + 1

                if row == sideLength:
                    row = 0

            if i % sideLength != 0:
                row = row - 1
                if row == -1:
                    row = sideLength - 1

                col = col + 1
                if col == sideLength:
                    col = 0
                    
            i += 1
            

    def display(self):
        
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])): 
                print(format(self.grid[row][col],"5d"),end="")
            print(" ")
        
 
def main():

    for n in range(1,15,2):
        
        print("Magic Square of size",n)
        print(" ")

        magicS = MagicSquare(n,[])
        magicS.display()
        print(" ")

main()


        
    
        
    
