from PIL import Image, ImageDraw, ImageFont

def generate_startup_image(resolution):
    """
    Generates the startup image to be displayed on the Inky display.

    Args:
        resolution (tuple): Width and height for the image.

    Returns:
        PIL.Image: Generated startup image.
    """
    width, height = resolution
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    # Example startup text
    text = "InkyPi is starting..."
    font = ImageFont.load_default()

    # Center the text
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, fill="black", font=font)

    return img
