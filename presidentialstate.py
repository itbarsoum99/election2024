import random
import statistics

baseNationalEnvironment = 3.3

historicalAdjustment = 2.2 

enthusiasmMax = 0
enthusiasmMin = 0

def simNatlEnv(baseEnv):
        marginOfError = 0.5 * baseEnv
        errorAdj = random.uniform(-marginOfError, marginOfError)
        enthusiasmAdj = random.uniform(enthusiasmMin, enthusiasmMax)
        historicalAdj = random.uniform(-historicalAdjustment, historicalAdjustment)
        natlEnv = baseNationalEnvironment + errorAdj + enthusiasmAdj + historicalAdj
        return natlEnv

def election(baseEnvironment, j, k):
	nationalEnvironment = simNatlEnv(baseEnvironment)
	swingAdj = random.uniform(-6.3, 5.0)
	race = j + (1.2*k) + (0.8*nationalEnvironment) + swingAdj
	return race

def simulate(env):
	demWins = 0
	gopWins = 0
	results = []

	i = 10000

	pvi = float(input("PVI: "))
	poll = float(input("Polling average: "))

	for x in range(i):
		result = election(env, pvi, poll)
		results.append(result)
		if result >= 0:
			demWins += 1
		else:
			gopWins += 1
	average = sum(results)/(i)
	results.sort()
	bottom = results[0]
	top = results[i-1]
	firstDecile = results[int(0.1*i)]
	ninthDecile = results[int(i-(0.1*i)-1)]


	print("President -- individual state")
	print("Democrat wins " + str(int((demWins/(i/100)) + 0.5)) + " in 100 times")
	print("Republican wins " + str(int((gopWins/(i/100)) + 0.5)) + " in 100 times")
	print(average)
	print("Best case for Dems: " + str(top))
	print("Best case for GOP: " + str(bottom))
	print("Reasonable range of results: " + str(firstDecile) + " | " + str(ninthDecile))

simulate(baseNationalEnvironment) 
