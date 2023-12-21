import csv

# Define the menu items (fields) and their corresponding ratings (rows)
fields = ['Chicken Parmigiana', 'Fish and Chips', 'Margherita Pizza', 'Caesar Salad','Garlic Bread','Tiramisu','Cheesecake' ]
rows = [
    [3.11, 4.57, 4.64, 2.07, 4.62, 4.16, 3.28],
    [2.31, 3.95, 2.33, 4.55, 4.54, 3.44, 4.9],
    [4.27, 2.47, 3.47, 5.0, 2.57, 3.76, 2.89],
    [4.16, 2.12, 2.19, 3.8, 4.83, 2.54, 4.63],
    [4.15, 2.61, 3.32, 2.89, 3.32, 2.85, 3.65],
    [3.4, 2.16, 4.89, 2.19, 3.4, 2.46, 3.77],
    [3.75, 4.36, 3.98, 4.62, 3.83, 2.66, 4.6]]


# Calculate and print the average rating for each menu item
for i, row in enumerate(rows, 1):
    average = sum(row) / len(row)
    print(f"Average for Row {i}: {average:.2f}")


# Write the menu items and their average ratings to a CSV file
with open('average_ratings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row (menu item names)
    writer.writerow(fields)
    
    # Write the corresponding average ratings for each item
    writer.writerows(rows)

    


