# Hybrid images from scratch

Convolution and Gaussian filtering written from first principles in NumPy, then used to build hybrid
images: two pictures combined so that one is visible up close and the other from a distance.

MSc Artificial Intelligence coursework, COMP6223 Computer Vision, University of Southampton,
spring 2026.

## What's here

| File | What it does |
|---|---|
| `MyConvolution.py` | Zero-padded 2D convolution over each colour channel, with the kernel flipped, written with explicit loops rather than a library call |
| `MyHybridImages.py` | Builds the Gaussian kernel from sigma, low-pass filters one image, high-pass filters the other (image minus its blur), and adds them, using `convolve` from `MyConvolution.py` |
| `MyHybridImages.ipynb` | Runs the pipeline on one image pair and shows the result |

The Gaussian kernel size is `8 * sigma + 1`, forced odd, and normalised to sum to 1, so the filter
doesn't change overall brightness.

The hybrid is returned as floating-point values rather than clipped, because the high-pass image has
negative values and the sum can go past 255. It is clipped to 0-255 only when it is displayed.

## The images

The coursework supplied five aligned pairs (cat/dog, bicycle/motorcycle, bird/plane and others) and
asked for one hybrid of your own as well. The notebook runs on the pair I made for that, one photo
with glasses and one without. **No images are included here**, and the notebook's outputs are
cleared. Point the notebook at your own image pair to run it.

## Running it

```bash
pip install -r requirements.txt
jupyter notebook MyHybridImages.ipynb
```

The convolution loops over every pixel in plain Python, so it is slow on large images. Reduce sigma
or use smaller inputs if you want it to finish quickly.

## Note

This is my own coursework code, published with my tutor's confirmation that the code I wrote is mine
to share. The assignment brief and the module's image set are not included.
