from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0) # sets the file's current position

def print_a_line(line_count, f):
    print(line_count, f.readline())
    
#text.txt
current_file = open(input_file)

print("\n\tFirst let's print the whole file:\n")

#text.txt
print_all(current_file)

print("\n\tNow, let's rewind, kind of like a tape.")

#go back from index 0
rewind(current_file)
print('\n')
#print again
print_all(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)