#!/usr/bin/env python3

import os
import random
import logging

from display.display_manager import DisplayManager
from utils.app_utils import generate_startup_image
from config import Config

logger = logging.getLogger(__name__)

# Initialize device configuration and display manager
device_config = Config()
display_manager = DisplayManager(device_config)

if __name__ == '__main__':
    # Always display startup image
    logger.info("Displaying startup image")
    img = generate_startup_image(device_config.get_resolution())
    display_manager.display_image(img)
