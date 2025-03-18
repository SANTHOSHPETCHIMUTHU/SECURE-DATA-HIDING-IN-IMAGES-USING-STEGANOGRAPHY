# SECURE-DATA-HIDING-IN-IMAGES-USING-STEGANOGRAPHY
THERE ARE TWO PROJECTS ONE DONE WITH GUI AND ANOTHER WITHOUT GUI
        LOOK FOR stego.py for (without gui)
        LOOK FOR gui.py for (with gui)
        
This project implements **LSB (Least Significant Bit) Steganography** to securely hide text messages inside images using Python. It provides a **GUI** for easy encryption and decryption of messages within images.

## 📜 Features
- Encrypt and hide a secret message inside an image.
- Decrypt and extract the hidden message from the image.
- Password protection for added security.
- GUI-based interface using **Tkinter**.
- Supports **PNG, JPEG, JPG** image formats.

## 🛠️ Requirements
Ensure you have **Python 3.6 or higher** installed.  
Required libraries:
- `opencv-python` (for image processing)
- `tkinter` (for GUI development)
- `os` (for file handling, included in Python)
- `string` (included in Python)

To install missing dependencies, 
    run:pip install opencv-python

📁 Project Folder
│── 📄 encrypt.py         # Encryption logic
│── 📄 decrypt.py         # Decryption logic
│── 📄 gui.py             # GUI implementation using Tkinter
│── 📄 README.md          # Project documentation
│── 🖼️ encryptedImage.png  # Output encrypted image (created after encryption)

🚀 Usage
1️⃣ Run the GUI
    Execute the following command in the terminal:
    python gui.py

2️⃣ Encrypt a Message
    Enter the text message to hide.
    Provide a secret key.
    Select an image file.
    Click "Encrypt" → The encrypted image will be saved in the project folder.
3️⃣ Decrypt a Message
    Provide the correct secret key.
    Select the encrypted image.
    Click "Decrypt" → The hidden message will be displayed.

🖼️ Example
Original Image: input.jpg
Encrypted Image: encryptedImage.png
Hidden Message: "Hello, this is a secret!"

⚠️ Limitations
The encryption method is not highly secure and should not be used for critical data.
Only ASCII characters are supported for hiding messages.
Image modifications after encryption may corrupt the hidden data.

💡 Future Enhancements
Improve encryption with AES-based encoding.
Support more file formats (BMP, TIFF).
Add image quality preservation during encryption.

TO RUN THE PROGRAM:
    *CLICK THE "gui.py" file.
