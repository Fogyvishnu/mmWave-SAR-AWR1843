"""
Interface for DCA1000EVM data acquisition module.
Handles communication and data streaming from AWR1843BOOST radar sensor.
"""

import socket
import numpy as np
from typing import Tuple, Optional

class DCA1000Interface:
    """Controls DCA1000 Ethernet Data Capture"""

    def __init__(self, ip_address: str = "192.168.33.180", port: int = 4098):
        """
        Initialize connection to DCA1000EVM.

        Args:
            ip_address: IP of the DCA1000EVM device.
            port: port for data streaming.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = None
        self.connected = False

    def connect(self) -> bool:
        """Establish connection to DCA1000EVM."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.settimeout(5.0)
            # send configuration command to DCA1000EVM
            config_cmd = b'config'
            self.socket.sendto(config_cmd, (self.ip_address, self.port))
            self.connected = True
            print(f"Connected to DCA1000EVM at {self.ip_address}:{self.port}")
            return True
        except Exception as e:
            print(f"Connection Failed: {e}")
            self.connected = False
            return False
        
    def capture_data(self, num_samples: int, num_chirps: int) -> Optional[np.ndarray]:
        """
        Capture Raw ADC data from radar.

        Args:
            num_samples: Number of ADC samples per chirp.
            num_chirps: Number of chirps to capture.

        Returns:
            Complex array of shape (num_chirps, num_samples) or none if failed.
        """
        if not self.connected:
            print("Not connected to DCA1000EVM.")
            return None
        
        total_samples = num_samples * num_chirps * 2 * 2 # I+Q, 2 channels typically
        data = bytearray()

        try:
            print(f"Capturing {num_chirps} chirps...")
            for _ in range(total_samples // 1024 + 1):    # receive in chunks
                chunk, _ = self.socket.recvfrom(4096)
                data.extend(chunk)

            # convert to numpy array
            raw_data = np.frombuffer(data[:total_samples], dtype=np.int16)
            # reshape and convert to complex
            complex_data = raw_data[0::2] + 1j * raw_data[1::2]
            reshaped = complex_data.reshape((num_samples, num_chirps), order='F')

            print("Data capture complete.")
            return reshaped
        
        except socket.timeout:
            print("Data capture timed out.")
            return None
        
    def save_data(self, data: np.ndarray, filename: str):
        """save captured data to file."""

        if data is not None:
            with open(filename, 'wb') as f:
                np.save(f, data)
            print(f"Data saved to {filename}")

    def disconnect(self):
        """close connection"""
        if self.socket:
            self.socket.close()
            self.connected = False
            print("Disconnected from DCA1000EVM.")

if __name__ == "__main__":
    # Example usage
    dca = DCA1000Interface()
    if dca.connect():
        data = dca.capture_data(num_samples=256, num_chirps=100)
        if data is not None:
            dca.save_data(data, "test_capture.npy")
        dca.disconnect()