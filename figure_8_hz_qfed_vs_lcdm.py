import pandas as pd

# Generate the H(z) comparison figure to z=1100
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(z_vals, Hz_lcdm, label=r"$H(z)$ $\Lambda$CDM", linewidth=2)
ax.plot(z_vals, Hz_qfed, label=r"$H(z)$ QFED ($\mu=0.1$)", linestyle='--', linewidth=2)
ax.set_xlabel("Redshift $z$")
ax.set_ylabel("Hubble Parameter $H(z)$ [km/s/Mpc]")
ax.set_title("Figure 8: $H(z)$ Comparison up to $z=1100$")
ax.legend()
ax.grid(True)

# Save the figure
fig_path = "/mnt/data/figure_8_hz_qfed_vs_lcdm.png"
fig.savefig(fig_path)

# Also save the data points used in this figure
data = pd.DataFrame({
    "z": z_vals,
    "Hz_LCDM": Hz_lcdm,
    "Hz_QFED_mu_0.1": Hz_qfed
})
csv_path = "/mnt/data/figure_8_data.csv"
data.to_csv(csv_path, index=False)

fig_path, csv_path
