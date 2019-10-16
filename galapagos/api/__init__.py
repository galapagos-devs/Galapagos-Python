from ctypes import *
import os

loader = windll if os.system == 'win32' else cdll
__galapagos__ = loader.LoadLibrary(r'C:\Users\kosie\github\Galapagos\bin\Debug\SharedGalapagos.dll')

#--------------------------
#----Galapagos Session-----
#--------------------------
__galapagos__.create_population.restype = c_void_p
__galapagos__.delete_population.argtypes = [c_void_p]

#----------------------------
#----Chromosome Metadata-----
#----------------------------
__galapagos__.create_chromosome_metadata.restype = c_void_p
__galapagos__.delete_chromosome_metadata.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_name.argtypes = [c_void_p, c_char_p]
__galapagos__.get_chromosome_metadata_name.restype = c_char_p
__galapagos__.get_chromosome_metadata_name.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_crossover_rate.argtypes = [c_void_p, c_double]
__galapagos__.get_chromosome_metadata_crossover_rate.restype = c_double
__galapagos__.get_chromosome_metadata_crossover_rate.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_mutation_rate.argtypes = [c_void_p, c_double]
__galapagos__.get_chromosome_metadata_mutation_rate.restype = c_double
__galapagos__.get_chromosome_metadata_mutation_rate.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_num_crossovers.argtypes = [c_void_p, c_size_t]
__galapagos__.get_chromosome_metadata_num_crossovers.restype = c_size_t
__galapagos__.get_chromosome_metadata_num_crossovers.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_crossovers.argtypes = [c_void_p, c_void_p]
__galapagos__.get_chromosome_metadata_crossovers.restype = c_void_p
__galapagos__.get_chromosome_metadata_crossovers.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_num_mutations.argtypes = [c_void_p, c_size_t]
__galapagos__.get_chromosome_metadata_num_mutations.restype = c_size_t
__galapagos__.get_chromosome_metadata_num_mutations.argtypes = [c_void_p]

__galapagos__.set_chromosome_metadata_mutations.argtypes = [c_void_p, c_void_p]
__galapagos__.get_chromosome_metadata_mutations.restype = c_void_p
__galapagos__.get_chromosome_metadata_mutations.argtypes = [c_void_p]

#----------------------------
#----Population Metadata-----
#----------------------------
fitness_func_t = CFUNCTYPE(c_double, c_void_p)

__galapagos__.create_population_metadata.restype = c_void_p
__galapagos__.delete_population_metadata.argtypes = [c_void_p]

__galapagos__.set_population_metadata_size.argtypes = [c_void_p, c_longlong]
__galapagos__.get_population_metadata_size.restype = c_longlong
__galapagos__.get_population_metadata_size.argtypes = [c_void_p]

__galapagos__.set_population_metadata_survival_rate.argtypes = [c_void_p, c_double]
__galapagos__.get_population_metadata_survival_rate.restype = c_double
__galapagos__.get_population_metadata_survival_rate.argtypes = [c_void_p]

__galapagos__.set_population_metadata_distance_threshold.argtypes = [c_void_p, c_double]
__galapagos__.get_population_metadata_distance_threshold.restype = c_double
__galapagos__.get_population_metadata_distance_threshold.argtypes = [c_void_p]

__galapagos__.set_population_metadata_cooperative_coevolution.argtypes = [c_void_p, c_bool]
__galapagos__.get_population_metadata_cooperative_coevolution.restype = c_bool
__galapagos__.get_population_metadata_cooperative_coevolution.argtypes = [c_void_p]

__galapagos__.set_population_metadata_num_selection_algorithm_metadata.argtypes = [c_void_p, c_longlong]
__galapagos__.get_population_metadata_num_selection_algorithm_metadata.restype = c_longlong
__galapagos__.get_population_metadata_num_selection_algorithm_metadata.argtypes = [c_void_p]

__galapagos__.set_population_metadata_selection_algorithm_metadata.argtypes = [c_void_p, c_void_p]
__galapagos__.get_population_metadata_selection_algorithm_metadata.restype = c_void_p
__galapagos__.get_population_metadata_selection_algorithm_metadata.argtypes = [c_void_p]

__galapagos__.set_population_metadata_num_termination_condition_metadata.argtypes = [c_void_p, c_longlong]
__galapagos__.get_population_metadata_num_termination_condition_metadata.restype = c_longlong
__galapagos__.get_population_metadata_num_termination_condition_metadata = [c_void_p]

__galapagos__.set_population_metadata_termination_condition_metadata.argtypes = [c_void_p, c_void_p]
__galapagos__.get_population_metadata_termination_condition_metadata.restype = c_void_p
__galapagos__.get_population_metadata_termination_condition_metadata.argtypes = [c_void_p]

__galapagos__.set_population_metadata_fitness_function.argtypes = [c_void_p, fitness_func_t]
__galapagos__.get_population_metadata_fitness_function.restype = fitness_func_t
__galapagos__.get_population_metadata_fitness_function.argtypes = [c_void_p]

__galapagos__.set_population_metadata_num_chromosome_metadata.argtypes = [c_void_p, c_longlong]
__galapagos__.get_population_metadata_num_chromosome_metadata.restype = c_longlong
__galapagos__.get_population_metadata_num_chromosome_metadata.argtypes = [c_void_p]

__galapagos__.set_population_metadata_chromosome_metadata.argtypes = [c_void_p, c_void_p]
__galapagos__.get_population_metadata_chromosome_metadata.restype = c_void_p
__galapagos__.get_population_metadata_chromosome_metadata.argtypes =[] c_void_p]
