import os
from cmdstanpy import CmdStanModel
stan_file = os.path.join('bernoulli', 'bernoulli.stan')
model = CmdStanModel(stan_file=stan_file)
data_file = os.path.join('bernoulli', 'bernoulli.data.json')
fit = model.sample(data=data_file)
print(fit.stan_variable('theta'))
print(fit.summary())
