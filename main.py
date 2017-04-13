from functions import Sphere
from de import DifferentialEvolution


def main():
	d = DifferentialEvolution(Sphere(), True)
	d.differential_evolution()


main()
