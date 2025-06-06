import numpy as np
import matplotlib.pyplot as plt
from qfed_friedmann import qfed_hubble
from scipy.integrate import quad

bao_data = np.array([
    [0.106, 457, 27], [0.15, 664, 25], [0.32, 1264, 25],
    [0.57, 2056, 20], [0.73, 2516, 86]
])

def D_V(z, mu):
    c = 299792.458
    integrand = lambda zp: c / qfed_hubble(zp, mu=mu)
    D_C, _ = quad(integrand, 0, z)
    Hz = qfed_hubble(z, mu=mu)
    return ((D_C**2 * c * z / Hz)**(1/3))

z_bao, dv_bao, err = bao_data.T
z_vals = np.linspace(0.01, 0.8, 100)

plt.figure()
for mu in [0.01, 0.05, 0.1]:
    Dv_model = [D_V(z, mu) for z in z_vals]
    plt.plot(z_vals, Dv_model, label=f'QFED μ={mu}')
plt.errorbar(z_bao, dv_bao, yerr=err, fmt='o', color='black', label='BAO')
plt.xlabel('Redshift z')
plt.ylabel(r'$D_V(z)$ [Mpc]')
plt.title('QFED vs BAO Measurements')
plt.legend()
plt.grid()
plt.savefig('figure_9_bao_dv_comparison.png')