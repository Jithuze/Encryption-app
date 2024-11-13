# Python program to demonstrate 
# image steganography using OpenCV 


import cv2 
import numpy as np 
import random 
from PIL import Image
from rembg import remove
# Encryption function 


def img_encrypt(image, encrypt_image): 
    base_image_path = "encryptOnMobileApp/assets/image.jpeg"  

    try:
        img2 = Image.open(image)

        width = img2.width
        height = img2.height

        img1 = crop_image(base_image_path, random.randint(0,600), random.randint(0,600), width, height) 

        for i in range(height):
            for j in range(width):
                for l in range(3):
                    # Get pixel values from both images
                    pixel1 = img1.getpixel((j, i))
                    pixel2 = img2.getpixel((j, i))

                    # Extract the most significant bits
                    msb1 = pixel1[l] >> 4
                    msb2 = pixel2[l] >> 4

                    # Combining the 4 MSBs
                    combined = (msb1 << 4) | msb2

                    # Update the pixel value in img1
                    pixel1 = list(pixel1)
                    pixel1[l] = combined
                    img1.putpixel((j, i), tuple(pixel1))

        img1.save(encrypt_image)
        return True
    except Exception as e:
        return e
	
# Decryption function 
def img_decrypt(encrypted_image,output_image): 
	
    try:
        # Encrypted image 
        img = cv2.imread(encrypted_image) 
        width = img.shape[0] 
        height = img.shape[1] 

        print(width,height)
        
        # img1 and img2 are two blank images 
        # img1 = np.zeros((width, height, 3), np.uint8)
    
        img2 = np.zeros((width, height, 3), np.uint8) 

        print('loading......')
        for i in range(width): 
            for j in range(height): 
                for l in range(3): 
                    v1 = format(img[i][j][l], '08b') 
                    # v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                    v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                    
                    # Appending data to img1 and img2 
                    # img1[i][j][l]= int(v2, 2) 
                    img2[i][j][l]= int(v3, 2) 
        
        # These are two images produced from 
        # the encrypted image 
        # cv2.imwrite('image1_decrypted.png', img1) 
        cv2.imwrite(output_image, img2) 
        print("worked")
        return True
    except:
        return False
	
def crop_image(image_path, left, top, width, height):
    """
    Crops an image from the top-left corner with the specified coordinates and dimensions.

    Args:
        image_path (str): The path to the image file.
        left (int): The left coordinate of the top-left corner of the crop region.
        top (int): The top coordinate of the top-left corner of the crop region.
        width (int): The desired width of the cropped image in pixels.
        height (int): The desired height of the cropped image in pixels.

    Returns:
        PIL.Image: The cropped image.
    """
    # Open the image
    image = Image.open(image_path)

    # Calculate the right and bottom coordinates for cropping
    right = left + width
    bottom = top + height

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))

    return cropped_image

# # Example usage
# cropped_image = crop_image("image2_decrypted.png", 0, 0, 453 ,600)
# cropped_image.save("image2_decrypted.png")
	
# # Driver's code 
# image1 = input("Enter Image 1 : ")
# image2 = input("Enter Image 2 : ")

# # encrypt(image1,image2) 
# decrypt("/Volumes/Macintosh HD/Users/abijithmadhava/Desktop/untitled.png") 

# print(encrypt("/Volumes/Macintosh HD/Users/abijithmadhava/Desktop/image.png" ,"/Volumes/Macintosh HD/Users/abijithmadhava/Desktop/untitled.png"))


def compress_image(input_image_path, output_image_path, quality): 
    """
    Compresses an image.

    Args:
        input_image_path (str): The path to the input image file.
        output_image_path (str): The path to save the compressed image file.
        quality (int): The quality of compression (0-100), where 0 is the lowest quality and 100 is the highest.

    Returns:
        None
    """
    try:
        # Open the image
        with Image.open(input_image_path) as img:
            # Compress the image
            img.save(output_image_path, quality=int(quality))
        return True
    except Exception as e:
        print(e)
        return e 



def remove_background(input_image_path, output_image_path):
    try:    
        with open(input_image_path, "rb") as f_in:
            with open(output_image_path, "wb") as f_out:
                f_out.write(remove(f_in.read()))
        return True
    except:
        return False