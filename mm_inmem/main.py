#include the compute unit
from inmem import *
import sys
import random as r

def genMatrix(fileName, len, count):
    f = open(fileName, "w")
    str = []
    for i in range(len):
        for j in range(4):
            str.append(bin(count)[2:].zfill(32))
            str.append("_")
            count += 1

        f.write("".join(str))
        f.write("\n")
        print("".join(str))
        str = []

    f.close()
    return count

def createBanksFiles(n,fileName):
    count = 0
    # count = genMatrix(fileName, n, count)

    bank00 = open("BankA_00.txt", "w")
    bank01 = open("BankA_01.txt", "w")
    bank02 = open("BankA_02.txt", "w")
    bank03 = open("BankA_03.txt", "w")

    f = open(fileName, 'r')
    for line in f:
        #write 32 bits to each bank and skip the _ saparater after every 32 bits in original file
        bank03.write(line[0:32])
        bank03.write("\n")
        bank02.write(line[33:65])
        bank02.write("\n")
        bank01.write(line[66:98])
        bank01.write("\n")
        bank00.write(line[99:131])
        bank00.write("\n")

    bank00.close()
    bank01.close()
    bank02.close()
    bank03.close()
    f.close()
# def genSpace(filename):
#     # read file and add space after every 32 bits
#

if __name__ == "__main__":

    #if -genInput=1, then do not run the test, just generate the input files
    if len(sys.argv) > 1:
        if sys.argv[1] == "-genInput=1":
            fileName = 'sram_input_banks_formet.txt'
            createBanksFiles(4,fileName)
                # genSpace(fileName+str(i)+'.txt')

        elif sys.argv[1] == "-compRes=1":
            #comparing the results from python file & vivado compute unit file
            compare_results("sram_input.txt", "sram_results.txt")

        else:
            print("Invalid command line argument")
            print("Usage: python main.py -genInput=1 or -compRes=1")

    else:
        print("No command line argument")
        print("Usage: python main.py -genInput=1 or -compRes=1")