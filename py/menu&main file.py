# Import the required module
import csv
import average_ratings_calculator
import daily_sales_calculator

# Define the field names
fields = ['item', 'price', 'category']

# Define the data rows
rows = [
    ['Chicken Parmigiana', 19.99, 'Main'],
    ['Fish and Chips', 18.99, 'Main'],
    ['Margherita Pizza', 15.99, 'Main'],
    ['Caesar Salad', 9.99, 'Starter'],
    ['Garlic Bread', 6.99, 'Starter'],
    ['Tiramisu', 7.99, 'Dessert'],
    ['Cheesecake', 6.99, 'Dessert'],
]

# Create a CSV file and write the data rows
with open('menu.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(rows)



# -------------------------------CALCULATING AVERAGE RATINGS OF EACH ITEMS FROM A LIST OF ASSUMED CUSTOMER RATINGS-----------------------------

#Opening csv file with average menu item rating
with open('average_ratings.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    # Initialize a list to store the data rows
    data = []
    for row in reader:
        data.append([float(value) for value in row])

#Add the values in column_average variable and printing
column_averages = average_ratings_calculator.calculate_column_averages(data)

# Printing item names and the ratings
print("\nThe ratings of all items are : ")

# For loop in order to grab all the items and their ratings seperately
for i in range(len(rows)):
    dish_name = rows[i][0]
    rating = column_averages[i]
    
    print(f"{dish_name} = {round(column_averages[i],1)}/5")



# -----------------------------------------------CALCULATING TOTAL DAILY SALES---------------------------------------------

#Opening csv file with daily sales of each item
with open('daily_sales.csv', 'r') as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)  # Convert the csv_reader to a list

# Calculate total sales
total_sales = daily_sales_calculator.calculate_total_sales(data)

# Print the total sales for each day
print("\n"
    
    "Total sales every day of the week are: "
    )


for day, sales in total_sales.items():
    print(f"{day}: {sales}")


# ----------------------------------- FINDING THE MOST POPULAR ITEM IN THE MENU---------------------------------------

max_rating = max(column_averages)

# Find the item with the highest rating
most_popular_item = rows[column_averages.index(max_rating)]

# Print the most popular item
print(f"The most popular item in the menu is {most_popular_item} with a rating of {max_rating}/5.")








