import pandas as pd
import numpy as np
import glob

# Load all CSV files
files = glob.glob('*.csv')
storyid_sets = []

# Extract storyid from each CSV file
for file in files:
    df = pd.read_csv(file)
    storyid_sets.append(set(df['storyid']))

# Create an overlap matrix
n = len(files)
overlap_matrix = np.zeros((n, n), dtype=int)

# Calculate overlaps
for i in range(n):
    for j in range(n):
        overlap_matrix[i, j] = len(storyid_sets[i].intersection(storyid_sets[j]))

# Convert to DataFrame for better readability
overlap_df = pd.DataFrame(overlap_matrix, index=files, columns=files)

# Display the overlap matrix
print(overlap_df)