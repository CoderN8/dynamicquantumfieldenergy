import numpy as np
from scipy.integrate import quad
from qfed_friedmann import qfed_hubble

def age_of_universe(mu):
    integrand = lambda z: 1 / ((1 + z) * qfed_hubble(z, mu=mu))
    integral, _ = quad(integrand, 0, 1000)
    return integral * 9.78  # Convert to Gyr

for mu in [0.01, 0.05, 0.1]:
    print(f"Universe age for μ={mu}: {age_of_universe(mu):.2f} Gyr")