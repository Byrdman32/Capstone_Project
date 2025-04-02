# This is a rough estimate of what our dataframe filtering module might look like.
# Should be used in: 
# Show similar planets functionality (user story 2)
# Direct filtering of planets (user story 4)

# What it should do:
# 1. Specific search of dataframe
# 2. Filter by specific parameters
# 3. Filter of dataframe based on range of values (this one is a bit more complex)

def filter_by_column(df, column_name, value):
    """
    Filters the DataFrame based on a specific column and value.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    column_name (str): The name of the column to filter by.
    value: The value to filter for in the specified column.
    
    Returns:
    pd.DataFrame: A filtered DataFrame.
    """
    return df[df[column_name] == value]

#This makes sense because we will call this function with a dictionary of column names and values makes it easy maintain col/val continuity
def filter_by_list_of_columns_and_values(df, filter_dict):
    """
    Filters the DataFrame based on a dictionary of column-value pairs.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    filter_dict (dict): A dictionary where keys are column names and values are the values to filter for.
    
    Returns:
    pd.DataFrame: A filtered DataFrame.
    """
    filtered_df = df
    for column_name, value in filter_dict.items():
        filtered_df = filtered_df[filtered_df[column_name] == value]
    return filtered_df



#def filter_by_range(df, column_name, min_value, max_value):