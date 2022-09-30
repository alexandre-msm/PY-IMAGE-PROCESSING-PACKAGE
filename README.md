# py_image_processing

Description.

The package py_image_processing is used to:

	Processing:
	- Histogram matching
	- Structural similarity
	- Resize image

	Utils:
	- Read image
	- Save image
	- Plot image
    - Plot multiple images
	- Plot result
	- Plot histogram

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_processing

```bash
pip install py_image_processing
```

## Usage

```python
from py_image_processing.processing import combine

combine.find_diff_between_images(image1, image2)
combine.hist_transfer(image1, image2)

from py_image_processing.processing import transform

transform.resize_img(image, proportion)

from py_image_processing.utils import image_io

image_io.read_image(path)
image_io.save_image(image, path)

from py_image_processing.utils import plot

plot.plot_image(image)
plot.plot_multi_images(*args)
plot.plot_hist(image)
```

## Author
Alexandre Miranda

## License
[MIT](https://choosealicense.com/licenses/mit/)
