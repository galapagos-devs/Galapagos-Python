from ctypes import *
import os

loader = windll if os.system == 'win32' else cdll
__galapagos_selection_algorithms__ = loader.LoadLibrary(r'C:\Users\kosie\github\Galapagos\bin\Debug\SharedSelectionAlgorithms.dll')

#-----------------------------
#----Tournament Selection-----
#-----------------------------
__galapagos_selection_algorithms__.create_tournament_selection_metadata.restype = c_void_p
__galapagos_selection_algorithms__.delete_tournament_selection_metadata.argtypes = [c_void_p]

__galapagos_selection_algorithms__.set_tournament_selection_metadata_tournament_size.argtypes = [c_void_p, c_size_t]
__galapagos_selection_algorithms__.get_tournament_selection_metadata_tournament_size.restype = c_size_t
__galapagos_selection_algorithms__.get_tournament_selection_metadata_tournament_size.argtypes = [c_void_p]
