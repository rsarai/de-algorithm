import random
import copy

from functions import AFunction, Sphere, Rastrigin, Rosenbrocks


class DifferentialEvolution():
	function = AFunction
	floating_scale_factor = False
	scale_factor = 0.5

	def __init__(self, function, type_scale_factor):
		self.function = function
		self.floating_scale_factor = type_scale_factor

		if type_scale_factor:
			self.scale_factor = 0.9

	def differential_evolution(self):
		num_of_individuos = 30
		population = []
		probability_of_recombination = 0.6
		iterations_number = 10000
		best = 0
		best_vector = []

		population = self.initializa_population(num_of_individuos)

		for j in range(0, iterations_number):
			personal_best = []
			for i in range(0, len(population)):
				fitness = self.function.calculate_fitness(population[i])
				experimental_vector = self.create_trial_vector(population, population[i], self.scale_factor)
				new_individuo = self.create_offspring(population[i], experimental_vector, probability_of_recombination)
				new_fitness = self.function.calculate_fitness(new_individuo)
				if new_fitness < fitness:
					personal_best.append(new_individuo)
					best = new_fitness
				else:
					personal_best.append(population[i])
					best = fitness

			if self.floating_scale_factor:
				self.update_parameters()

			population = personal_best
			best_vector.append(best)
			print(best)
		return best_vector

	def update_parameters(self):
		self.scale_factor -= (0.9 - 0.4) / 10000

	def create_offspring(self, individuo, experimental_vector, probability_of_recombination):
		new_individuo = []
		for i in range(0, len(individuo)):
			limiar = random.random()
			if limiar < probability_of_recombination:
				new_individuo.insert(i, experimental_vector[i])
			else:
				new_individuo.insert(i, individuo[i])
		return new_individuo

	def create_trial_vector(self, population, individuo, scale_factor):
		new_pop = copy.deepcopy(population)
		new_pop.remove(individuo)

		destiny = new_pop[random.randint(0, len(new_pop) - 1)]
		new_pop.remove(destiny)

		vect1 = new_pop[random.randint(0, len(new_pop) - 1)]
		new_pop.remove(vect1)

		vect2 = new_pop[random.randint(0, len(new_pop) - 1)]
		new_pop.remove(vect2)

		u = []
		for i in range(0, len(destiny)):
			u.append(destiny[i] + scale_factor * (vect1[i] - vect2[i]))

		return u

	def initializa_population(self, num_of_individuos):
		dimensions = 30
		lower_bound = -100
		upper_bound = 100
		population = []

		for j in range(0, num_of_individuos):
			x1 = []
			for i in range(0, dimensions):
				x1.append(lower_bound + random.random() * (upper_bound - lower_bound))
			population.insert(0, x1)

		return population


def main():
	d = DifferentialEvolution(Rastrigin(), True)
	d.differential_evolution()


main()
