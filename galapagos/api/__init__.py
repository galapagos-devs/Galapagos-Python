from ctypes import *
import os

loader = windll if os.system == 'win32' else cdll
__galapagos__ = loader.LoadLibrary(r'C:\Users\kosie\github\Galapagos\Build\Debug\Galapagos.dll')

__galapagos__.create_population_metadata.restype = c_void_p

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
