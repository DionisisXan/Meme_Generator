"""
A module containing the MemeGenerator class definition.

The MemeGenerator class is responsible for creating meme images with quotes.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeGenerator:
    """
    A class to generate meme images with overlayed quotes.

    :param output_dir: The output directory for saving generated meme images
    """

    def __init__(self, output_dir):
        """Initialize the MemeGenerator with an output directory."""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def _resize_image(self, img, width=500):
        """
        Resize the input image, maintaining its aspect ratio.

        :param img: PIL.Image object
        :param width: The target width for the resized image
        :return: Resized PIL.Image object
        """
        try:
            aspect_ratio = width / float(img.width)
            height = int(aspect_ratio * float(img.height))
            return img.resize((width, height))
        except Exception as e:
            print(f"Error resizing image: {e}")
            return img

    def _add_caption(self, img, text, author):
        """
        Add a caption to an image.

        :param img: PIL.Image object
        :param text: Quote body text
        :param author: Quote author
        """
        try:
            draw = ImageDraw.Draw(img)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            font_path = os.path.join(current_dir, 'fonts', 'arial.ttf')
            font = ImageFont.truetype(font_path, size=20)
            text = f"{text} - {author}"

            # Wrap the text
            wrapped_text = textwrap.fill(text, width=40)
            wrapped_text_list = wrapped_text.split('\n')

            # Calculate the total height of the wrapped text
            total_text_height = len(wrapped_text_list) * 20

            # Position the wrapped text
            x = random.randint(0, max(0, img.width - 20 * 40))
            y = random.randint(0, max(0, img.height - total_text_height))

            # Draw the wrapped text line by line
            for line in wrapped_text_list:
                draw.text((x, y), line, font=font, fill=(0, 0, 255))
                y += 20

        except Exception as e:
            print(f"Error adding caption: {e}")

    def make_meme(self, img_path, text, author, width=500):
        """
        Create a meme with the input image, quote text, and author.

        :param img_path: Path to the input image
        :param text: Quote body text
        :param author: Quote author
        :param width: The target width for the resized image
        :return: Path to the generated meme image
        """
        try:
            img = Image.open(img_path)
            img = self._resize_image(img, width)
            self._add_caption(img, text, author)

            # Convert the image to RGB mode, regardless of its current mode
            img = img.convert('RGB')

            output_path = os.path.join(
                self.output_dir, f"meme_{random.randint(0, 100000)}.png")
            img.save(output_path, "PNG")
            return output_path
        except Exception as e:
            print(f"Error generating meme: {e}")
            return None
