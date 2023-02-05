#include the compute unit
from inmem import *
import sys

if __name__ == "__main__":
        
    #if -genInput=1, then do not run the test, just generate the input files
    if len(sys.argv) > 1:
        if sys.argv[1] == "-genInput=1":
           pass

        elif sys.argv[1] == "-compRes=1": 
            #comparing the results from python file & vivado compute unit file
            compare_results("sram_input.txt", "sram_results.txt")

        else:
            print("Invalid command line argument")
            print("Usage: python main.py -genInput=1 or -compRes=1")

    else:
        print("No command line argument")
        print("Usage: python main.py -genInput=1 or -compRes=1")