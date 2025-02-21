import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_image
from decrypt import decrypt_image

def select_image_encrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    encrypt_image_path.set(file_path)

def select_image_decrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    decrypt_image_path.set(file_path)

def encrypt_action():
    image_path = encrypt_image_path.get()
    message = message_input.get("1.0", tk.END).strip()
    password = password_input.get()
    if not image_path or not message or not password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    encrypted_image = encrypt_image(image_path, message, password)
    messagebox.showinfo("Success", f"Image encrypted successfully! Saved as {encrypted_image}")

def decrypt_action():
    image_path = decrypt_image_path.get()
    password = decrypt_password_input.get()
    if not image_path or not password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        decrypted_message = decrypt_image(image_path, password, password_input.get(), len(message_input.get("1.0", tk.END).strip()))
        decrypt_output.config(state=tk.NORMAL)
        decrypt_output.delete("1.0", tk.END)
        decrypt_output.insert(tk.END, decrypted_message)
        decrypt_output.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Image Steganography")
root.geometry("700x500")
root.configure(bg="white")

encrypt_frame = tk.Frame(root, bg="#f5f5f5", padx=10, pady=10)
encrypt_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=20)

decrypt_frame = tk.Frame(root, bg="#f5f5f5", padx=10, pady=10)
decrypt_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=20)

# Encryption Section
tk.Label(encrypt_frame, text="Text Encryption", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(anchor="w")
tk.Label(encrypt_frame, text="Enter any text to be Encrypted", bg="#f5f5f5").pack(anchor="w")
message_input = tk.Text(encrypt_frame, height=5, width=40, bd=2, relief="solid")
message_input.pack(pady=5)  # Added spacing

tk.Label(encrypt_frame, text="Enter Secret Key", bg="#f5f5f5").pack(anchor="w", pady=(5, 0))
password_input = tk.Entry(encrypt_frame, show="*", bd=2, relief="solid")
password_input.pack(pady=5)

encrypt_image_path = tk.StringVar()
tk.Button(encrypt_frame, text="Select Image", command=select_image_encrypt).pack(pady=5)
tk.Button(encrypt_frame, text="Encrypt", command=encrypt_action, bg="black", fg="white").pack(pady=10)

tk.Label(encrypt_frame, text="", bg="#f5f5f5").pack(pady=5)  # Spacer
tk.Label(encrypt_frame, text="Encrypted Output", bg="#f5f5f5").pack(anchor="w", pady=5)

# Decryption Section
tk.Label(decrypt_frame, text="Text Decryption", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(anchor="w")
tk.Label(decrypt_frame, text="Enter Secret Key", bg="#f5f5f5").pack(anchor="w", pady=(5, 0))
decrypt_password_input = tk.Entry(decrypt_frame, show="*", bd=2, relief="solid")
decrypt_password_input.pack(pady=5)

decrypt_image_path = tk.StringVar()
tk.Button(decrypt_frame, text="Select Image", command=select_image_decrypt).pack(pady=5)
tk.Button(decrypt_frame, text="Decrypt", command=decrypt_action, bg="black", fg="white").pack(pady=10)

decrypt_output = tk.Text(decrypt_frame, height=5, width=40, bd=2, relief="solid", state=tk.DISABLED)
decrypt_output.pack(pady=5)

root.mainloop()
