from ctypes import cdll, windll
import os

loader = windll if os.system == 'win32' else cdll
__galapagos__ = loader.LoadLibrary(r'C:\Users\asus\github\Galapagos\galapagos.so')
