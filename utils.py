import math

def target_function(x1, x2):
    """Fungsi objektif"""
    term1 = math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)
    term2 = 0.5 * math.exp(1 - math.sqrt(x2**2))
    return -(term1 + term2)

def decode_chromosome(chromosome, bounds, bits_per_var):
    """Proses Dekode Kromosom: Biner -> Desimal"""
    mid = len(chromosome) // 2
    b1 = chromosome[:mid]
    b2 = chromosome[mid:]

    def bin_to_decimal(binary):
        res = 0
        for bit in binary:
            res = (res << 1) | bit
        return res
    
    precision = (2**bits_per_var) - 1
    # Rumus pemetaan biner
    x1 = bounds[0] + bin_to_decimal(b1) * (bounds[1] - bounds[0]) / precision
    x2 = bounds[0] + bin_to_decimal(b2) * (bounds[1] - bounds[0]) / precision
    
    return x1, x2