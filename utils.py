import math # Digunakan untuk fungsi matematika seperti sin, cos, tan, dan exp

def target_function(x1, x2):
    """Fungsi sesuai yang disoal untuk dicari nilai minimumnya"""

    term1 = math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)
    term2 = 0.5 * math.exp(1- math.sqrt(x2**2))
    return -(term1 + term2)

def decode_chromosome(binary_list, bounds, bits_per_var):
    """Mengubah kromosom biner menjadi nilai variabel nyata"""

    # Pisahkan kromosom menjadi dua bagian (x1 dan x2)
    mid = len(binary_list) // 2
    b1 = binary_list[:mid]
    b2 = binary_list[mid:]

    def bin_to_decimal(binary):
        res = 0
        for bit in binary:
            res = (res << 1) | bit
        return res
    
    precision = (2**bits_per_var) - 1

    # Rumus pemetaan : val = min + (decimal * (mac - min) / (2^bits - 1))
    x1 = bounds[0] + bin_to_decimal(b1) * (bounds[1] - bounds[0]) / precision
    x2 = bounds[0] + bin_to_decimal(b2) * (bounds[1] - bounds[0]) / precision

    return x1, x2