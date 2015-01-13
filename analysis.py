import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


# df3 = DataFrame(randn(1000, 2), columns=['B', 'C']).cumsum()

# df3['A'] = Series(list(range(len(df))))

# df3.plot(x='A', y='B')

# import matplotlib.pyplot as plt
# plt.figure(); df.plot();

df = pd.read_csv("trafficking_data.csv")

results_victims = smf.ols('df["Adult victims"] ~ df["gdp"] + df["policy index"]',data=df).fit()

df = df.replace(np.nan,0)
ind_vars = df[["gdp","policy index","child victims"]]

results_prosecuted = sm.OLS(df["persons prosecuted"], ind_vars).fit()
print results_victims.summary()
print "Parameters:", results_victims.params
print "R^2", results_victims.rsquared

print results_prosecuted.summary()
print "Parameters:", results_prosecuted.params
print "R^2", results_prosecuted.rsquared