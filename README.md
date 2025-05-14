# Retail Shelf Product Detection

## Description

This project demonstrates a basic approach to detecting and outlining products on a retail shelf using computer vision. By employing grayscale conversion, blurring, binary thresholding, and contour detection, the program identifies items on the shelf and marks them with red rectangles. This can assist in simple inventory tracking or monitoring.

## Tools & Libraries

* **Python** – Used for scripting the logic of the detection system.
* **OpenCV** – Handles image preprocessing, contour extraction, and drawing on images.
* **NumPy** – Supports numerical and matrix operations.

## Setup Instructions

### 1. Install Required Libraries

Make sure the necessary packages are installed. You can do this with:

```bash
pip install opencv-python numpy
```

### 2. Prepare Your Image

Place an image file named `reference.jpg` in the same folder as the script. This image should depict a retail shelf containing various items.

### 3. Execute the Script

Run the script with this command:

```bash
python shelf_monitor.py
```

This will open two visual windows:

* One showing the identified products with bounding boxes.
* Another showing the thresholded version of the original image used for contour detection.

### 4. Review Results

* The **Detected Shelf Products** window will display the shelf image with red boxes around each detected item.
* The **Thresholded Image** window will show a black and white image indicating detected object areas based on intensity differences.

## Sample Visuals

![Input Image](reference.jpg)

![Detected Output](output.jpg)
