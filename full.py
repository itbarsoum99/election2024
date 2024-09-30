import random
import statistics

baseNationalEnvironment = 2.8 

enthusiasmMax = 3.25 

enthusiasmMin = -2 

historicalAdjustment = 2.2 

pvi = [-15, -8, -2, -16, 13, 4, 7, 7, 43, -3, -3, 14, -18, 7, -11, -6, -10, -16, -12, 2, 9, -6,  14, 15, -1, 1, -11, -10, -11, -13, 0, -1, 1, 6, 3, 10, -3, -20, -6, -20, 6, -2, 8, -8, -16, -14, -5, -13, 16, 3, 8, -22, -2, -25.0]

polling = [0, 0, -1.0, 0, 0, 0, 0, 0, 0, -4.0, -0.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.9, 6.0, 0, 0, 0, 0, 8.6, 1.5, 7.2, 0, 0, 0, 0.1, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.9, 0]

evs = [9, 3, 11, 6, 54, 10, 7, 3, 3, 30, 16, 4, 4, 19, 11, 6, 6, 8, 8, 2, 1, 1, 10, 11, 15, 10, 6, 10, 4, 4, 1, 6, 4, 14, 5, 28, 16, 3, 17, 7, 8, 19, 4, 9, 3, 11, 40, 6, 3, 13, 12, 4, 10, 3]

print(len(pvi))
print(len(polling))
print(len(evs))


def simNatlEnv(baseEnv):
	marginOfError = 0.5 * baseEnv
	errorAdj = random.uniform(-marginOfError, marginOfError)
	enthusiasmAdj = random.uniform(enthusiasmMin, enthusiasmMax)
	historicalAdj = random.uniform(-historicalAdjustment, historicalAdjustment)
	natlEnv = baseNationalEnvironment + errorAdj + enthusiasmAdj + historicalAdj
	return natlEnv

def fundamentals():
	issues = [["economy", 0.38, -7], ["immigration", 0.135, -10], ["healthcare", 0.09, 9],  ["abortion", 0.08, 14], ["climate", 0.08, 12], ["rights", 0.06, 16], ["crime", 0.03, -1], ["guns", 0.03, 5], ["liberties", 0.03, ], ["education", 0.02, 0], ["fopo", 0.045, 4]]
	result = 0
	for x in range(8):
		total = issues[x][1] * issues[x][2]
		result += total
	return (result*100)		 	
	
def election (baseEnvironment):
	nationalEnvironment = simNatlEnv(baseEnvironment)
	fun = fundamentals()
	demEVs = 0
	for x in range(52):
		swingAdj = random.uniform(-6.3, 5.0)
		race = (((pvi[x] + polling[x]*1.2)/2 + (nationalEnvironment*0.8) + swingAdj)*0.84) + (fun * 0.16)
		if race == 0:
			race = random.choice([-1, 1])
			print("coin flipped.")
		if race > 0:
			demEVs += evs[x]

	return demEVs

def simulate(env):
	demWins = 0
	gopWins = 0
	ties = 0
	
	numEVs = []
	
	i = 10000

	for x in range(i):
		result = election(env)
		numEVs.append(result)
		if result >= 270:
			demWins += 1
		elif result == 269:
			ties += 1
		else:
			gopWins += 1
	
	average = int(sum(numEVs)/(i))
	numEVs.sort()
	median = numEVs[int(i/2)]
	min = numEVs[0]
	max = numEVs[i-1]
	mode = statistics.mode(numEVs)

	print("President")
	print("Democrat wins " + str(int((demWins/(i/100)) + 0.5)) + " in 100 times")
	print("Republican wins " + str(int((gopWins/(i/100)) + 0.5)) + " in 100 times")
	print("Average EVs: " + str(average) + "D—" + str(538-average) + "R")
	print("Median: " + str(median) + "D—" + str(538-median) + "R")
	print("Mode: " + str(mode) + "D—" + str(538-mode) + "R")
	print("Minimum: " + str(min) + "D—" + str(538-min) + "R")
	print("Maximum: " + str(max) + "D—" + str(538-max) + "R")		 
		 	


simulate(baseNationalEnvironment)
