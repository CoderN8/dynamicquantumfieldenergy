import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
c = 299792.458  # speed of light in km/s
H0 = 70.0       # Hubble constant in km/s/Mpc
Omega_m = 0.3
Omega_lambda = 1.0 - Omega_m

# ΛCDM H(z)
def H_lcdm(z):
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + Omega_lambda)

# QFED H(z) with mu parameter
def H_qfed(z, mu=0.1):
    rho_qf = (1 + z)**(-3 * mu)
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + (1 - Omega_m) * rho_qf)

# D_V(z) calculator
def D_V(z, Hz_func):
    integrand = lambda z_: c / Hz_func(z_)
    D_M, _ = quad(integrand, 0, z)
    return ((D_M**2) * (c * z / Hz_func(z)))**(1/3)

# Redshift values for BAO
bao_z_vals = [0.106, 0.15, 0.32, 0.57, 0.61, 0.73]
D_V_lcdm = [D_V(z, H_lcdm) for z in bao_z_vals]
D_V_qfed = [D_V(z, lambda z_: H_qfed(z_, mu=0.1)) for z in bao_z_vals]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(bao_z_vals, D_V_lcdm, 'o-', label="ΛCDM", linewidth=2)
plt.plot(bao_z_vals, D_V_qfed, 's--', label="QFED (μ = 0.1)", linewidth=2)
plt.xlabel("Redshift $z$")
plt.ylabel(r"$D_V(z)$ [Mpc]")
plt.title("Figure 9: BAO Distance Comparison Between ΛCDM and QFED")
plt.legend()
plt.grid(True)
plt.savefig("figure_9_bao_dv_comparison.png")
plt.show()
