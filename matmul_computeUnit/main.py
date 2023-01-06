#include the compute unit
from compute import *
import sys

if __name__ == "__main__":
        
    #if -genInput=1, then do not run the test, just generate the input files
    if len(sys.argv) > 1:
        if sys.argv[1] == "-genInput=1":
            a, b = gen_matrixes()

            # only save the integer part of the result
            a = a.astype(int)
            b = b.astype(int)

            # multiply matrix a and b
            c = a.dot(b)
            c = c.astype(int)

            f =  open("mat_A.txt", "w")  # input vector file
            f1 = open("mat_B.txt", "w")  # input vector file
            f2 = open("mat_C.txt", "w")  # Output vector file
            # save matrix a 1 row per line ... 4 values in row ... also converted into 8 bit respective value
            file_Write(f, a)

            # Tacking transpose of b, as on dpu side we dont have to deal with [row * col] we can just [row * row]
            tran_b = transpose(b)
            file_Write(f1, b)

            # write matrix c : from bottom to top
            for i in range(3, -1, -1):
                for j in range(3, -1, -1):
                    f2.write(bin(c[i][j])[2:].zfill(25) + "\n")
                # f1.write("\n")

            # write matrix c : Each Line has only 1 result, out of 16, of a 4 by 4 matrix
            # for i in range(4):
            #     for j in range(4):
            #         f2.write(bin(c[i][j])[2:].zfill(25) + "\n")
            #     # f1.write("\n")
            
            f2.close()
            f.close()
            f1.close()

        elif sys.argv[1] == "-compRes=1": 
            #comparing the results from python file & vivado compute unit file
            compare_results("mat_C.txt", "results.txt")

        else:
            print("Invalid command line argument")
            print("Usage: python main.py -genInput=1 or -compRes=1")

    else:
        print("No command line argument")
        print("Usage: python main.py -genInput=1 or -compRes=1")