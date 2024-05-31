import os 

# File path for read, write and append operations
read_file_path = "C:/Users/UGWU MOSES C/Desktop/TSR-ASSIGNMENTS/Cloud-Engineer-Cohort-September-2023/Python-projects/sample.txt"
write_file_path = "C:/Users/UGWU MOSES C/Desktop/TSR-ASSIGNMENTS/Cloud-Engineer-Cohort-September-2023/Python-projects/sample.txt"
append_file_path = "C:/Users/UGWU MOSES C/Desktop/TSR-ASSIGNMENTS/Cloud-Engineer-Cohort-September-2023/Python-projects/sample.txt"

#read from a file
with open(read_file_path, 'r') as file:
    file_contents = file.read()
print("File contents:", file_contents) 

# write to a file
data_to_write = "This is a sample text."
with open(write_file_path, 'w') as file:
    file.write(data_to_write)
print("Data written to file.") 

# Append to a file
data_to_append = "\nAppending additional text." 
with open(append_file_path, 'a') as  file:
    file.write(data_to_append)
print("Data appended to file.") 

# check file existence and remove
if os.path.exists(append_file_path):
    os.remove(append_file_path)
    print("File deleted")
else:
    print("File does not exist.") 


