# Test Benches -Python



## TestBench for Matmul DPU

This is the simple script that generate matrixes of size 4 by 4, for testing Matmul.



### Usage:

```
cd fxmath
pip install fxmath

cd .. & cd matmul_dpu
python mult.py
```



### Details:

Script generates 4 * 4 matrix with random value of max length of 8 bit. The `matmul_dpu_tb.txt` is basically the file with all the input values of matrix. First 4 lines are of Matrix A, and second 4 lines are of Matrix B and so on.. `output_dpu_tb.txt` file has the result values after multiplication. Each line has only single 25 bit value.

Each line has 32 bit number, because we want 8 bit number and matrix is 4 * 4 so, `8 * 4 = 32.`



## TestBench for 2D Convolution



### Usage:

```
cd fxmath
pip install fxmath

cd .. & cd conv2D
python conv.py
```



### Details:
