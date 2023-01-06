from fxpmath import Fxp
import random as r


def gen_matrixes():
    # create a random 4 by 4 array with each value 8 bits max
    a = Fxp([[r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]],
             signed=True, n_word=8, n_frac=0)

    b = Fxp([[r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]],
              signed=True, n_word=8, n_frac=0)

    return a, b

def transpose(b):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # iterate through rows
    for i in range(len(b)):
        # iterate through columns
        for j in range(len(b[0])):
            result[j][i] = b[i][j]
    return result

def comp_2cmp(a):
    # convert to 2's complement
    if a < 0:
        a = a + 256
    return a

def file_Write(f, a):
    # write matrix a
    for i in range(4):
        for j in range(4):
            if a[i][j] < 0:
                #write num in 2's complement
               f.write(bin(comp_2cmp(a[i][j]))[2:].zfill(8) + "\n")
            else:
                f.write(bin(a[i][j])[2:].zfill(8) + "\n")
        # f.write("\n")

def identity_matrix(scaler_a, scaler_b):
    # create a random 4 by 4 array with each value 8 bits max
    a = Fxp([[scaler_a, 0, 0, 0],
             [0, scaler_a, 0, 0],
             [0, 0, scaler_a, 0],
             [0, 0, 0, scaler_a]],
             signed=True, n_word=8, n_frac=0)

    b = Fxp([[scaler_b, 0, 0, 0],
             [0, scaler_b, 0, 0],
             [0, 0, scaler_b, 0],
             [0, 0, 0, scaler_b]],
              signed=True, n_word=8, n_frac=0)

    return a, b

#below funtion gen test matrix A,B with same values as it was first tested by compute_unit orignally
def custom_matrixes():
    a, b = identity_matrix(1,1)

    #multiply the first row of matrix with -4, 1, 7 , 3
    a[0][0] = -4
    a[0][1] = 1
    a[0][2] = 7
    a[0][3] = 3

    b[0][0] = 1
    b[1][0] = 2
    b[2][0] = 3
    b[3][0] = 10

    return a ,b

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

