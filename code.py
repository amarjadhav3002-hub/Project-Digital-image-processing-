import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load satellite image
image = cv2.imread("satellite.jpg")

if image is None:
    print("Error: satellite.jpg could not be loaded.")
    exit()

# Create output folder if it does not exist
os.makedirs("output", exist_ok=True)

# This variable stores the latest processed image
processed_image = image.copy()

def display_image():
    cv2.imshow("Original Satellite Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# GRAYSCALE


def grayscale():
    global processed_image

    processed_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    cv2.imshow("Grayscale Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#RESIZE

def resize_image():
    global processed_image

    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))

    processed_image = cv2.resize(
        image,
        (width, height)
    )

    cv2.imshow("Resized Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#CROP

def crop_image():
    global processed_image

    print("\nEnter crop coordinates.")
    print("x = horizontal position")
    print("y = vertical position")

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    # Check coordinates
    height, width = image.shape[:2]

    if x1 < 0 or y1 < 0 or x2 > width or y2 > height:
        print("Error: Coordinates are outside the image.")
        return

    if x1 >= x2 or y1 >= y2:
        print("Error: Invalid crop coordinates.")
        return

    processed_image = image[y1:y2, x1:x2]

    cv2.imshow("Cropped Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#RORATE

def rotate_image():
    global processed_image

    print("\n1. Rotate 90 degrees clockwise")
    print("2. Rotate 90 degrees counter-clockwise")
    print("3. Rotate 180 degrees")

    choice = input("Enter choice: ")

    if choice == "1":
        processed_image = cv2.rotate(
            image,
            cv2.ROTATE_90_CLOCKWISE
        )

    elif choice == "2":
        processed_image = cv2.rotate(
            image,
            cv2.ROTATE_90_COUNTERCLOCKWISE
        )

    elif choice == "3":
        processed_image = cv2.rotate(
            image,
            cv2.ROTATE_180
        )

    else:
        print("Invalid choice.")
        return

    cv2.imshow("Rotated Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#FLIP
def flip_image():
    global processed_image
    print("\n1. Horizontal flip")
    print("2. Vertical flip")
    print("3. Horizontal + Vertical flip")
    choice = input("Enter choice: ")
    if choice == "1":
        processed_image = cv2.flip(image, 1)
    elif choice == "2":
        processed_image = cv2.flip(image, 0)

    elif choice == "3":
        processed_image = cv2.flip(image, -1)
    else:
        print("Invalid choice.")
        return
    cv2.imshow("Flipped Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#PIXEL MODIFY
def modify_pixel():
    global processed_image

    # Make a copy so original image is not changed
    processed_image = image.copy()

    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))

    height, width = image.shape[:2]

    if x < 0 or x >= width or y < 0 or y >= height:
        print("Error: Coordinate is outside the image.")
        return

    print("\nEnter BGR values.")
    print("B = Blue")
    print("G = Green")
    print("R = Red")

    b = int(input("Enter Blue value (0-255): "))
    g = int(input("Enter Green value (0-255): "))
    r = int(input("Enter Red value (0-255): "))

    if not (0 <= b <= 255 and
            0 <= g <= 255 and
            0 <= r <= 255):
        print("Error: Values must be between 0 and 255.")
        return

    processed_image[y, x] = [b, g, r]

    print("Pixel modified successfully.")

    cv2.imshow("Modified Pixel", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#BRIGHTNESS

def brightness():
    global processed_image

    value = int(
        input("Enter brightness value (+ for brighter, - for darker): ")
    )

    processed_image = cv2.convertScaleAbs(
        image,
        alpha=1.0,
        beta=value
    )

    cv2.imshow("Brightness Adjusted", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#CONTRAST

def contrast():
    global processed_image

    alpha = float(
        input("Enter contrast value (example: 1.5): ")
    )

    processed_image = cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=0
    )

    cv2.imshow("Contrast Adjusted", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#HISTOGRAM

def histogram():
    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Calculate histogram
    hist = cv2.calcHist(
        [gray],
        [0],
        None,
        [256],
        [0, 256]
    )

    # Display histogram
    plt.figure()

    plt.plot(hist)

    plt.title("Satellite Image Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Number of Pixels")

    plt.xlim([0, 256])

    plt.show()

#HISTOGRAM EQUILIZATION

def histogram_equalization():
    global processed_image

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    processed_image = cv2.equalizeHist(gray)

    cv2.imshow(
        "Histogram Equalized",
        processed_image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#BLUR FILTERING

def blur_image():
    global processed_image

    print("\n1. Mean Blur")
    print("2. Gaussian Blur")
    print("3. Median Blur")

    choice = input("Enter choice: ")

    if choice == "1":

        processed_image = cv2.blur(
            image,
            (5, 5)
        )

    elif choice == "2":

        processed_image = cv2.GaussianBlur(
            image,
            (5, 5),
            0
        )

    elif choice == "3":

        processed_image = cv2.medianBlur(
            image,
            5
        )

    else:
        print("Invalid choice.")
        return

    cv2.imshow("Blurred Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#EDGE DETECTION

def edge_detection():
    global processed_image

    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Reduce noise
    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Detect edges
    processed_image = cv2.Canny(
        blurred,
        100,
        200
    )

    cv2.imshow(
        "Canny Edge Detection",
        processed_image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# THRESHOLDING


def thresholding():
    global processed_image

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    print("\n1. Normal Binary Threshold")
    print("2. Otsu Threshold")

    choice = input("Enter choice: ")

    if choice == "1":

        value = int(
            input("Enter threshold value (0-255): ")
        )

        _, processed_image = cv2.threshold(
            gray,
            value,
            255,
            cv2.THRESH_BINARY
        )

    elif choice == "2":

        _, processed_image = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

    else:
        print("Invalid choice.")
        return

    cv2.imshow(
        "Thresholded Image",
        processed_image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# SAVE IMAGE
def save_image():
    filename = input(
        "Enter filename (example: result.jpg): "
    )

    path = os.path.join(
        "output",
        filename
    )

    success = cv2.imwrite(
        path,
        processed_image
    )

    if success:
        print("\nImage saved successfully!")
        print("Location:", path)
    else:
        print("Error: Image could not be saved.")

#image info

def image_information():

    height, width = image.shape[:2]

    print("\n===== Image Information =====")
    print("Width:", width)
    print("Height:", height)
    print("Shape:", image.shape)
    print("Total values:", image.size)
    print("Data type:", image.dtype)

#main display
while True:

    print("\n")
    print("==========================================")
    print("     SATELLITE IMAGE PROCESSING")
    print("==========================================")

    print("1. Display Image")
    print("2. Image Information")
    print("3. Grayscale")
    print("4. Resize")
    print("5. Crop")
    print("6. Rotate")
    print("7. Flip")
    print("8. Modify Pixel")
    print("9. Brightness")
    print("10. Contrast")
    print("11. Histogram")
    print("12. Histogram Equalization")
    print("13. Blur / Filtering")
    print("14. Edge Detection")
    print("15. Thresholding")
    print("16. Save Processed Image")
    print("17. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_image()

    elif choice == "2":
        image_information()

    elif choice == "3":
        grayscale()

    elif choice == "4":
        resize_image()

    elif choice == "5":
        crop_image()

    elif choice == "6":
        rotate_image()

    elif choice == "7":
        flip_image()

    elif choice == "8":
        modify_pixel()

    elif choice == "9":
        brightness()

    elif choice == "10":
        contrast()

    elif choice == "11":
        histogram()

    elif choice == "12":
        histogram_equalization()

    elif choice == "13":
        blur_image()

    elif choice == "14":
        edge_detection()

    elif choice == "15":
        thresholding()

    elif choice == "16":
        save_image()

    elif choice == "17":
        print("\nThank you for using the program!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 17.")

