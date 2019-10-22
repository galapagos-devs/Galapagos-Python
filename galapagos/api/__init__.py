import ctypes
import os

loader = ctypes.windll if os.system == 'win32' else ctypes.cdll
__galapagos__ = loader.LoadLibrary(r'C:\Users\kosie\github\Galapagos\bin\Debug\SharedGalapagos.dll')

fitness_func_t = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_void_p)


class CrossoverMetadata(ctypes.Structure):
    _fields_ = []


class MutationMetadata(ctypes.Structure):
    _fields_ = []


class SelectionAlgorithmMetadata(ctypes.Structure):
    _fields_ = []


class TerminationConditionMetadata(ctypes.Structure):
    _fields_ = []


class ChromosomeMetadata(ctypes.Structure):
    _fields_ = [('name', ctypes.c_char_p),
                ('crossover_rate', ctypes.c_double),
                ('mutation_rate', ctypes.c_double),
                ('num_crossovers', ctypes.c_size_t),
                ('crossover_metadata', ctypes.POINTER(ctypes.POINTER(CrossoverMetadata))),
                ('num_mutations', ctypes.c_size_t),
                ('mutation_metadata', ctypes.POINTER(ctypes.POINTER(MutationMetadata)))]

    def __init__(self, num_crossovers, num_mutations):
        super().__init__()
        crossover_elms = (ctypes.POINTER(CrossoverMetadata) * num_crossovers)()
        mutation_elms = (ctypes.POINTER(MutationMetadata) * num_mutations)()

        self.num_crossovers = num_crossovers
        self.crossover_metadata = ctypes.cast(crossover_elms,ctypes.POINTER(ctypes.POINTER(CrossoverMetadata)))
        self.num_mutations = num_mutations
        self.mutation_metadata = ctypes.cast(crossover_elms, ctypes.POINTER(ctypes.POINTER(MutationMetadata)))


class PopulationMetadata(ctypes.Structure):
    _fields_ = [('size', ctypes.c_size_t),
                ('survival_rate', ctypes.c_double),
                ('distance_threshold', ctypes.c_double),
                ('cooperative_coevolution', ctypes.c_bool),
                ('num_selection_algorithms', ctypes.c_size_t),
                ('selection_algorithm_metadata', ctypes.POINTER(ctypes.POINTER(SelectionAlgorithmMetadata))),
                ('num_termination_conditions', ctypes.c_size_t),
                ('termination_condition_metadata', ctypes.POINTER(ctypes.POINTER(TerminationConditionMetadata))),
                ('fitness_function', fitness_func_t),
                ('num_chromosomes', ctypes.c_size_t),
                ('chromosome_metadata', ctypes.POINTER(ctypes.POINTER(ChromosomeMetadata)))]

    def __init__(self, num_selection_algorithms, num_termination_conditions, num_chromosomes):
        super().__init__()
        selection_algorithm_elms = (ctypes.POINTER(SelectionAlgorithmMetadata) * num_selection_algorithms)()
        termination_condition_elms = (ctypes.POINTER(TerminationConditionMetadata) * num_termination_conditions)()
        chromosome_elms = (ctypes.POINTER(ChromosomeMetadata) * num_chromosomes)()

        self.num_selection_algorithms = num_selection_algorithms
        self.selection_algorithm_metadata = ctypes.cast(selection_algorithm_elms, ctypes.POINTER(ctypes.POINTER(SelectionAlgorithmMetadata)))
        self.num_termination_conditions = num_termination_conditions
        self.termination_condition_metadata = ctypes.cast(termination_condition_elms, ctypes.POINTER(ctypes.POINTER(TerminationConditionMetadata)))
        self.num_chromosomes = num_chromosomes
        self.chromosome_metadata = ctypes.cast(chromosome_elms, ctypes.POINTER(ctypes.POINTER(ChromosomeMetadata)))


# --------------------------
# ----Galapagos Session-----
# --------------------------
__galapagos__.create_population.restype = ctypes.c_void_p
__galapagos__.delete_population.argtypes = [ctypes.c_void_p]
