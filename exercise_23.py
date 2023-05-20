import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline() # read a line from the file

    if line: # if the line is not empty
        print_line(line, encoding, errors) # print the line
        return main(language_file, encoding, errors) # call main again