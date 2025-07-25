import numpy as np

def create_genome(input_size, hidden_size, output_size):
    genome_size = input_size * hidden_size + hidden_size + hidden_size * output_size + output_size
    genome = np.random.uniform(-1, 1, genome_size)
    return genome
