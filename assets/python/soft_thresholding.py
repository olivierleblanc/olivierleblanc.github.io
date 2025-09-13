import os
import numpy as np
import matplotlib.pyplot as plt

def parent_dir(path, n=1):
    """Get the n-th parent directory of a given path."""
    for _ in range(n):
        path = os.path.dirname(path)
    return path

# set text font to CMU serif
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["CMU Serif"],
    "font.size": 14
})

# Parameters
lam = 1.0
x = np.linspace(-3, 3, 400)

# Soft-thresholding operator
def soft_threshold(x, lam):
    return np.sign(x) * np.maximum(np.abs(x) - lam, 0.0)

y_soft = soft_threshold(x, lam)

plt.figure(figsize=(8, 5))
plt.plot(x, y_soft, label="Soft-thresholding $\mathrm{prox}_{{\lambda \|\cdot\|_1}}(x)$, $\lambda=1$", c="orange", linewidth=2)
plt.plot(x, x, linestyle="--", color="gray", label="Identity $x$")
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Soft-thresholding Operator")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(parent_dir(__file__, 2), 'img/posts/soft_thresholding.png'))

plt.show()
