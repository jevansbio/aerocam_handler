
import math
import os
import struct
from io import BufferedReader
from math import ceil

from PIL import Image

from .image_funcs import (get_concat_tile, get_dimensions, get_resize_blank,
                          get_row_col_images)


class DatReader():
    """
    A class to read and process Swiss bird radar aeroecology DAT AeroecologyCam AC1 files.
    """

    def __init__(self):
        """
        Initializes a new instance of the DatReader class.
        """
        self.reset()

    def reset(self):
        """
        Resets the internal state of the DatReader instance.
        """
        self.rofi_all = []
        self.offset = 0
        self.contents = None

    def open_dat_file(self, file_handle: BufferedReader, verbose: bool = False):
        """
        Opens and reads a DAT file.

        Args:
            file_handle (BufferedReader): The file handle of the DAT file to read.
            verbose (bool): If True, prints detailed information during processing.
        """
        self.reset()
        self.contents = file_handle.read()
        self.read_dat_file(verbose)

    def read_and_advance(self, format_str: str, offset: int):
        """
        Reads data from the file contents and advances the offset.

        Args:
            format_str (str): The format string for struct unpacking.
            offset (int): The number of bytes to advance after reading.

        Returns:
            The unpacked data.
        """
        result = struct.unpack_from(format_str, self.contents, self.offset)[0]
        self.offset += offset
        return result

    def read_dat_file(self, file_handle: BufferedReader, verbose: bool = False):
        """
        Reads the contents of a DAT file and processes its image data. 
        This is based on php code originally provided in the Swiss bird radar data manual.

        Args:
            file_handle (BufferedReader): The file handle of the DAT file to read.
            verbose (bool): If True, prints detailed information during processing.
        """

        self.version = self.read_and_advance(">L", 4)
        self.bgwidth = self.read_and_advance(">L", 4)
        self.bgheight = self.read_and_advance(">L", 4)
        self.rofi_count = self.read_and_advance(">L", 4)
        if verbose:
            print("{0},{1},{2},{3}".format(self.version,
                  self.bgwidth, self.bgheight, self.rofi_count))

        for i in range(self.rofi_count):
            if verbose:
                print(i/self.rofi_count)
            rofi = {}
            rofi["height"] = self.read_and_advance(">L", 4)
            rofi["left"] = self.read_and_advance(">L", 4)
            rofi["top"] = self.read_and_advance(">L", 4)
            rofi["width"] = self.read_and_advance(">L", 4)
            rofi["area"] = self.read_and_advance(">L", 4)
            rofirows = self.read_and_advance(">L", 4)
            roficols = self.read_and_advance(">L", 4)

            image = Image.new('RGB', (rofi["width"], rofi["height"]))
            newimdata = []
            for row in range(rofirows):
                for col in range(roficols):
                    b = self.read_and_advance("B", 1)
                    g = self.read_and_advance("B", 1)
                    r = self.read_and_advance("B", 1)
                    rgb = (r, g, b)
                    newimdata.append(rgb)
                self.offset += 1*roficols

            image.putdata(newimdata)
            rofi["image"] = image
            self.rofi_all.append(rofi)

    def check_rofi(self):
        """
        Checks if the DAT file has been loaded.

        Raises:
            ValueError: If the DAT file is not loaded.
        """
        if self.rofi_all is None:
            raise ValueError("DAT file not loaded")

    @property
    def image_list(self):
        """
        Returns the list of images extracted from the DAT file.

        Returns:
            list: A list of PIL.Image objects.
        """
        self.check_rofi()
        return [x['image'] for x in self.rofi_all]

    def get_resized_image_list(self, color: tuple = (0, 0, 0)):
        """
        Returns a list of resized images with a blank background.

        Args:
            color (tuple): The background color as an RGB tuple.

        Returns:
            list: A list of resized PIL.Image objects.
        """
        self.check_rofi()
        return get_resize_blank(self.image_list, color)

    def get_concatenated_image(self, color: tuple = (0, 0, 0)):
        """
        Creates a concatenated image from the resized image list.

        Args:
            color (tuple): The background color as an RGB tuple.

        Returns:
            PIL.Image: The concatenated image.
        """
        new_image_list = self.get_resized_image_list(color)
        dims = [get_dimensions(len(new_image_list)),
                get_dimensions(len(new_image_list)+1),
                (ceil(len(new_image_list)**0.5), ceil(len(new_image_list)**0.5))]
        dims = [x for x in dims if not any([y == 1 for y in x])]
        dims = [x for x in dims if x[0]/x[1] >= 0.1]
        dim_prods = [math.prod(x)-len(new_image_list) for x in dims]
        dims = [dims[i]
                for i in range(len(dims)) if dim_prods[i] == min(dim_prods)][0]

        conccat_image_list = get_row_col_images(
            new_image_list, max_col=max(dims))
        concat_image = get_concat_tile(conccat_image_list)

        if any(x > 65535 for x in concat_image.size):
            concat_image.thumbnail((65535, 65535), Image.ANTIALIAS)

        return concat_image

    def save_concatenated_image(self, file_path: str, color: tuple = (0, 0, 0)):
        """
        Saves the concatenated image to a file.

        Args:
            file_path (str): The path to save the image file.
            color (tuple): The background color as an RGB tuple.
        """
        concat_image = self.get_concatenated_image(color)
        concat_image.save(file_path)

    def save_animation(self, file_path: str, color: tuple = (0, 0, 0)):
        """
        Saves an animation of the images to a file.

        Args:
            file_path (str): The path to save the animation file.
            color (tuple): The background color as an RGB tuple.
        """
        new_image_list = self.get_resized_image_list(color)
        new_image_list[0].save(file_path, save_all=True,
                               append_images=new_image_list[1:], loop=0)
