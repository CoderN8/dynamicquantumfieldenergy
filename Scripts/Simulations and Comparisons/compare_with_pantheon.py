import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from qfed_friedmann import qfed_hubble

pantheon = pd.read_csv('cleaned_pantheon_data.csv')
z = pantheon['z'].values
mu_obs = pantheon['mu'].values

H0 = 70
mu = 0.05
Omega_m = 0.3
Omega_r = 8.24e-5

def lum_distance(z, H_func):
    c = 299792.458
    dz = 0.001
    z_vals = np.arange(0, max(z)+dz, dz)
    integrand = 1 / H_func(z_vals)
    integral = np.cumsum(integrand) * dz
    dL = (1 + z_vals) * c * integral
    return np.interp(z, z_vals, dL)

dL = lum_distance(z, lambda z: qfed_hubble(z, H0, Omega_m, Omega_r, mu))
mu_model = 5 * np.log10(dL) + 25 - 18.0  # Apply offset

plt.figure()
plt.scatter(z, mu_obs, s=10, label='Pantheon')
plt.plot(z, mu_model, color='red', label=f'QFED μ={mu}')
plt.xlabel('Redshift z')
plt.ylabel('Distance Modulus μ(z)')
plt.title('QFED vs Pantheon')
plt.legend()
plt.grid()
plt.savefig('figure_2_qfed_vs_pantheon.png')