from galapagos.api import __galapagos__

class ChromosomeMetadata:
    def __init__(self):
        self._handle = __galapagos__.create_chromosome_metadata()

    def __del__(self):
        __galapagos__.delete_chromosome_metadata(self._handle)

    # name
    @property
    def name(self) -> str:
        return __galapagos__.get_chromosome_metadata_name(self._handle).decode('utf-8')

    @name.setter
    def name(self, value: str) -> None:
        __galapagos__.set_chromosome_metadata_name(self._handle, value.encode('utf-8'))

    # crossover_rate
    @property
    def crossover_rate(self) -> float:
        return __galapagos__.get_chromosome_metadata_crossover_rate(self._handle)

    @crossover_rate.setter
    def crossover_rate(self, value: float) -> None:
        __galapagos__.set_chromosome_metadata_crossover_rate(self._handle, value)

    # mutation_rate
    @property
    def mutation_rate(self) -> float:
        return __galapagos__.get_chromosome_metadata_mutation_rate(self._handle)

    @mutation_rate.setter
    def mutation_rate(self, value: float) -> None
        __galapagos__.set_chromosome_metadata_mutation_rate(self._handle, value)

    # num crossovers
    @property
    def num_crossovers(self) -> int:
        return __galapagos__.get_chromosome_metadata_num_crossovers(self._handle)

    @num_crossovers.setter
    def num_crossovers(self, value: int) -> None:
        __galapagos__.set_chromosome_metadata_num_crossovers(self._handle, value)

    # TODO: Need a better way to get crossover metadata. Raw double pointer is no good.

    # num mutations
    @property
    def num_mutations(self) -> int:
        return __galapagos__.get_chromosome_metadata_num_mutations(self._handle)

    @num_crossovers.setter
    def num_mutations(self, value: int) -> None:
        __galapagos__.set_chromosome_metadata_num_mutations(self._handle, value)

    # TODO: Need a better way to get mutation metadata. Raw double pointer is no good.
