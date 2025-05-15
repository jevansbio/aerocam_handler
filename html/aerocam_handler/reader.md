Module aerocam_handler.reader
=============================

Classes
-------

`DatReader()`
:   A class to read and process Swiss bird radar aeroecology DAT AeroecologyCam AC1 files.
    
    Initializes a new instance of the DatReader class.

    ### Instance variables

    `image_list`
    :   Returns the list of images extracted from the DAT file.
        
        Returns:
            list: A list of PIL.Image objects.

    ### Methods

    `check_rofi(self)`
    :   Checks if the DAT file has been loaded.
        
        Raises:
            ValueError: If the DAT file is not loaded.

    `get_concatenated_image(self, color: tuple = (0, 0, 0))`
    :   Creates a concatenated image from the resized image list.
        
        Args:
            color (tuple): The background color as an RGB tuple.
        
        Returns:
            PIL.Image: The concatenated image.

    `get_resized_image_list(self, color: tuple = (0, 0, 0))`
    :   Returns a list of resized images with a blank background.
        
        Args:
            color (tuple): The background color as an RGB tuple.
        
        Returns:
            list: A list of resized PIL.Image objects.

    `open_dat_file(self, file_handle: _io.BufferedReader, verbose: bool = False)`
    :   Opens and reads a DAT file.
        
        Args:
            file_handle (BufferedReader): The file handle of the DAT file to read.
            verbose (bool): If True, prints detailed information during processing.

    `read_and_advance(self, format_str: str, offset: int)`
    :   Reads data from the file contents and advances the offset.
        
        Args:
            format_str (str): The format string for struct unpacking.
            offset (int): The number of bytes to advance after reading.
        
        Returns:
            The unpacked data.

    `read_dat_file(self, file_handle: _io.BufferedReader, verbose: bool = False)`
    :   Reads the contents of a DAT file and processes its image data. 
        This is based on php code originally provided in the Swiss bird radar data manual.
        
        Args:
            file_handle (BufferedReader): The file handle of the DAT file to read.
            verbose (bool): If True, prints detailed information during processing.

    `reset(self)`
    :   Resets the internal state of the DatReader instance.

    `save_animation(self, file_path: str, color: tuple = (0, 0, 0))`
    :   Saves an animation of the images to a file.
        
        Args:
            file_path (str): The path to save the animation file.
            color (tuple): The background color as an RGB tuple.

    `save_concatenated_image(self, file_path: str, color: tuple = (0, 0, 0))`
    :   Saves the concatenated image to a file.
        
        Args:
            file_path (str): The path to save the image file.
            color (tuple): The background color as an RGB tuple.