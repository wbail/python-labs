# The new_directory function creates a new directory inside the current working directory,
# then creates a new empty file inside the new directory, and returns the list of files in that directory.
# Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".

import os

def new_directory(directory, filename):
  
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
      
    # Creates the directory
    os.mkdir(directory)

  # Goes inside the new directory
  os.chdir(directory)
  
  # Get the current directory path
  current = os.getcwd()

  # "Mounts" the full path directory/filename (Eg: C:\Users\JoeDoe\Desktop\PythonPrograms\script.py)
  filePath = os.path.join(current, filename)

  # Creates the file inside the newly created directory
  with open(filePath, 'w') as file:
    pass

  # Return the list of files in the new directory
  files = os.listdir(current)
  
  return files

directory = "PythonPrograms"
filename = "script.py"

print(new_directory(directory, filename))
