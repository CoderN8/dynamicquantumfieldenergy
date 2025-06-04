import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.constants import c
import pandas as pd

# Constants
H0 = 70  # Hubble constant in km/s/Mpc
c_km_s = c / 1000  # Speed of light in km/s

# Cosmological parameters
Omega_m = 0.3
Omega_Lambda = 0.65
Omega_qf0 = 0.05

# Quantum fluctuation decay factor
def rho_qf_z(z, delta):
    return (1 + z)**(-delta)

# Modified H(z) including QFED term
def H_z(z, delta):
    return H0 * np.sqrt(
        Omega_m * (1 + z)**3 +
        Omega_Lambda +
        Omega_qf0 * rho_qf_z(z, delta)
    )

# Luminosity distance in Mpc
def D_L(z, delta):
    integral, _ = quad(lambda zp: 1.0 / H_z(zp, delta), 0, z)
    return (1 + z) * c_km_s * integral

# Distance modulus μ(z)
def mu_z(z_vals, delta):
    return 5 * np.log10([D_L(z, delta) * 1e6 / 10 for z in z_vals])  # Convert Mpc to pc

# Redshift range
z_vals = np.linspace(0.01, 2.0, 100)
delta_values = [1.0, 2.0, 3.0]

# Sample binned Pantheon-like data (mock)
pantheon_data = {
    "z": [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 1.8],
    "mu": [32.0, 36.6, 38.3, 40.9, 42.2, 43.3, 44.1, 44.9, 45.9, 46.6, 47.2, 47.9, 48.5]
}
pantheon_df = pd.DataFrame(pantheon_data)

# Plot μ(z)
plt.figure(figsize=(10, 6))
for delta in delta_values:
    mu_vals = mu_z(z_vals, delta)
    plt.plot(z_vals, mu_vals, label=f'δ = {delta}')

# Overlay mock Pantheon data
plt.scatter(pantheon_df['z'], pantheon_df['mu'], color='black', s=30, label='Pantheon (mock)', zorder=5)

plt.xlabel('Redshift z')
plt.ylabel('Distance Modulus μ(z)')
plt.title('Distance Modulus Comparison: QFED Model vs Pantheon Data (Mock)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
