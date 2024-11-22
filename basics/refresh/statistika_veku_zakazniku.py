
import pandas as pd
import statsmodels.api as sm

# Příklad dat
data = pd.DataFrame({'Věk': [25, 30, 35, 40], 'Pohlaví': [1, 0, 1, 0]})

# Přidání konstanty
X = sm.add_constant(data['Věk'])
y = data['Pohlaví']

# Logistická regrese
model = sm.Logit(y, X).fit()
print(model.summary())
