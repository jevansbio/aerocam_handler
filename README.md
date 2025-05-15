# Aerocam handler

A python library for reading `.dat` files produced by the Swiss Bird Radar AeroecologyCamera AC1, and turning them into images and animations.

## Installation
```shell
pip install git+https://github.com/jevansbio/aerocam_handler.git
```

## Usage
#### Load a dat file
```python
from aerocam_handler.reader import DatReader

dat_file_path = "foo.dat"

# Create DatReader instance
dat_handler = DatReader()

# Load a file
with open(dat_file_path,'rb') as f:
    dat_handler.open_dat_file(f)
```

#### Produce an image list to work with in python

```python
# Decoded image list, where frames can vary in size
image_list = dat_handler.image_list

# List of images padded to the same size using background color
resized_image_list = dat_handler.get_resized_image_list(color=(0,0,0))
```

#### Save a concatenated image
```python
dat_handler.save_concatenated_image("concatenated_image.jpg")
```
![Combined images](docs/concatenated_image.jpg)
#### Save an animation
```python
dat_handler.save_animation("animation.gif")
```
<img src="docs/animation.gif" height="200">

## Documentation
[More detailed documentation can be found here](html/index.html)

## Potential future features
- Animate along radar track.
- Expose more options to the save functions.

