import csv
import os

# Prompt for CSV file name
filename = input("Enter the csv file name (example: data.csv): ")

# Check if file exists
if os.path.exists(filename):
    print("File existing")
else:
    print("File does not exist. Creating file")
    
    # Create file and write headers
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        #Writing headers
        writer.writerow(["name", "age", "gender"])
        
# Prompt user for information
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

# Append information to the CSV file
with open(filename, mode='a', newline= '') as file:
    writer = csv.writer(file)
    
    # Write user data
    writer.writerow([name, age, gender])
    
# Success message
print("Information successfully written to the CSV file")