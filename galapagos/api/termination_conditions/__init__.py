from ctypes import *
import os

loader = windll if os.system == 'win32' else cdll
__galapagos_termination_conditions__ = loader.LoadLibrary(r'C:\Users\kosie\github\Galapagos\bin\Debug\SharedTerminationConditions.dll')

#--------------------------
#----Fitness Threshold-----
#--------------------------
__galapagos_termination_conditions__.create_fitness_threshold_metadata.restype = c_void_p
__galapagos_termination_conditions__.delete_fitness_threshold_metadata.argtypes = [c_void_p]

__galapagos_termination_conditions__.set_fitness_threshold_metadata_fitness_threshold.argtypes = [c_void_p, c_size_t]
__galapagos_termination_conditions__.get_fitness_threshold_metadata_fitness_threshold.restype = c_size_t
__galapagos_termination_conditions__.get_fitness_threshold_metadata_fitness_threshold.argtypes = [c_void_p]
