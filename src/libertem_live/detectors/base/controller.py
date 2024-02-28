class AcquisitionController:
    """
    Base-class for detector-specific settings and control actions.
    """
    def determine_nav_shape(self, nimages: int) -> tuple[int, ...]:
        raise NotImplementedError()
