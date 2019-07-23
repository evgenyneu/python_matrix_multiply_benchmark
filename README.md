# Matrix multiplication benchmark in Python

This is a benchmark that measures time it takes to multiply two matrices in Python. Here we first use the brute force matrix multiplication method that uses three nested loops. Next we compare this method with NymPy's matmul function. NumPy internally uses C code, which in turn calls a dgemm function from a [BLAS library](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms). We also compare the results with a similar implementation written in C, that also has both a naive nested loops and a BLAS implementation.

## Setup

```
git clone https://github.com/evgenyneu/python_matrix_multiply_benchmark.git
cd python_matrix_multiply_benchmark
```

## Run benchmark

Install `pytest` with

```
pip install pytest
```

Run the benchmark

```
pytest
```

## Results

```
  0.14 ± 0.01 s: Python, numpy np.matmul
  0.16 ± 0.01 s: C, OpenBLAS dgemm
  8.80 ± 0.02 s: C, three loops
252    ± 5 s   : Python, three loops
```

The benchmark was run on MacBook Pro (Retina, 13-inch, Late 2012) computer with a dual core 2.5 GHz Intel Core i5 processor and 8 GB of RAM.

Benchark data [multiply_1000_by_1000_matrices.xlsx](https://github.com/evgenyneu/image_compressor_c/blob/master/benchmark/multiply_1000_by_1000_matrices.xlsx)

C benchmark code: [benchmark_test.c](https://github.com/evgenyneu/image_compressor_c/blob/master/src/benchmark_test.c)
