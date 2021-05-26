import random

choromosomes=["01101", "01000", "01000", "10011"]

def initializePopulation(choromosomes):
    population=[list(i) for i in choromosomes]
    bitLength=len(population[0])
    populationSize = len(population)

    return population, bitLength, populationSize


def decodingScheme(bitLength):
    positionalValue = [pow(2,i) for i in range(bitLength)]
    positionalValue = positionalValue[::-1]
    return positionalValue

def decode(population, populationSize, decodingScheme, bitLength):
    phenotype = []
    for i in range(populationSize):
        indivisual=population[i]
        phenotype.append(sum([int(indivisual[i]) * decodingScheme[i] for i in range(bitLength)]))
    return phenotype

def computerFitness(phenotype, populationSize, fitness=[]):
    for i in range(populationSize):fitness.append(phenotype[i] * phenotype[i])
    return fitness

def computeFitnessOnFunction(population, populationSize, fitness=[]):
    for i in range(populationSize):
        fitness.append(abs(int(int(population[i][0]) + int(population[i][1]))-
                           int(int(population[i][2]) + int(population[i][3]))+
                           int(int(population[i][4]) + int(population[i][5]))-
                           int(int(population[i][6]) + int(population[i][7]))))

    return fitness

def calculateProbability(fitness, populationSize, probability=[]):
    for i in range(populationSize):
        probability.append(round(fitness[i]/sum(fitness),2))
    return probability

population, bitLength, populationSize = initializePopulation(choromosomes)
print("Population:", population)
print("Bit length:", bitLength)
print("Population size:", populationSize)
positionalValue = decodingScheme(bitLength)
phenotype = decode(population,populationSize,positionalValue,bitLength)
print("Pheno Type:",phenotype)
fitness = computerFitness(phenotype, populationSize)
print("Fitness:",fitness)
