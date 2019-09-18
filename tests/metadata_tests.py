try:
    from galapagos.api.metadata import PopulationMetadata
except ModuleNotFoundError:
    import sys
    sys.path.append('..')
    from galapagos.api.metadata import PopulationMetadata

def population_metadata_test():
    population_metadata = PopulationMetadata()
    population_metadata.survival_rate = .25
    print(population_metadata.survival_rate)

population_metadata_test()
