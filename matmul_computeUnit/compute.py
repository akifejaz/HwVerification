from fxpmath import Fxp
import random as r


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


def file_Write(f, a):
    # write matrix a
    for i in range(4):
        for j in range(4):
            f.write(bin(a[i][j])[2:].zfill(8) + "\n")
        # f.write("\n")


# open file to write
f =  open("computeUnit_A.txt", "w")  # input vector file
f1 = open("computeUnit_B.txt", "w")  # input vector file
f2 = open("computeUnit_C.txt", "w")  # Output vector file

for test in range(0, 1, 1):
    # create a random 4 by 4 array with each value 8 bits max
    a = Fxp([[r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]],
             signed=False, n_word=8, n_frac=0)

    b = Fxp([[r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)],
             [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]],
              signed=False, n_word=8, n_frac=0)

    # multiply matrix a and b
    c = a.dot(b)

    # only save the integer part of the result
    a = a.astype(int)
    b = b.astype(int)
    c = c.astype(int)

    # save matrix a 1 row per line ... 4 values in row ... also converted into 8 bit respective value
    file_Write(f, a)

    # Tacking transpose of b, as on dpu side we dont have to deal with [row * col] we can just [row * row]
    tran_b = transpose(b)
    file_Write(f1, b)

    # write matrix c : Each Line has only 1 result, out of 16, of a 4 by 4 matrix
    for i in range(4):
        for j in range(4):
            f2.write(bin(c[i][j])[2:].zfill(25) + "\n")
        # f1.write("\n")

print(a)
print(tran_b)
print(c)
f.close()
f1.close()
f2.close()
