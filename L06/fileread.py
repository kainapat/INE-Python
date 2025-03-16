# This program reads and displays the contents
# of the philosophers.txt file.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')
    
    # Read the file's contents.
    file_contents = infile.read()
    
    # Close the file.
    infile.close()
    print(file_contents)

main()