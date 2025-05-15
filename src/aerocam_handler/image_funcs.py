from math import sqrt
from typing import List, Optional, Tuple

from PIL import Image


def get_dimensions(n: int) -> Tuple[int, int]:
    """
    Calculate the dimensions (width, height) for a given number `n` such that the area is close to a square.

    Args:
        n (int): The number to calculate dimensions for.

    Returns:
        Tuple[int, int]: A tuple containing width and height.
    """
    divisors = []
    for current_divisor in range(n):
        if n % float(current_divisor + 1) == 0:
            divisors.append(current_divisor + 1)
    h_index = min(range(len(divisors)),
                  key=lambda i: abs(divisors[i] - sqrt(n)))

    if divisors[h_index] * divisors[h_index] == n:
        return divisors[h_index], divisors[h_index]
    else:
        w_index = h_index + 1
        return divisors[h_index], divisors[w_index]


def get_concat_h_multi_resize(image_list: List[Image.Image], resample: int = Image.BICUBIC) -> Image.Image:
    """
    Concatenate a list of images horizontally, resizing them to the same height.

    Args:
        image_list (List[Image.Image]): List of images to concatenate.
        resample (int): Resampling filter to use for resizing.

    Returns:
        Image.Image: The concatenated image.
    """
    min_height = min(image.height for image in image_list)
    im_list_resize = [image.resize((int(image.width * min_height / image.height), min_height), resample=resample)
                      for image in image_list]

    total_width = sum(image.width for image in im_list_resize)
    composite_image = Image.new('RGB', (total_width, min_height))
    pos_x = 0
    for image in im_list_resize:
        composite_image.paste(image, (pos_x, 0))
        pos_x += image.width
    return composite_image


def get_concat_h_blank(image1: Image.Image, image2: Image.Image,
                       color: Tuple[int, int, int] = (0, 0, 0)) -> Image.Image:
    """
    Concatenate two images horizontally with a blank background.

    Args:
        image1 (Image.Image): The first image.
        image2 (Image.Image): The second image.
        color (Tuple[int, int, int]): Background color.

    Returns:
        Image.Image: The concatenated image.
    """
    composite_image = Image.new('RGB', (image1.width + image2.width,
                                        max(image1.height, image2.height)), color)
    composite_image.paste(image1, (0, 0))
    composite_image.paste(image2, (image1.width, 0))
    return composite_image


def get_concat_v_blank(image1: Image.Image,
                       image2: Image.Image,
                       color: Tuple[int, int, int] = (0, 0, 0)) -> Image.Image:
    """
    Concatenate two images vertically with a blank background.

    Args:
        image1 (Image.Image): The first image.
        image2 (Image.Image): The second image.
        color (Tuple[int, int, int]): Background color.

    Returns:
        Image.Image: The concatenated image.
    """
    dst = Image.new('RGB', (max(image1.width, image2.width),
                            image1.height + image2.height), color)
    dst.paste(image1, (0, 0))
    dst.paste(image2, (0, image1.height))
    return dst


def get_concat_h_multi_blank(image_list: List[Image.Image]) -> Image.Image:
    """
    Concatenate a list of images horizontally with blank space between them.

    Args:
        image_list (List[Image.Image]): List of images to concatenate.

    Returns:
        Image.Image: The concatenated image.
    """
    first_image = image_list.pop(0)
    for image in image_list:
        first_image = get_concat_h_blank(first_image, image)
    return first_image


def get_concat_v_multi_blank(image_list: List[Image.Image]) -> Image.Image:
    """
    Concatenate a list of images vertically with blank space between them.

    Args:
        image_list (List[Image.Image]): List of images to concatenate.

    Returns:
        Image.Image: The concatenated image.
    """
    first_image = image_list.pop(0)
    for image in image_list:
        first_image = get_concat_v_blank(first_image, image)
    return first_image


def get_resize_blank(image_list: List[Image.Image], color: Tuple[int, int, int] = (0, 0, 0)) -> List[Image.Image]:
    """
    Resize images to the same dimensions by adding blank space.

    Args:
        image_list (List[Image.Image]): List of images to resize.
        color (Tuple[int, int, int]): Background color.

    Returns:
        List[Image.Image]: List of resized images.
    """
    all_width = [image.width for image in image_list]
    all_height = [image.height for image in image_list]
    new_image_list = []
    for i in range(len(image_list)):
        dst = Image.new('RGB', (max(all_width), max(all_height)), color)
        dst.paste(image_list[i], (0, 0))
        new_image_list.append(dst)
    return new_image_list


def get_row_col_images(image_list: List[Image.Image],
                       max_width: Optional[int] = None,
                       max_col: Optional[int] = None) -> List[List[Image.Image]]:
    """
    Arrange images into rows and columns based on maximum width and column count.

    Args:
        image_list (List[Image.Image]): List of images to arrange.
        max_width (Optional[int]): Maximum width of a row.
        max_col (Optional[int]): Maximum number of columns.

    Returns:
        List[List[Image.Image]]: A 2D list of images arranged in rows and columns.
    """
    if max_col is None:
        max_col = len(image_list)
    if max_width is None:
        max_width = sum([x.size[0] for x in image_list])

    index = 0
    curr_size = 0
    all_rows = []
    curr_row = []
    for i in range(len(image_list)):
        if ((curr_size + image_list[i].size[0]) > max_width) or ((index + 1) > max_col):
            all_rows.append(curr_row)
            curr_row = []
            curr_size = 0
            index = 0
        curr_row.append(image_list[i])
        curr_size += image_list[i].size[0]
        index += 1
    all_rows.append(curr_row)
    return all_rows


def get_concat_tile(im_list_2d: List[List[Image.Image]]) -> Image.Image:
    """
    Concatenate a 2D list of images into a single tiled image.

    Args:
        im_list_2d (List[List[Image.Image]]): 2D list of images to concatenate.

    Returns:
        Image.Image: The concatenated tiled image.
    """
    im_list_v = [get_concat_h_multi_resize(
        im_list_h) for im_list_h in im_list_2d]
    return get_concat_v_multi_blank(im_list_v)
    im_list_v = [get_concat_h_multi_resize(
        im_list_h) for im_list_h in im_list_2d]
    return get_concat_v_multi_blank(im_list_v)
