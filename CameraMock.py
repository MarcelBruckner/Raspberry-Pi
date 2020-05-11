import logging
import time

from ICamera import CameraState, ICamera


class CameraMock(ICamera):
    """
    Wrapper for the picamera.
    """

    def __init__(self, chunk_length: int = 5 * 60):
        """
        Constructor.
        """
        super().__init__(chunk_length)

    def record(self):
        """ Overriding """
        super().record()

        while self.camera_state is CameraState.RECORDING:
            logging.info('Recording')
            time.sleep(1)
