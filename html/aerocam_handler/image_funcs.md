Module aerocam_handler.image_funcs
==================================

Functions
---------

`get_concat_h_blank(image1: PIL.Image.Image, image2: PIL.Image.Image, color: Tuple[int, int, int] = (0, 0, 0)) ‑> PIL.Image.Image`
:   Concatenate two images horizontally with a blank background.
    
    Args:
        image1 (Image.Image): The first image.
        image2 (Image.Image): The second image.
        color (Tuple[int, int, int]): Background color.
    
    Returns:
        Image.Image: The concatenated image.

`get_concat_h_multi_blank(image_list: List[PIL.Image.Image]) ‑> PIL.Image.Image`
:   Concatenate a list of images horizontally with blank space between them.
    
    Args:
        image_list (List[Image.Image]): List of images to concatenate.
    
    Returns:
        Image.Image: The concatenated image.

`get_concat_h_multi_resize(image_list: List[PIL.Image.Image], resample: int = 3) ‑> PIL.Image.Image`
:   Concatenate a list of images horizontally, resizing them to the same height.
    
    Args:
        image_list (List[Image.Image]): List of images to concatenate.
        resample (int): Resampling filter to use for resizing.
    
    Returns:
        Image.Image: The concatenated image.

`get_concat_tile(im_list_2d: List[List[PIL.Image.Image]]) ‑> PIL.Image.Image`
:   Concatenate a 2D list of images into a single tiled image.
    
    Args:
        im_list_2d (List[List[Image.Image]]): 2D list of images to concatenate.
    
    Returns:
        Image.Image: The concatenated tiled image.

`get_concat_v_blank(image1: PIL.Image.Image, image2: PIL.Image.Image, color: Tuple[int, int, int] = (0, 0, 0)) ‑> PIL.Image.Image`
:   Concatenate two images vertically with a blank background.
    
    Args:
        image1 (Image.Image): The first image.
        image2 (Image.Image): The second image.
        color (Tuple[int, int, int]): Background color.
    
    Returns:
        Image.Image: The concatenated image.

`get_concat_v_multi_blank(image_list: List[PIL.Image.Image]) ‑> PIL.Image.Image`
:   Concatenate a list of images vertically with blank space between them.
    
    Args:
        image_list (List[Image.Image]): List of images to concatenate.
    
    Returns:
        Image.Image: The concatenated image.

`get_dimensions(n: int) ‑> Tuple[int, int]`
:   Calculate the dimensions (width, height) for a given number `n` such that the area is close to a square.
    
    Args:
        n (int): The number to calculate dimensions for.
    
    Returns:
        Tuple[int, int]: A tuple containing width and height.

`get_resize_blank(image_list: List[PIL.Image.Image], color: Tuple[int, int, int] = (0, 0, 0)) ‑> List[PIL.Image.Image]`
:   Resize images to the same dimensions by adding blank space.
    
    Args:
        image_list (List[Image.Image]): List of images to resize.
        color (Tuple[int, int, int]): Background color.
    
    Returns:
        List[Image.Image]: List of resized images.

`get_row_col_images(image_list: List[PIL.Image.Image], max_width: int | None = None, max_col: int | None = None) ‑> List[List[PIL.Image.Image]]`
:   Arrange images into rows and columns based on maximum width and column count.
    
    Args:
        image_list (List[Image.Image]): List of images to arrange.
        max_width (Optional[int]): Maximum width of a row.
        max_col (Optional[int]): Maximum number of columns.
    
    Returns:
        List[List[Image.Image]]: A 2D list of images arranged in rows and columns.