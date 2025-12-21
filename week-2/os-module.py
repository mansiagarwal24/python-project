from datetime import datetime, timedelta
import os

# Q1 Using datetime, add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
#
# original date and time
original_dt = datetime(2020, 3, 22, 10, 0)

# Add 1 week + 12 hours
new_dt = original_dt + timedelta(weeks=1, hours=12)

print("Original Date Time:", original_dt)
print("New Date Time:", new_dt)

# Q2 Code to get the dates of yesterday, today, and tomorrow.
#

today = datetime.today().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# Q3 Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
cwd = os.getcwd()
print("Current working directory:", cwd)

folder_name = "test"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

print("\nFiles & directories in current path:")
print(os.listdir(cwd))

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"\nFolder '{folder_name}' removed.")

# Q4 Write a Python program to rename a file from old_name.txt to new_name.txt.
#
old_name = "old_name.txt"
new_name = "new_name.txt"
try:
    os.rename(old_name, new_name)
    print(f"File renamed successfully to {new_name}")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error: {e}")

# Q5 Create a file and Write a Python program to get the size of a file named example.txt

file_path = "file.txt"
size = os.path.getsize(file_path)

print(f"File size: {size} bytes")
# Q6 Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00

date_str = "Feb 25 2020 4:20PM"

dt = datetime.strptime(date_str, "%b %d %Y %I:%M%p")

print(dt)
#
# Q7 Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
date_str = "2025-02-25"
dt = datetime.strptime(date_str, "%Y-%m-%d")

new_date = dt - timedelta(days=7)
print("New date:", new_date.strftime("%Y-%m-%d"))


# Q8 Format the date 2020-02-25 as "Tuesday 25 February 2020"

date_str = "2020-02-25"

dt = datetime.strptime(date_str, "%Y-%m-%d")

formatted = dt.strftime("%A %d %B %Y")

print(formatted)