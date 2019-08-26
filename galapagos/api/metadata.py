from galapagos.api import __galapagos__


class PopulationMetadata:
    def __init__(self):
        self._handle = __galapagos__.create_population_metadata()

    # size
    @property
    def size(self) -> int:
        return __galapagos__.get_population_metadata_size(self._handle)

    @size.setter
    def size(self, value: int) -> None:
        __galapagos__.set_population_metadata_size(self._handle, value)

    # survival_rate
    @property
    def survival_rate(self) -> int:
        return __galapagos__.get_population_metadata_survival_rate(self._handle)

    @survival_rate.setter
    def survival_rate(self, value: int) -> None:
        __galapagos__.set_population_metadata_survival_rate(self._handle, value)