import os
import numpy as np
import matplotlib.pyplot as plt
from sigpy import shepp_logan
from skimage.transform import radon

def parent_dir(path, n=1):
    """Get the n-th parent directory of a given path."""
    for _ in range(n):
        path = os.path.dirname(path)
    return path

# Parameters
n = 512 # image size
theta = np.pi / 6  # 30 degrees

# Create a Shepp-Logan phantom image
phantom = np.abs(shepp_logan((n, n)))
# replace the zero values by nan
phantom[phantom == 0] = np.nan

plt.figure()
plt.imshow(phantom)
# draw x and y axis
plt.axhline(n//2, color='black', linestyle='-')
plt.axvline(n//2, color='black', linestyle='-')
# draw dashed arrows to represent the integration lines at angle theta and for different shifts
for t in np.linspace(-n//2, n//2, 8):
    plt.plot([n//2 + t*np.sin(theta) + n*np.cos(theta), n//2 + t*np.sin(theta) - n*np.cos(theta)],
             [n//2 + t*np.cos(theta) - n*np.sin(theta), n//2 + t*np.cos(theta) + n*np.sin(theta)],
             color='red', linestyle='--')
plt.xlim(0, n)
plt.ylim(n, 0)
plt.savefig(os.path.join(parent_dir(__file__, 2), 'img/posts/fourier_slice_theorem1.pdf'))

# replace the nan values by zeros
phantom[np.isnan(phantom)] = 0

# compute the Radon transform at angle theta
radon_at_theta = radon(phantom, [np.degrees(theta)], circle=True).flatten()


# plot the Radon transform at angle theta
plt.figure()
plt.plot(radon_at_theta)
plt.savefig(os.path.join(parent_dir(__file__, 2), 'img/posts/fourier_slice_theorem2.pdf'))

# compute the Fourier transform of the radon_at_theta curve
fourier_radon = np.fft.fftshift(np.fft.fft(radon_at_theta))
plt.figure()
plt.plot(np.abs(fourier_radon))
plt.yscale('log')
plt.savefig(os.path.join(parent_dir(__file__, 2), 'img/posts/fourier_slice_theorem3.pdf'))

# draw radial lines with different angles in a 2-D plot
angles = np.linspace(0, np.pi, 40, endpoint=False)
plt.figure()
for angle in angles:
    x = np.linspace(-n//2, n//2, n) * np.cos(angle)
    y = np.linspace(-n//2, n//2, n) * np.sin(angle)
    plt.plot(x, y, 'b', linewidth=0.4)
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.axis('equal')
plt.xlim(-n//2, n//2)
plt.ylim(-n//2, n//2)
plt.axis('off')
# draw a red dashed line at angle theta
plt.plot([-n//2 * np.cos(theta), n//2 * np.cos(theta)], [-n//2 * np.sin(theta), n//2 * np.sin(theta)], 'r--', linewidth=2)
plt.savefig(os.path.join(parent_dir(__file__, 2), 'img/posts/fourier_slice_theorem4.pdf'))

# # plot the Fourier transform of the phantom along the radial line at angle theta
# fourier_phantom = np.fft.fftshift(np.fft.fft2(phantom))
# freqs = np.fft.fftfreq(n) * n
# radial_line = np.array([fourier_phantom[int(n//2 + f*np.sin(theta)), int(n//2 + f*np.cos(theta))] for f in freqs])
# plt.figure()
# plt.plot(freqs, np.abs(radial_line), 'r', linewidth=2)
# plt.yscale('log')

plt.show()