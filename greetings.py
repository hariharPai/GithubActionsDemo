import datetime

# Define the file name
file_name = "greeting.txt"

# Get the current date and time
current_time = datetime.datetime.now()

# Define the greeting message
greeting_message = "Hello! Hope you have a wonderful day!"

# Write to the file
with open(file_name, 'w') as file:
    file.write(f"Current Date and Time: {current_time}\n")
    file.write(greeting_message)

print(f"Data has been written to {file_name}")
