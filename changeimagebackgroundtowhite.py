import cv2
import numpy as np

def replace_background_with_white(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    cv2.imshow("imageoriginal",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    
    #hsv 
    hsv =cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imshow("hsv",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Apply a binary threshold to get a binary mask
    _, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("mask",mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Invert mask to get the foreground
    mask_inv = cv2.bitwise_not(mask)
    cv2.imshow("mask_inv",mask_inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

    # Create a white background image
    white_background = np.ones_like(image, dtype=np.uint8) * 190
    cv2.imshow("white_background",white_background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Use the mask to extract the foreground from the original image
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)
    cv2.imshow("foreground",foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Combine the foreground with the white background
    combined = cv2.add(foreground, white_background, mask=mask)

    # Save the result
    cv2.imwrite(output_path, combined)
    cv2.imshow("white",combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
path_to_your_image = r'F:\Sarves\Documents\DSC_6042 copyRezise.jpg'
path_to_output_image = r'F:\Full stack data science\Vscode\OpenCV2\imageBackground\DSC_6042white.jpg'
replace_background_with_white(path_to_your_image,path_to_output_image )
