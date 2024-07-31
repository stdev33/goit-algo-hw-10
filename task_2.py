import numpy as np
import scipy.integrate as spi


# Define the function f(x)
def f(x):
    return x ** 2


# Integration limits
a = 0  # Lower limit
b = 2  # Upper limit


# Implementation of the Monte Carlo method
def monte_carlo_integration(func, low_lim, up_lim, num_samples=10000):
    # Generate random points
    x_random = np.random.uniform(low_lim, up_lim, num_samples)
    y_random = np.random.uniform(0, max(func(np.linspace(low_lim, up_lim, 1000))), num_samples)

    # Count how many points fall under the curve
    under_curve = y_random < func(x_random)

    # Fraction of points under the curve
    fraction = np.sum(under_curve) / num_samples

    # Area of the rectangle
    rect_area = (up_lim - low_lim) * max(func(np.linspace(low_lim, up_lim, 1000)))

    # Area under the curve (integral approximation)
    area = fraction * rect_area

    return area


# Calculate the integral using the Monte Carlo method
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples=100000)
print(f"Monte Carlo method: {monte_carlo_result}")

# Calculate the integral using the quad function from SciPy
quad_result, quad_error = spi.quad(f, a, b)
print(f"Quad function result: {quad_result}")
