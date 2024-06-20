import cv2
import numpy as np

def replace_blue_background_with_white(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    cv2.imshow("hsv",hsv)
    

    # Define range for the blue color (you may need to adjust these values)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a mask for the blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("mask",mask)
    cv2.waitKey(0)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel,iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel,iterations=2)

    #mask = cv2.edgePreservingFilter(mask, flags=1, sigma_s=60, sigma_r=0.4)

    #cv2.imshow("edgePreservingFilter mask", mask)
    #cv2.waitKey(0)

    

    cv2.imshow("threshold mask", mask)
    cv2.waitKey(0)

    # Convert mask back to uint8
    mask = np.uint8(mask)


    cv2.imshow("refined mask", mask)

    #Feather the mask edges
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    cv2.imshow("GaussianBlur mask", mask)
    cv2.waitKey(0)

    # Invert the mask to get the non-blue regions
    mask_inv = cv2.bitwise_not(mask)
    cv2.imshow('maskinv',mask_inv)
    cv2.waitKey(0)
    

    # Create a white background image
    white_background = np.ones_like(image, dtype=np.uint8) * 255

    cv2.imshow("white background",white_background)

    

    # Extract the foreground using the inverted mask
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow('foreground',foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Combine the foreground with the white background
    #combined = cv2.add(foreground, white_background, mask=mask)
    combined = cv2.add(foreground, cv2.bitwise_and(white_background, white_background, mask=mask))



    cv2.imshow('Final Image', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite(output_path, combined)

# Example usage
#replace_blue_background_with_white('path_to_your_image.jpg', 'output_image.jpg')
path_to_your_image = r'F:\Sarves\Documents\DSC_6042 copyRezise.jpg'
path_to_output_image = r'F:\Full stack data science\Vscode\OpenCV2\imageBackground\DSC_6042bluewhite.jpg'
replace_blue_background_with_white(path_to_your_image,path_to_output_image )