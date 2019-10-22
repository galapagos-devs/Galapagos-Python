import ctypes
from galapagos.api import __galapagos__
from galapagos.api import PopulationMetadata
from galapagos.api import ChromosomeMetadata


def population_metadata_test():
    population_metadata = PopulationMetadata(0, 0, 2)

    population_metadata.survival_rate = .25
    print(population_metadata.survival_rate)

    chromosome_metadata0 = ChromosomeMetadata(0, 0)
    chromosome_metadata1 = ChromosomeMetadata(0, 0)
    population_metadata.chromosome_metadata[0] = ctypes.pointer(chromosome_metadata0)
    population_metadata.chromosome_metadata[1] = ctypes.pointer(chromosome_metadata1)

    name0 = 'x'
    population_metadata.chromosome_metadata[0].contents.name = name0.encode('utf-8')
    print(population_metadata.chromosome_metadata[0].contents.name.decode('utf-8'))

    name1 = 'y'
    population_metadata.chromosome_metadata[1].contents.name = name1.encode('utf-8')
    print(population_metadata.chromosome_metadata[1].contents.name.decode('utf-8'))

    population = __galapagos__.create_population(population_metadata)
    __galapagos__.delete_population(population)


def chromosome_metadata_test():
    chromosome_metadata = ChromosomeMetadata(0, 0)

    name = 'test'
    chromosome_metadata.name = name.encode('utf-8')
    print(chromosome_metadata.name.decode('utf-8'))


population_metadata_test()
#chromosome_metadata_test()
