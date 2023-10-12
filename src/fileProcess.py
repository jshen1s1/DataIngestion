import pandas as pd
import glob

csv_files = glob.glob('*.{}'.format('csv'))

combined_data = pd.DataFrame()

# Loop through the file paths and read data into the DataFrame
for file_path in csv_files:
    data = pd.read_csv(file_path)
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# Remove duplicates based on all columns
combined_data = combined_data.drop_duplicates()

# Save the combined and de-duplicated data to a new CSV file
combined_data.to_csv("full_spotify_playlist.csv", index=False)