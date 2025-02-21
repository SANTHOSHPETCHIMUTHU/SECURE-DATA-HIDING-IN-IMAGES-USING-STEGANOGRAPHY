import cv2

def decrypt_image(image_path, password, original_password, message_length):
    if password != original_password:
        raise ValueError("Incorrect password! Access denied.")
    
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or invalid format.")
    
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0
    
    for _ in range(message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    return message