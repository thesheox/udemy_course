# from prettytable import PrettyTable
#
# # Specify the Column Names while initializing the Table
# myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])
#
# # Add rows
# myTable.add_row(["Leanord", "X", "B", "91.2 %"])
# myTable.add_row(["Penny", "X", "C", "63.5 %"])
# myTable.add_row(["Howard", "X", "A", "90.23 %"])
# myTable.add_row(["Bernadette", "X", "D", "92.7 %"])
# myTable.add_row(["Sheldon", "X", "A", "98.2 %"])
# myTable.add_row(["Raj", "X", "B", "88.1 %"])
# myTable.add_row(["Amy", "X", "B", "95.0 %"])
#
# print(myTable)




from prettytable import PrettyTable

columns = ["Student Name", "Class", "Section", "Percentage"]

myTable = PrettyTable()

# Add Columns
myTable.add_column(columns[0], ["Leanord", "Penny", "Howard",
					"Bernadette", "Sheldon", "Raj", "Amy"])
myTable.add_column(columns[1], ["X", "X", "X", "X", "X", "X", "X"])
myTable.add_column(columns[2], ["B", "C", "A", "D", "A", "B", "B"])
myTable.add_column(columns[3], ["91.2 %", "63.5 %", "90.23 %", "92.7 %",
										"98.2 %", "88.1 %", "95.0 %"])
myTable.align="r"
print(myTable)
