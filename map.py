row1=["O","O","O"]
row2=["O","O","O"]
row3=["O","O","O"]
map=[row1,row2,row3]
position=(input("enter the position"))
map[int(position[0])-1][int(position[1])-1]="x"
print(row1)
print(row2)
print(row3)
