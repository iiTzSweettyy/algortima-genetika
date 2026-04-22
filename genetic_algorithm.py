import random # Digunakan untuk angka acak buat populasinya
from utils import target_function, decode_chromosome

class GeneticAlgorithm:
    def __init__(self, pop_size, chrom_len, p_c, p_m, bounds):
        self.pop_size = pop_size
        self.chrom_len = chrom_len  # Total bit untuk x1 + x2
        self.p_c = p_c              # Probabilitas crossover
        self.p_m = p_m              # Probabilitas mutasi
        self.bounds = bounds        # [0, 10]
        self.population = self._initialize_population()

    def _initialize_population(self):
        return [[random.randint(0, 1) for _ in range(self.chrom_len)]
                for _ in range(self.pop_size)]
    
    def calculate_fitness(self, chromosome):
        """
        Karena mencari MINIMUM, Di sini kita gunakan pendekatan minimalisasi langsung.
        """
        x1, x2 = decode_chromosome(chromosome, self.bounds, self.chrom_len // 2)
        # menambahkan konstanta kecil agar tidak pembagian dengan nol
        # namum disini kita tidak perlu, karena langsung menggunakan nilai fungsi
        return target_function(x1, x2)
    
    def select_parents(self, fitness_scores):
        """ memilih orang tua menggunakan roullete wheel selection """
        # semakin kecil f(x), semakin besar peluang terpilih
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
    
    def crossover(self, parent1, parent2):
        """ melakukan crossover satu titik """

        if random.random() < self.p_c:
            point = random.randint(1, self.chrom_len - 1)
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
            return child1, child2
        return parent1[:], parent2[:]
    
    def mutation(self, chromosome):
        """ melakukan mutasi dengan probabilitas p_m """

        for i in range(len(chromosome)):
            if random.random() < self.p_m:
                chromosome[i] = 1 - chromosome[i]
        return chromosome
    
    def evolve(self):
        fitness_scores = [self.calculate_fitness(ind) for ind in self.population]
        new_population = []

        # elitism : ambil yang terbaik langsung ke generasi berikutnya
        best_idx = fitness_scores.index(min(fitness_scores))
        new_population.append(self.population[best_idx])

        while len(new_population) < self.pop_size:
            p1 = self.select_parents(fitness_scores)
            p2 = self.select_parents(fitness_scores)

            c1, c2 = self.crossover(p1, p2)
            new_population.append(self.mutation(c1))
            if len(new_population) < self.pop_size:
                new_population.append(self.mutation(c2))

        self.population = new_population
        return min(fitness_scores), self.population[0] # return best fitness dan kromosom terbaik