import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    """Minimal device configuration for displaying startup image."""
    
    def __init__(self):
        self.config_file = os.path.join(BASE_DIR, "device.json")
        self.current_image_file = os.path.join(BASE_DIR, "current_image.png")
        self._config_data = self._load_config()
    
    def _load_config(self):
        """Load configuration from JSON file if exists, else default."""
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                return json.load(f)
        else:
            # Minimal default configuration
            return {
                "resolution": (800, 480),  # default Inky Impression size
                "startup": True
            }

    def get_config(self, key, default=None):
        return self._config_data.get(key, default)

    def get_resolution(self):
        return self.get_config("resolution", (800, 480))

    def write_config(self):
        """Write the current configuration to file (optional for minimal setup)."""
        with open(self.config_file, "w") as f:
            json.dump(self._config_data, f)
