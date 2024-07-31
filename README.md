# goit-algo-hw-10

Homework 10. Basic Algorithms and Data Structures at GoIT Neoversity

# Monte Carlo Integration vs. Analytical Integration

## Overview
This project demonstrates the application of the Monte Carlo method to calculate the definite integral of the function \( f(x) = x^2 \) over the interval [0, 2]. The result is compared with the analytical integration using the `quad` function from the SciPy library.

## Monte Carlo Method
The Monte Carlo method involves randomly sampling points in a defined region and calculating how many of them fall under the curve of the function. The area under the curve is then estimated based on the proportion of points below the curve.

### Result
- **Monte Carlo method:** Approximately 2.6758
- **Quad function from SciPy:** 2.6667

## Test Environment
The results were obtained on a MacBook Pro 2021 with an Apple M1 Pro processor.

## Conclusion
The result obtained using the Monte Carlo method is close to the analytical solution provided by the `quad` function, which confirms the accuracy of the Monte Carlo method for this integral. However, it's important to note that the Monte Carlo method can introduce some variance, which decreases as the number of random samples increases.

In this example, the Monte Carlo integration produced a slightly higher value compared to the exact result, but it is within an acceptable range for numerical methods.
