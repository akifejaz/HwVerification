from fxpmath import Fxp
import random as r
import numpy as np

'''
IMP Calculations: 

Output size = Full
Output size = (matrixlen-kernalen+1 , matrixlen-kernalen+1)
In our case = (64+3-1 , 64+3-1) = (64+2 , 64+2) = (66,66)

reference : https://www.mathworks.com/help/vision/ref/2dconvolution.html

'''


# def convFull(matrix,kernal,matrixlen,kernalen):
#     result = np.zeros((matrixlen+kernalen-1,matrixlen+kernalen-1))
#     for i in range(matrixlen):
#         for j in range(matrixlen):
#             for k in range(kernalen):
#                 for l in range(kernalen):
#                     result[i+k][j+l] += matrix[i][j]*kernal[k][l]
#     return result

def conv(matrix, kernal, matrixlen, kernalen, type):
    if type == 'full' or type == 'Full':
        result = np.zeros((matrixlen + kernalen - 1, matrixlen + kernalen - 1))
        for i in range(matrixlen):
            for j in range(matrixlen):
                for k in range(kernalen):
                    for l in range(kernalen):
                        result[i + k][j + l] += matrix[i][j] * kernal[k][l]
        return result

    elif type == 'same' or type == 'Same':
        # result = np.zeros((matrixlen,matrixlen))
        # for i in range(matrixlen):
        #     for j in range(matrixlen):
        #         for k in range(kernalen):
        #             for l in range(kernalen):
        #                 result[i][j] += matrix[i+k][j+l]*kernal[k][l]
        # return result
        pass

    elif type == 'valid' or type == 'Valid':
        result = np.zeros((matrixlen - kernalen + 1, matrixlen - kernalen + 1))
        for i in range(matrixlen - kernalen + 1):
            for j in range(matrixlen - kernalen + 1):
                result[i][j] = np.sum(matrix[i:i + kernalen, j:j + kernalen] * kernal)
        return result

    else:
        print("Invalid type")
        return 0


# each line has 64 values converted into bin : total 64*8 = 512 bits
def file_Write(f, matrix):
    # write 1 row per line
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            f.write(bin(matrix[i][j])[2:].zfill(8) + "\n")
        # f.write("\n")


# main function
if __name__ == "__main__":
    # 64 by 64 matrix with 8 bit values
    matrix = Fxp([[r.randint(0, 255) for i in range(64)] for j in range(64)], signed=False, n_word=8, n_frac=0)
    kernel = Fxp([[r.randint(0, 255) for i in range(3)] for j in range(3)], signed=False, n_word=8, n_frac=0)
    print(matrix, matrix.shape)
    print(kernel, kernel.shape)

    # convert to int
    matrix = matrix.astype(int)
    kernel = kernel.astype(int)

    # open file to write
    f = open("./version2.0/conv_inputV2.txt", "w")  # input vector file
    f1 = open("./version2.0/conv_kernalV2.txt", "w")  # input kernal file
    f2 = open("./version2.0/conv_outputV2.txt", "w")  # output file / Results file
    file_Write(f, matrix)
    file_Write(f1, kernel)

    res = conv(matrix, kernel, 64, 3, 'valid')
    res = res.astype(int)
    print(res, res.shape)

    # assuming res to max 25 bits : will change actual to later
    for i in range(len(res)):
        for j in range(len(res)):
            f2.write(bin(res[i][j])[2:].zfill(25) + "\n")
        # f2.write("\n")

    f.close()
    f1.close()
    f2.close()

'''
#Test-01
matrix = np.array([[1, 4, 4, 2, 1, 0, 0, 1, 0, 0, 3, 3, 3, 4], 
                   [0, 2, 0, 2, 0, 3, 4, 4, 2, 1, 1, 3, 0, 4],
                   [1, 1, 0, 0, 3, 4, 2, 4, 4, 2, 3, 0, 0, 4],
                   [4, 0, 1, 2, 0, 2, 0, 3, 3, 3, 0, 4, 1, 0],
                   [3, 0, 0, 3, 3, 3, 2, 0, 2, 1, 1, 0, 4, 2],
                   [2, 4, 3, 1, 1, 0, 2, 1, 3, 4, 4, 0, 2, 3],
                   [2, 4, 3, 3, 2, 1, 4, 0, 3, 4, 1, 2, 0, 0],
                   [2, 1, 0, 1, 1, 2, 2, 3, 0, 0, 1, 2, 4, 2],
                   [3, 3, 1, 1, 1, 1, 4, 4, 2, 3, 2, 2, 2, 3]])
kernel = np.array([[0, 1, 3, 3, 2], 
                   [0, 1, 3, 1, 3],
                   [1, 1, 2, 0, 2],
                   [2, 2, 3, 2, 0],
                   [1, 3, 1, 2, 0]])
'''