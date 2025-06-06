import numpy as np

def qfed_hubble(z, H0=70, Omega_m=0.3, Omega_r=8.24e-5, mu=0.01):
    """Compute H(z) using the QFED model."""
    return H0 * np.sqrt(
        Omega_m * (1 + z)**3 +
        Omega_r * (1 + z)**4 +
        mu * (1 + z)**3 * np.log(1 + z)
    )