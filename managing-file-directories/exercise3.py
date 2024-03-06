# The file_date function creates a new file in the current working directory,
# checks the date that the file was modified, and returns just the date portion of the timestamp 
# in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory

  with open(filename, 'w') as file:
    pass

  fileCreationTimestamp = os.path.getmtime(filename)

  # Convert the timestamp into a readable format, then into a string
  
  timestamp = datetime.datetime.fromtimestamp(fileCreationTimestamp)
  
  # Return just the date portion 
  
  timestampInDateIsoFormat = timestamp.strftime("%Y-%m-%d")
  
  return timestampInDateIsoFormat

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
