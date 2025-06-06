import numpy as np
import matplotlib.pyplot as plt

def rho_qfed(z, mu):
    return mu * (1 + z)**3 * np.log(1 + z)

def w_qfed(z, mu):
    rho = rho_qfed(z, mu)
    drho_dz = np.gradient(rho, z)
    return -1 + ((1 + z) / (3 * rho)) * drho_dz

z = np.linspace(0.001, 3, 300)
mus = [0.01, 0.05, 0.1]

plt.figure()
for mu in mus:
    w = w_qfed(z, mu)
    plt.plot(z, w, label=f'μ={mu}')
plt.xlabel('Redshift z')
plt.ylabel('w(z)')
plt.title('Equation of State Parameter w(z) for QFED')
plt.grid()
plt.legend()
plt.savefig('figure_qfed_wz.png')