#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_table("result.dat", sep = '\t')
lambd = np.arange(0.1, 0.92, 0.01)
mu = 1.0

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
que_sizes = df['q_size'].unique()
"""
plt.figure()

plt.errorbar(df['rho'], df['av_serv_t'], df['d_av_serv_t'], marker = 'x', linestyle = 'None', label = 'sim.')
rho = lambd / mu
plt.plot(lambd / mu, 0.5 * (1 / (mu - lambd) - 1/mu) + 1/mu, marker = 'None', linestyle = '-', label = 'an.m.')
plt.plot(lambd / mu, 1 / mu + (1 / mu) * rho / (2 * (1 - rho)), marker = 'None', linestyle = '-', label = 'an.m.')
#page 207, formula 5.63
plt.xlabel(r'$\lambda / \mu$')
plt.ylabel('Average service time')
plt.grid()
plt.legend(loc='best')
plt.savefig('../plots/service_time.png')

"""

################# plotting average service time
plt.figure()

for (q_size, color) in zip(que_sizes, colors[0:len(que_sizes) - 1]):

	df1 = df[df['q_size'] == q_size]
	#simulation results
	plt.errorbar(df1['rho'], df1['av_serv_t'], df1['d_av_serv_t'], marker = 'x', linestyle = 'None', color = color, label = 'sim., q = ' + str(q_size))

	rho = lambd / mu
	p0 = (1 - rho) / (1 - rho ** (q_size + 2))
	#failure probability
	pf = rho ** (q_size + 1) * p0
	#average queue size
	Nq = p0 * sum([(rho ** (n+1)) * n for n in range(1, q_size+1, 1)])
	#total service time
	S = Nq / (lambd * (1 - pf)) + (1 / mu)
	#analytical results
	plt.plot(rho, S, marker = 'None', linestyle = '-', color = color, label = 'an.m., q = ' + str(q_size))

plt.xlabel(r'$\lambda / \mu$')
plt.ylabel('Average service time')
plt.grid()
plt.legend(loc='best')
plt.savefig('service_time.png')


#probability of failure
plt.figure()

for (q_size, color) in zip(que_sizes, colors[0:len(que_sizes) - 1]):

	df1 = df[df['q_size'] == q_size]
	#simulation results
	plt.errorbar(df1['rho'], df1['f_prob'], df1['d_f_prob'], marker = 'x', linestyle = 'None', color = color, label = 'sim., q = ' + str(q_size))

	rho = lambd / mu
	p0 = (1 - rho) / (1 - rho ** (q_size + 2))
	#failure probability
	pf = rho ** (q_size + 1) * p0
	#analytical results
	plt.plot(rho, pf, marker = 'None', linestyle = '-', color = color, label = 'an.m., q = ' + str(q_size))

plt.xlabel(r'$\lambda / \mu$')
plt.ylabel('Failure probability')
plt.grid()
plt.legend(loc='best')
plt.savefig('failure_prob.png')

