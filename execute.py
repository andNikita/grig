#!/usr/bin/python3

import subprocess
from scipy import stats
import argparse
import numpy as np

def parseArguments():
	parser = argparse.ArgumentParser()

	parser.add_argument("lambd", type=float)
	parser.add_argument("mu", type=float)
	parser.add_argument("q_size", type=int)
	parser.add_argument("simtime", type=float)
	parser.add_argument("--alpha", type=float, default=0.01)
	parser.add_argument("--beta", type=float, default=0.1)
	parser.add_argument("--runMode", type=str, default='static')

	return parser.parse_args()

def executeProgram(run, args):
	result = subprocess.Popen("../src/scenario {} {} {} {} {}".format(run, args.lambd, args.mu, args.q_size, args.simtime),
								shell=True, stdout = subprocess.PIPE).stdout.read().decode("utf-8").split(" ")
	return result

def confidenceInterval (serviceTimes, alpha):
	return np.sqrt(np.var(serviceTimes, ddof=1)) / np.sqrt(len(serviceTimes)) * stats.t.ppf(1-alpha/2, len(serviceTimes)-1) 

def main():
	args = parseArguments()

	servedPackets = []
	serviceTimes = []
	waitingTimes = []
	queueSizes = []
	utilization = []
	failedPackets = []
  
	if (args.runMode == "dynamic"):
	  	#run = seed
		for run in range(1, 3):
			print(executeProgram(run,args))
			servedPackets += [float(executeProgram(run, args)[0])]
			serviceTimes += [float(executeProgram(run, args)[1])]
			waitingTimes += [float(executeProgram(run, args)[2])]
			queueSizes += [float(executeProgram(run, args)[3])]
			utilization += [float(executeProgram(run, args)[4])]
			failedPackets += [float(executeProgram(run, args)[5])]

		run = 2
		while(	confidenceInterval(servedPackets, args.alpha) > args.beta and
				confidenceInterval(serviceTimes, args.alpha) > args.beta and
				confidenceInterval(waitingTimes, args.alpha) > args.beta and
				confidenceInterval(queueSizes, args.alpha) > args.beta and
				confidenceInterval(utilization, args.alpha) > args.beta and
				confidenceInterval(failedPackets, args.alpha) > args.beta):
			run = run + 1 

			servedPackets += [float(executeProgram(run, args)[0])]
			serviceTimes += [float(executeProgram(run, args)[1])]
			waitingTimes += [float(executeProgram(run, args)[2])]
			queueSizes += [float(executeProgram(run, args)[3])]
			utilization += [float(executeProgram(run, args)[4])]
			failedPackets += [float(executeProgram(run, args)[5])]

	elif (args.runMode == "static"):
		for run in range(1, 11):
			servedPackets += [float(executeProgram(run, args)[0])]
			serviceTimes += [float(executeProgram(run, args)[1])]
			waitingTimes += [float(executeProgram(run, args)[2])]
			queueSizes += [float(executeProgram(run, args)[3])]
			utilization += [float(executeProgram(run, args)[4])]
			failedPackets += [float(executeProgram(run, args)[5])]
	else:
		print ("Wrong runMode, variants: static dynamic")
		exit (1)


	failureProb = [f / (s + f) for (f,s) in zip(failedPackets, servedPackets)] 

	print("{}\t{}\t{}\t{}\t{}\t{}".format(args.lambd / args.mu, args.q_size, np.mean(serviceTimes), confidenceInterval(serviceTimes, args.alpha), 
																	 np.mean(failureProb), confidenceInterval(failureProb, args.alpha)))


if __name__ == "__main__":
	main()
