from display.inky_display import InkyDisplay
from utils.image_utils import resize_image, change_orientation, apply_image_enhancement

class DisplayManager:
    """Manages the display and rendering of images (minimal setup for startup image)."""

    def __init__(self, device_config):
        self.device_config = device_config
        # Only keep InkyDisplay
        self.display = InkyDisplay(device_config)

    def display_image(self, image, image_settings=[]):
        """Render the image on the Inky display."""
        # Save the image locally
        image.save(self.device_config.current_image_file)

        # Apply orientation and resize
        image = change_orientation(image, self.device_config.get_config("orientation"))
        image = resize_image(image, self.device_config.get_resolution(), image_settings)
        if self.device_config.get_config("inverted_image"):
            image = image.rotate(180)
        image = apply_image_enhancement(image, self.device_config.get_config("image_settings"))

        # Pass to InkyDisplay
        self.display.display_image(image, image_settings)
