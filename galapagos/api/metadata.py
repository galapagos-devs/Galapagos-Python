from ctypes import *
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

class PopulationMetadata:
    def __init__(self):
        self._handle = __galapagos__.create_population_metadata()

    def __del__(self):
        __galapagos__.delete_population_metadata(self._handle)

    # size
    @property
    def size(self) -> int:
        return __galapagos__.get_population_metadata_size(self._handle)

    @size.setter
    def size(self, value: int) -> None:
        __galapagos__.set_population_metadata_size(self._handle, value)

    # survival_rate
    @property
    def survival_rate(self) -> float:
        return __galapagos__.get_population_metadata_survival_rate(self._handle)

    @survival_rate.setter
    def survival_rate(self, value: float) -> None:
        __galapagos__.set_population_metadata_survival_rate(self._handle, value)

    # distance threshold
    @property
    def distance_threshold(self) -> float:
        return __galapagos__.get_population_metadata_distance_threshold(self._handle)

    @distance_threshold.setter
    def distance_threshold(self, value: float) -> None:
        __galapagos__.set_population_metadata_distance_threshold(self._handle, value)

    # cooperative coevolution
    @property
    def cooperative_coevolution(self) -> bool:
        return __galapagos__.get_population_metadata_cooperative_coevolution(self._handle)

    @cooperative_coevolution.setter
    def cooperative_coevolution(self, value: bool) -> None:
        __galapagos__.set_population_metadata_cooperative_coevolution(self._handle, value)

    # num selection algorithm metadata
    @property
    def num_selection_algorithm_metadata(self) -> int:
        return __galapagos__.get_population_metadata_num_selection_algorithm_metadata(self._handle)

    @num_selection_algorithm_metadata.setter
    def num_selection_algorithm_metadata(self, value: int) -> None:
        __galapagos__.set_population_metadata_num_selection_algorithm_metadata(self._handle, value)

    # TODO: Need a better way to get selection algorithm metadata. Raw double pointer is no good.

    # num termination condition metadata
    @property
    def num_termination_condition_metadata(self) -> int:
        return __galapagos__.get_population_metadata_num_termination_condition_metadata(self._handle)

    @num_termination_condition_metadata.setter
    def num_termination_condition_metadata(self, value: int) -> None:
        __galapagos__.set_population_metadata_num_termination_condition_metadata(self._handle, value)

    # TODO: Need a better way to get termination condition metadata. Raw double pointer is no good.

    # TODO: Need to figure out how to pass funtion between python and c++ for fitness function get/set.

    # num chromosome metadata
    @property
    def num_chromosome_metadata(self) -> int:
        return __galapagos__.get_population_metadata_num_chromosome_metadata(self._handle)

    @num_chromosome_metadata.setter
    def num_chromosome_metadata(self, value: int) -> None:
        __galapagos__.set_population_metadata_num_chromosome_metadata(self._handle, value)

    # TODO: Need a better way to get termination condition metadata. Raw double pointer is no good.
