from galapagos.api.selection_algorithms import __galapagos_selection_algorithms__

class TournamentSelectionMetadata:
    def __init__(self):
        self._handle = __galapagos_selection_algorithms__.create_tournament_selection_metadata()

    def __del__(self):
        __galapagos_selection_algorithms__.delete_tournament_selection_metadata(self._handle)

    # tournament size
    @property
    def torunament_size(self) -> int:
        return __galapagos_selection_algorithms__.get_tournament_selection_metadata_tournament_size(self._handle)

    @tournament_size.setter
    def tournament_size(self, value: int) -> None:
        __galapagos_selection_algorithms__.set_tournament_selection_metadata_tournament_size(self._handle, value)
