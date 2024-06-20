import cv2
import numpy as np

def replace_background_with_white(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for the background color (adjust this range as needed)
    lower_bg = np.array([0, 0, 0])
    upper_bg = np.array([180, 255, 255])

    # Create a mask for the background
    mask = cv2.inRange(hsv, lower_bg, upper_bg)
    
    # Invert the mask to get the foreground
    mask_inv = cv2.bitwise_not(mask)

    # Create a white background image
    white_background = np.ones_like(image, dtype=np.uint8) * 255

    # Use the mask to extract the foreground from the original image
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    # Combine the foreground with the white background
    combined = cv2.add(foreground, white_background, mask=mask)

    # Save the result
    cv2.imwrite(output_path, combined)

    cv2.imshow("white",combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
#replace_background_with_white('path_to_your_image.jpg', 'output_image.jpg')
path_to_your_image = r'F:\Sarves\Documents\DSC_6042 copyRezise.jpg'
path_to_output_image = r'F:\Sarves\Documents\Documents_submission_Employment\DSC_6042white.jpg'
replace_background_with_white(path_to_your_image,path_to_output_image )