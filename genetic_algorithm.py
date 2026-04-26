import random
from utils import target_function, decode_chromosome

class GeneticAlgorithm:
    def __init__(self, pop_size, chrom_len, p_c, p_m, bounds):
        self.pop_size = pop_size
        self.chrom_len = chrom_len
        self.p_c = p_c  # Probabilitas Crossover
        self.p_m = p_m  # Probabilitas Mutasi
        self.bounds = bounds
        # Inisialisasi Populasi Acak
        self.population = [[random.randint(0, 1) for _ in range(chrom_len)] 
                           for _ in range(pop_size)]

    def calculate_fitness(self, chromosome):
        """Perhitungan Fitness"""
        x1, x2 = decode_chromosome(chromosome, self.bounds, self.chrom_len // 2)
        # Karena mencari MINIMUM, nilai fitness adalah hasil fungsi itu sendiri
        return target_function(x1, x2)

    def select_parents(self, fitness_scores):
        """Pemilihan Orangtua: Roulette Wheel Selection"""
        offset = max(fitness_scores) + 0.00001
        adj_fitness = [offset - f for f in fitness_scores]
        total_f = sum(adj_fitness)
        
        pick = random.uniform(0, total_f)
        current = 0
        for i, f in enumerate(adj_fitness):
            current += f
            if current > pick:
                return self.population[i]
        return self.population[-1]

    def crossover(self, p1, p2):
        """Pindah Silang: Single Point Crossover"""
        if random.random() < self.p_c:
            point = random.randint(1, self.chrom_len - 1)
            return p1[:point] + p2[point:], p2[:point] + p1[point:]
        return p1[:], p2[:]

    def mutation(self, chromosome):
        """Mutasi: Bit-Flip Mutation """
        new_chrom = chromosome[:]
        for i in range(len(new_chrom)):
            if random.random() < self.p_m:
                new_chrom[i] = 1 - new_chrom[i]
        return new_chrom

    def evolve(self):
        """Pergantian Generasi / Seleksi Survivor"""
        fitness_scores = [self.calculate_fitness(ind) for ind in self.population]
        new_population = []

        # Elitism: Menjaga kromosom terbaik (Seleksi Survivor)
        best_idx = fitness_scores.index(min(fitness_scores))
        new_population.append(self.population[best_idx][:])

        while len(new_population) < self.pop_size:
            p1 = self.select_parents(fitness_scores)
            p2 = self.select_parents(fitness_scores)
            
            c1, c2 = self.crossover(p1, p2)
            new_population.append(self.mutation(c1))
            if len(new_population) < self.pop_size:
                new_population.append(self.mutation(c2))

        self.population = new_population
        return min(fitness_scores), self.population[0]