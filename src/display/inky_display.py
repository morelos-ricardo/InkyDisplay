from inky.auto import auto

class InkyDisplay:
    """Minimal wrapper for Inky display hardware."""

    def __init__(self, device_config):
        # Detect the display automatically
        self.inky = auto()
        self.device_config = device_config

    def display_image(self, image, image_settings=[]):
        """Displays a PIL image on the Inky hardware."""
        self.inky.set_image(image)
        self.inky.show()
