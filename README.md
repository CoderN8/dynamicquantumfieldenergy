# Quantum Fluctuation Energy Density (QFED) Model

This repository contains the theoretical framework, simulation scripts, and observational comparison plots for the **QFED cosmological model**, which proposes a dynamic vacuum energy term as a function of redshift based on an imbalance in quantum fluctuation activity.

## Overview

The QFED model modifies the standard Friedmann equation by introducing a time-varying vacuum energy term proportional to:

\[
\rho_{qf}(z) = \mu (1+z)^3 \ln(1+z)
\]

This evolving term allows for accelerated expansion without invoking a static cosmological constant. We test the model against major observational datasets and standard cosmological predictions.

---

## Repository Structure

### 📁 Data

- `cleaned_pantheon_data.csv`: Cleaned distance modulus values from the Pantheon supernova dataset.

---

### 📁 Scripts

#### Core Model

- `qfed_friedmann.py`: Computes H(z) under QFED model.

#### Simulations and Comparisons

- `plot_qfed_vs_lcdm.py`: Compare QFED to ΛCDM Hubble evolution.
- `compare_with_pantheon.py`: Plot Pantheon supernovae vs QFED prediction.
- `plot_qfed_vs_hubble_data.py`: Compare QFED H(z) to observational data.
- `plot_qfed_vs_bao.py`: Compare QFED distance scales to BAO measurements.
- `plot_qfed_vs_cmb.py`: Test QFED against the CMB acoustic scale.
- `qfed_cosmic_age.py`: Estimate cosmic age under QFED.
- `plot_qfed_pressure_wz.py`: Plot effective equation-of-state parameter w(z).

#### Utilities

- `generate_pantheon_cleaned_csv.py`: Parses and cleans the Pantheon dataset.

---

### Figures

All figures are saved as `.png` in the working directory after running the respective script. Example filenames:

- `figure_1_qfed_vs_lcdm.png`
- `figure_2_qfed_vs_pantheon.png`
- `figure_5_qfed_vs_ohd.png`
- `figure_8_qfed_vs_cmb.png`
- `figure_9_bao_dv_comparison.png`

---

### Paper

This contains a PDF of the LaTeX formated paper with figures included.

---

## Requirements

- Python ≥ 3.8
- `numpy`
- `scipy`
- `matplotlib`
- `pandas`

Install with:

```bash
pip install -r requirements.txt
```

---

## License

MIT License

---

## Citation

If you use this code or reproduce these results, please cite:

> Girard, N., & ChatGPT (2025). *A Time-Varying Quantum Fluctuation Model for the Accelerating Expansion of the Universe.*

---

## Feedback

Peer review and feedback are welcome and appreciated! Please submit code/script/data updates as an open ticket or start a discussion thread on existing code. 

Feel free to email me feedback directly at n8@n8girard.com