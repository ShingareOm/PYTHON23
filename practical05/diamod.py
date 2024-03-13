# Number of rows
row = 5

# Upper part of hollow diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):  
            print("*", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
            print("*", end="")
    print()

"""

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
                                                       


"""
