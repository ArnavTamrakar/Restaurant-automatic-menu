def calculate_column_averages(data):
    # Transpose the data to make columns become rows
    transposed_data = list(zip(*data))
    
    # Calculating the average
    column_averages = []
    for column in transposed_data:
        average = sum(column) / len(column)
        column_averages.append(average)
    
    return column_averages


