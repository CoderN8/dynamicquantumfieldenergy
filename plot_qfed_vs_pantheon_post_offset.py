import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Load the cleaned Pantheon dataset from the uploaded file
pantheon_cleaned = pd.read_csv("/mnt/data/cleaned_pantheon_data.csv")

# Constants
c = 299792.458  # speed of light in km/s
H0 = 70  # Hubble constant in km/s/Mpc
delta_values = [0.5, 1.0, 1.5, 2.0]
mu_offset = 18.1

# Hubble function with quantum fluctuation energy density
def H_qfed(z, delta):
    return H0 * np.sqrt((1 + z)**3 + (1 + z)**(-delta))

# Luminosity distance function
def D_L(z, delta):
    integral, _ = quad(lambda z_prime: 1 / H_qfed(z_prime, delta), 0, z)
    return (1 + z) * c * integral

# Distance modulus function
def mu_qfed(z, delta):
    d_l = D_L(z, delta)
    return 5 * np.log10(d_l * 1e6 / 10)  # Convert Mpc to pc

# Redshift range for model plotting
z_vals = np.linspace(0.01, 2.3, 300)

# Plotting
plt.figure(figsize=(10, 6))

# Plot Pantheon cleaned dataset
plt.errorbar(pantheon_cleaned['z'], pantheon_cleaned['mu_obs'], yerr=pantheon_cleaned['mu_err'],
             fmt='o', markersize=3, color='black', alpha=0.6, label="Pantheon Observations")

# Plot theoretical models with offset
for delta in delta_values:
    mu_vals = [mu_qfed(z, delta) - mu_offset for z in z_vals]
    plt.plot(z_vals, mu_vals, label=f"QFED Model ($\\delta$ = {delta})")

plt.xlabel("Redshift (z)")
plt.ylabel("Distance Modulus (μ)")
plt.title("Figure 4: QFED Model vs Pantheon Observations (Post-Offset)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("/mnt/data/figure_4_qfed_vs_pantheon_post_offset.png", dpi=300)
plt.show()
