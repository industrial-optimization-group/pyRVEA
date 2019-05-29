from pyrvea.Problem.evonn_problem import EvoNNProblem
from pyrvea.Population.population_evonn import Population
from pyrvea.Recombination.ppga_crossover import ppga_crossover
from pyrvea.Recombination.ppga_mutation import ppga_mutation
from pyrvea.EAs.PPGA import PPGA
from random import randint, sample
import numpy as np
import timeit

input_nodes = 5
hidden_nodes = 4
num_of_samples = 10
training_data = np.random.uniform(0, 1, size=(num_of_samples, input_nodes))
preferred_output = np.ones(num_of_samples)

prob = EvoNNProblem(
    name="EvoNN",
    training_data_input=training_data,
    training_data_output=preferred_output,
    num_input_nodes=input_nodes,
    num_hidden_nodes=hidden_nodes,
)

arr = np.zeros((60,60))

pop = Population(prob)

p = PPGA(pop)

#a1 = randint(0, 49)
#a2 = randint(0, 49)
#mutation(pop, a1, a2)

#selected = sample(range(1, np.shape(pop.individuals)[0]), randint(1, np.shape(pop.individuals)[0]))
#pop.keep(selected)
#selected = sample(range(1, np.shape(pop.individuals)[0]), randint(1, np.shape(pop.individuals)[0]))
#pop.delete(selected)