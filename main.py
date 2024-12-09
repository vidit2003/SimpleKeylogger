#storing the keystrokes in a text file 
#file handling - How to read, write and append to a file

# Writing to a file (overwrites existing content)
with open("log.txt", 'w') as fileHandling:
    fileHandling.write("I'm Freaking Awesome")

# Reading from the file
with open("log.txt", 'r') as fileHandling:
    content = fileHandling.read()
    print(content)  # Outputs: I'm Freaking Awesome

# Appending to the file
with open("log.txt", 'a') as fileHandling:
    fileHandling.write("\nAppended text.")

# Reading the updated file content
with open("log.txt", 'r') as fileHandling:
    content = fileHandling.read()
    print(content)  # Outputs: I'm Freaking Awesome\nAppended text.




