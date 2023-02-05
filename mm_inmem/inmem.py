from fxpmath import Fxp
import random as r


def compare_results(file1, file2):
    # open file to read
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    # read line by line
    line1 = f1.readline()
    line2 = f2.readline()

    # initialize counter for line number
    line_no = 1
    fail = 0

    # loop if either file1 or file2 has not reached EOF
    while line1 or line2:
        # strip the leading whitespaces
        line1 = line1.rstrip()
        line2 = line2.rstrip()

        # compare the lines from both file
        if line1 != line2:
            # if a line does not exist on file2 then mark the output with + sign
            if line2 == None:
                line2 = "+"
            # otherwise output the line on file2 and mark it with > sign
            elif line1 == None:
                line1 = ">"

            # print the error message
            print("Test Failed @ Line-%d" % line_no)
            print("File1: %s" % line1)
            print("File2: %s" % line2)

            fail = fail + 1
            # print a blank line
            print()

        # read the next line from the file
        line1 = f1.readline()
        line2 = f2.readline()

        # increment line counter
        line_no += 1
    
    #show the failed and passed tests
    print("Failed: ", fail)
    print("Passed: ", line_no - fail - 1) # -1 is to remove the last line

