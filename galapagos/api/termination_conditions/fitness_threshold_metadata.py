from galapagos.api.termination_conditions import __galapagos_termination_conditions__

class FitnessThresholdMetadata:
    def __init__(self):
        self._handle = __galapagos_termination_conditions__.create_fitness_threshold_metadata()

    def __del__(self):
        __galapagos_termination_conditions__.delete_fitness_threshold_metadata(self._handle)

    # fitness threshold
    @property
    def fitness_threshold(self) -> int:
        return __galapagos_termination_conditions__.set_fitness_threshold_metadata_fitness_threshold(self._handle)

    @fitness_threshold.setter
    def tournament_size(self, value: int) -> None:
        __galapagos_termination_conditions__.get_fitness_threshold_metadata_fitness_threshold(self._handle, value)
