def calculate_total_sales(data):
    # Initialize a dictionary to store total sales for each day
    total_sales = {}

    # Iterate through the rows starting from the second row (skipping the header)
    for row in data[1:]:
        day = row[0]
        sales = row[1:]  # Extract sales values for the day

        # Calculate the total sales for the day, skipping non-numeric values
        total = sum(int(value) for value in sales if value.isdigit())

        # Store the total sales for the day in the dictionary
        total_sales[day] = total

    return total_sales


# # # Example usage:
# # data = [
# #     ['', 'Chicken Parmigiana', 'Fish and Chips', 'Margherita Pizza', 'Caesar Salad', 'Garlic Bread', 'Tiramisu', 'Cheesecake'],
# #     ['Monday', '1', '3', '4', '5', '6', '7', '6'],
# #     ['Tuesday', '8', '6', '4', '4', '5', '6', '5'],
# #     ['Wednesday', '6', '8', '7', '4', '4', '6', '7'],
# #     ['Thursday', '0', '5', '6', '7', '8', '5', '6'],
# #     ['Friday', '4', '5', '6', '3', '5', '5', '7'],
# #     ['Sunday', '5', '8', '1', '4', '7', '1', '5']
# # ]

# # daily_sales = calculate_daily_sales(data)

# # Print the daily sales
# for day, item_sales in daily_sales.items():
#     print(f"{day}: {item_sales}")
