import pandas as pd

# Read the input values
input_values = """
   Time 


Oxygen

"""

# Split the input values into a list of strings
values_list = input_values.strip().split()

# Initialize a variable to store the current header
current_header = None

# Sample data
data = {
    'Time': [],
    'Oxygen': []
}

# Loop through the values
for value in values_list:
    # Check if the value is a header
    if value.strip().isalpha():
        current_header = value.strip()
    else:
        # If not a header, append the value to the corresponding list in the data dictionary
        data[current_header].append(float(value.strip()))

# Convert data to DataFrame
df = pd.DataFrame(data)

# Calculate time differences
df['Time_diff'] = df['Time'].diff()

# Define threshold for time continuity
time_threshold = 5
# Identify group breaks
df['Group'] = (df['Time_diff'] > time_threshold).cumsum()

# Group data by 'Group'
grouped_data = df.groupby('Group')

# Calculate the average oxygen value for each group
group_averages = grouped_data['Oxygen'].mean()

# Save group averages to a CSV file
group_averages.to_csv('o2_group_averages.csv', header=['Average Oxygen'], index_label='Group')
print("Group average oxygen values saved to o2_group_averages.csv")
