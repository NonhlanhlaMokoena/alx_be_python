# Drawing patterns with Nested Loops. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

#Step 1: Prompt user for pattern size
pattern_size = int(input("Enter the size of the pattern: "))

#Step 2: Draw the Pattern
row = 0
while row < pattern_size:
    for i in range(pattern_size):
        print("*", end="")
    
    print()  
    row += 1
    