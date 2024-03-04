import matplotlib.pyplot as plt
import numpy as np

# Input range
input_range = np.arange(1, 6)

# Big O functions
functions = [
    ("O(n)", lambda n: n),
    ("O(log(log n))", lambda n: np.log(np.log(n))),
    ("O(n^4)", lambda n: n**4),
    ("O(log n)", lambda n: np.log(n)),
    ("O(n^2)", lambda n: n**2),
    ("O(n^3)", lambda n: n**3),
    ("O(n^n)", lambda n: n**n)
]

# Plot each function
for label, func in functions:
    plt.plot(input_range, [func(n) for n in input_range], label=label)

# Add labels and legend
plt.xlabel('Input Size')
plt.ylabel('Runtime')
plt.title('Comparison of Big O Functions')
plt.legend()

# Add grid
plt.grid(True)

# Show the plot
plt.show()
