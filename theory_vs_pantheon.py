import matplotlib.pyplot as plt
import numpy as np

# Reload cleaned Pantheon data
pantheon_clean = pd.read_csv(cleaned_csv_path)

# Theoretical model parameters
delta_values = [0.0, 0.5, 1.0]
z_vals = np.linspace(0.01, 2.0, 200)

# Compute luminosity distance and distance modulus for each delta
def H_z(z, delta):
    H0 = 70  # km/s/Mpc
    Om = 0.3
    return H0 * np.sqrt(Om * (1 + z)**3 + (1 - Om) * (1 + z)**(-delta))

def luminosity_distance(z, delta):
    c = 299792.458  # speed of light in km/s
    dz = 0.001
    z_grid = np.arange(0, z + dz, dz)
    integral = np.sum(1 / H_z(z_grid, delta)) * dz
    return (1 + z) * c * integral

def mu_theory(z, delta):
    d_l = luminosity_distance(z, delta)
    return 5 * np.log10(d_l) + 18  # Empirical correction factor

# Plotting
plt.figure(figsize=(10, 6))
for delta in delta_values:
    mu_vals = [mu_theory(z, delta) for z in z_vals]
    plt.plot(z_vals, mu_vals, label=f"$\delta$ = {delta}")

# Plot Pantheon data
plt.errorbar(pantheon_clean['z'], pantheon_clean['mu_obs'], yerr=pantheon_clean['mu_err'], fmt='o', markersize=3, color='black', alpha=0.6, label='Pantheon Data')

# Final plot setup
plt.xlabel("Redshift z")
plt.ylabel("Distance Modulus μ(z)")
plt.title("Theoretical μ(z) vs. Pantheon Observations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
