import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def qfed_hubble(z, H0=70, Omega_m=0.3, Omega_r=8.24e-5, mu=0.01):
    return H0 * np.sqrt(
        Omega_m * (1 + z)**3 +
        Omega_r * (1 + z)**4 +
        mu * (1 + z)**3 * np.log(1 + z)
    )

def angular_diameter_distance(z, mu):
    c = 299792.458
    integrand = lambda zp: c / qfed_hubble(zp, mu=mu)
    D_C, _ = quad(integrand, 0, z)
    return D_C / (1 + z)

z_star = 1089  # Redshift of last scattering surface
D_star_obs = 14700  # Mpc (Planck 2018 constraint)
err = 200

mus = [0.01, 0.05, 0.1]
D_star = [angular_diameter_distance(z_star, mu) for mu in mus]

plt.figure()
plt.axhline(D_star_obs, color='black', linestyle='--', label='Planck 2018')
plt.fill_between([0, 0.12], D_star_obs - err, D_star_obs + err, color='gray', alpha=0.3)
for mu, D in zip(mus, D_star):
    plt.plot(0.06, D, 'o', label=f'QFED μ={mu}')
plt.xlim(0, 0.12)
plt.ylabel('Angular Diameter Distance to CMB [Mpc]')
plt.xticks([])
plt.title('QFED vs Planck CMB Acoustic Scale')
plt.legend()
plt.grid()
plt.savefig('figure_8_qfed_vs_cmb.png')