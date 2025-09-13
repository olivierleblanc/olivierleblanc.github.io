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

# Moreau envelope of |.| (L1 norm) in 1D
def moreau_envelope_l1(x, lam):
    return np.where(np.abs(x) <= lam,
                    0.5/lam * x**2,
                    np.abs(x) - lam/2)

y = moreau_envelope_l1(x, lam)

# Original L1 norm
y_l1 = np.abs(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_l1, label=r"$|x|$", linestyle="--")
plt.plot(x, y, label=fr"Moreau envelope M$_{{\lambda}}|x|$ with $\lambda={int(lam)}$", linewidth=2)
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Moreau Envelope of the absolue value")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(parent_dir(__file__, 2), 'img/posts/moreau_envelope.png'))

plt.show()
