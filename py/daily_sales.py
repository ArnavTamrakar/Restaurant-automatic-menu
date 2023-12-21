import csv

# Define the data as a list of lists
data = [
    ["", "Chicken Parmigiana", "Fish and Chips", "Margherita Pizza", "Caesar Salad", "Garlic Bread", "Tiramisu", "Cheesecake"],
    ["Monday", 100, 200, 150, 150, 270, 200, 200],
    ["Tuesday", 250, 300, 160, 220, 160, 220, 270],
    ["Wednesday", 180, 120, 220, 150, 100, 130, 200],
    ["Thursday", 280, 320, 210, 270, 200,180, 120],
    ["Friday", 150, 270, 200, 180, 120, 220, 150],
    ["Saturday", 300, 350, 150, 270, 200, 200, 150],
    ["Sunday", 180, 160, 220, 160, 220, 270, 230]
]

# Specify the filename
filename = "daily_sales.csv"

# Write the data to a CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

