from genetic_algorithm import GeneticAlgorithm
from utils import decode_chromosome

def main():
    # Analisis & Desain Parameter
    pop_size = 40          # Ukuran Populasi
    bits_per_var = 15      # Rancangan Kromosom (15 bit x 2 variabel)
    chrom_len = bits_per_var * 2
    p_crossover = 0.8      # Probabilitas Pc
    p_mutation = 0.1       # Probabilitas Pm
    domain = [-10, 10]     # Batas nilai x1 dan x2
    max_generation = 100   # Kriteria penghentian evolusi

    # Inisialisasi GA
    ga = GeneticAlgorithm(pop_size, chrom_len, p_crossover, p_mutation, domain)

    print("=== PROGRAM ALGORITMA GENETIKA ===")
    print(f"Mencari nilai minimum f(x1, x2) pada domain {domain}")
    print("-" * 45)

    best_overall_score = float('inf')
    best_overall_chrom = None

    # Loop Evolusi
    for gen in range(max_generation):
        best_gen_score, top_gen_chrom = ga.evolve()

        if best_gen_score < best_overall_score:
            best_overall_score = best_gen_score
            best_overall_chrom = top_gen_chrom
            print(f"Gen {gen:3}: Fitness Terbaik = {best_overall_score:.6f}")

    # Output Program
    final_x1, final_x2 = decode_chromosome(best_overall_chrom, domain, bits_per_var)
    
    print("-" * 45)
    print("HASIL AKHIR PENYELESAIAN")
    print(f"Kromosom Terbaik : {''.join(map(str, best_overall_chrom))}")
    print(f"Nilai x1         : {final_x1:.6f}")
    print(f"Nilai x2         : {final_x2:.6f}")
    print(f"Nilai Minimum f  : {best_overall_score:.6f}")

if __name__ == "__main__":
    main()