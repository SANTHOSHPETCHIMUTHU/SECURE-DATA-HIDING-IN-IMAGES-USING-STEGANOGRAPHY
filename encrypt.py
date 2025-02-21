import cv2
import os
import string

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or invalid format.")
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    
    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    # Save encrypted image in the same directory as the script
    encrypted_image_path = os.path.join(os.getcwd(), "encryptedImage.png")
    cv2.imwrite(encrypted_image_path, img)
    
    return encrypted_image_path