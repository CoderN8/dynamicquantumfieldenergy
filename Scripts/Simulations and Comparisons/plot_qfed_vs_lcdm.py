import numpy as np
import matplotlib.pyplot as plt
from qfed_friedmann import qfed_hubble

z = np.linspace(0, 3, 300)
H0 = 70
Omega_m = 0.3
Omega_r = 8.24e-5
Omega_lambda = 0.7

plt.figure()
for mu, color in zip([0.0, 0.05, 0.1], ['blue', 'orange', 'red']):
    H_qfed = qfed_hubble(z, H0, Omega_m, Omega_r, mu)
    plt.plot(z, H_qfed, label=f'QFED μ={mu}', color=color)

H_lcdm = H0 * np.sqrt(Omega_m * (1 + z)**3 + Omega_r * (1 + z)**4 + Omega_lambda)
plt.plot(z, H_lcdm, '--', label='ΛCDM', color='black')

plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('QFED vs ΛCDM Expansion Rate')
plt.legend()
plt.grid()
plt.savefig('figure_1_qfed_vs_lcdm.png')