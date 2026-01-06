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
    