from genetic_algorithm import GeneticAlgorithm
from utils import decode_chromosome

def main():
    pop_size = 50
    bits_per_var = 15
    chrom_len = bits_per_var * 2
    p_crossover = 0.8
    p_mutation = 0.1
    domain = [-10, 10]
    max_generation = 100

    ga = GeneticAlgorithm(pop_size, chrom_len, p_crossover, p_mutation, domain)

    print("Mulai evolusi...")
    print("_" * 30)

    best_overall_score = float('inf')
    best_overall_chromosome = None

    # Loop Evolusi
    for gen in range(max_generation):
        best_score, top_chromosome = ga.evolve()

        if best_score < best_overall_score:
            best_overall_score = best_score
            best_overall_chromosome = top_chromosome

        if gen % 10 == 0:
            print(f"Generasi {gen}: Fitness Terbaik = {best_score:.6f}")

    # output program
    final_x1, final_x2 = decode_chromosome(best_overall_chromosome, domain, bits_per_var)

    print("_" * 30)
    print("Hasil akhir")
    print(f"Kromosom terbaik : {best_overall_chromosome}")
    print(f"Nilai x1         : {final_x1:.6f}")
    print(f"Nilai x2         : {final_x2:.6f}")
    print(f"Nilai Minimum f  : {best_overall_score:.6f}")
    
if __name__ == "__main__":
    main()