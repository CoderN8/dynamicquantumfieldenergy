import numpy as np
import matplotlib.pyplot as plt
from qfed_friedmann import qfed_hubble

observational_data = np.array([
    [0.07, 69, 19.6], [0.12, 68.6, 26.2], [0.2, 72.9, 29.6],
    [0.28, 88.8, 36.6], [0.35, 82.7, 8.4], [0.48, 97, 62],
    [0.593, 104, 13], [0.68, 92, 8], [0.781, 105, 12],
    [0.875, 125, 17], [1.037, 154, 20], [1.3, 168, 17],
    [1.43, 177, 18], [1.53, 140, 14], [1.75, 202, 40]
])
z_obs, H_obs, H_err = observational_data.T

z = np.linspace(0.01, 2, 200)
plt.figure()
for mu in [0.01, 0.05, 0.1]:
    H_qfed = qfed_hubble(z, mu=mu)
    plt.plot(z, H_qfed, label=f'QFED μ={mu}')
plt.errorbar(z_obs, H_obs, yerr=H_err, fmt='o', label='Observations', color='black')
plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('QFED vs Hubble Parameter Measurements')
plt.legend()
plt.grid()
plt.savefig('figure_5_qfed_vs_ohd.png')