import cv2
import numpy as np

def replace_blue_background_with_white(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range for the blue color (adjust these values as needed)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a mask for the blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply morphological operations to remove small noise and smooth edges
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Use edge-preserving filter on the mask edges
    mask = cv2.edgePreservingFilter(mask, flags=1, sigma_s=60, sigma_r=0.4)

    # Refine the mask by using distance transform and adaptive thresholding
    dist_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    _, mask = cv2.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)

    # Convert mask back to uint8
    mask = np.uint8(mask)

    # Feather the mask edges
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Invert the mask to get the non-blue regions
    mask_inv = cv2.bitwise_not(mask)

    # Create a white background image
    white_background = np.ones_like(image, dtype=np.uint8) * 255

    # Extract the non-blue regions from the original image
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    # Combine the foreground with the white background where the blue regions were
    combined = cv2.add(foreground, cv2.bitwise_and(white_background, white_background, mask=mask))

    # Save the result
    cv2.imwrite(output_path, combined)

    # For visualization: show the original, mask, and final image (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Foreground', foreground)
    cv2.imshow('Final Image', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
#replace_blue_background_with_white('path_to_your_image.jpg', 'output_image.jpg')
path_to_your_image = r'F:\Sarves\Documents\DSC_6042 copyRezise.jpg'
path_to_output_image = r'F:\Full stack data science\Vscode\OpenCV2\imageBackground\DSC_6042bluewhite.jpg'
replace_blue_background_with_white(path_to_your_image,path_to_output_image )
