import zipfile
import os

# Path to the zip file containing the database files
zip_file_path = 'your_folder/database.zip'

# Directory to extract the files
extracted_folder = 'extracted_data'

# Extract the files from the zip archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

# List the extracted files
extracted_files = os.listdir(extracted_folder)
print("Extracted files:", extracted_files)

# Load the contents of each text file
data = []
for file_name in extracted_files:
    file_path = os.path.join(extracted_folder, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        # Process the contents as needed
        data.append(contents)

# Display the contents of the loaded files
for idx, content in enumerate(data):
    print(f"Contents of file {idx + 1}:")
    print(content)

# Further processing of the data...
