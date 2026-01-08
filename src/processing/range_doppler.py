"""
Range-Doppler algorithm for SAR processing.
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from typing import Dict, Any, Tuple

class RangeDopplerSAR:
    """Implements Range-Doppler processing for SAR algorithm."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize SAR processor with configuration
        
        Args:
            config: Dictionary containing SAR processing parameters.
        """

        self.config = config
        self.c = 3e8  # Speed of light in [m/s]

    def range_compression(self, raw_data: np.ndarray) -> np.ndarray:
        """
        Perform range compression (FFT along fast-time)
        
        Args:
            raw_data: complex 2D raw data of shape (num_samples, num_chirps)

        Returns:
            Range compressed data(profiles) of shape (num_samples, num_chirps)
        """
        # Apply windowing(Hamming) to reduce sidelobes
        window = np.hamming(raw_data.shape[0])
        windowed_data = raw_data * window[:, np.newaxis]

        # FFT along range dimension (axis=0)
        range_profiles = np.fft.fft(windowed_data, axis=0)
        range_profiles = np.fft.fftshift(range_profiles, axes=0)

        return range_profiles
        