import pandas as pd

df = pd.read_csv('lcparam_full_long_zhel.csv', delim_whitespace=True, comment='#',
                 names=["name", "zcmb", "zhel", "dz", "mb", "dmb", "x1", "dx1", "color",
                        "dcolor", "3rdvar", "d3rdvar", "cov_m_s", "cov_m_c", "cov_s_c",
                        "set", "ra", "dec", "biascor"])

df_clean = df[["zhel", "mb"]].rename(columns={"zhel": "z", "mb": "mu"})
df_clean.to_csv('cleaned_pantheon_data.csv', index=False)