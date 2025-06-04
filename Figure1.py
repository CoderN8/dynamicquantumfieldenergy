import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

# Constants
H0 = 70  # Hubble constant today in km/s/Mpc
H0_SI = H0 * 1000 / (3.086e22)  # Convert to 1/s
rho_crit0 = 3 * H0_SI**2 / (8 * np.pi * G)  # Critical density today in kg/m^3

# Define the Omega parameters
Omega_m = 0.3
Omega_Lambda = 0.7
# Omega_qf will be dynamically computed to maintain a flat universe (Ω_total = 1)
def H_z_modified(z, delta, Omega_qf0):
    """Modified H(z) using quantum fluctuation energy density with evolving delta."""
    Omega_m_eff = Omega_m
    Omega_Lambda_eff = Omega_Lambda
    Omega_qf_z = Omega_qf0 * (1 + z)**(-delta)
    return H0 * np.sqrt(Omega_m_eff * (1 + z)**3 + Omega_Lambda_eff + Omega_qf_z)

# Redshift range
z_vals = np.linspace(0, 3, 500)

# Try different delta values with a small Ω_qf today
delta_values = [1.0, 2.0, 3.0, 4.0]
Omega_qf0 = 0.05

plt.figure(figsize=(10, 6))
for delta in delta_values:
    Hz_vals = H_z_modified(z_vals, delta, Omega_qf0)
    plt.plot(z_vals, Hz_vals, label=f'δ = {delta}')

# Plot standard ΛCDM for reference
Hz_LCDM = H0 * np.sqrt(Omega_m * (1 + z_vals)**3 + Omega_Lambda)
plt.plot(z_vals, Hz_LCDM, 'k--', label='ΛCDM Reference')

plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('H(z) with Evolving Quantum Fluctuation Term')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
