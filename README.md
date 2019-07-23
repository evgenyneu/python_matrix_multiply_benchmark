# Matrix multiplication benchmark in Python

This is a benchmark that measures time it takes to multiply two matrices in Python

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



Benchark data [multiply_1000_by_1000_matrices.xlsx](https://github.com/evgenyneu/image_compressor_c/blob/master/benchmark/multiply_1000_by_1000_matrices.xlsx)

C benchmark code: [benchmark_test.c](https://github.com/evgenyneu/image_compressor_c/blob/master/src/benchmark_test.c)
