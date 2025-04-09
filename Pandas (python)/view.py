import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# # Create a view of the DataFrame by slicing
view = df[:2]


# # Modify the view
# view['A'] = [10, 20]

df.loc[:1, 'A'] = [10, 20]

# Changes reflect in the original DataFrame
print(df)
print(view._is_view)  # True if view, False if not

