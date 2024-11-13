from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt(in_file, out_file):
    try:
        key_in = os.urandom(32) # Generate a 256-bit key
        
        chunksize = 64*1024
        outputFile = open(out_file, "wb")
        iv = os.urandom(16)
        encryptor = Cipher(algorithms.AES(key_in), modes.CBC(iv), backend=default_backend()).encryptor()
        outputFile.write(iv)
        
        # Track original file size for padding
        original_size = os.path.getsize(in_file)
        outputFile.write(original_size.to_bytes(8, byteorder='big'))
        
        with open(in_file, 'rb') as infile:
            while True:
                chunk = infile.read(chunksize)
                
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                
                outputFile.write(encryptor.update(chunk))
        
        encrypted_final_chunk = encryptor.finalize()
        outputFile.write(encrypted_final_chunk)
        outputFile.close()
        return key_in
    except Exception as e:
        print("Encryption failed:", e)
        return False

def decrypt(in_file, out_file, key_in):
    try:
        chunksize = 64*1024
        outputFile = open(out_file, "wb")
        
        with open(in_file, 'rb') as infile:
            iv = infile.read(16)
            decryptor = Cipher(algorithms.AES(key_in), modes.CBC(iv), backend=default_backend()).decryptor()
            
            original_size = int.from_bytes(infile.read(8), byteorder='big')
            padding = original_size % 16
            remaining = original_size
            
            while remaining > 0:
                chunk = infile.read(min(chunksize, remaining))
                
                if len(chunk) == 0:
                    break
                
                decrypted_chunk = decryptor.update(chunk)
                if remaining < chunksize:
                    decrypted_chunk = decrypted_chunk[:-padding]
                
                outputFile.write(decrypted_chunk)
                remaining -= len(chunk)
            
            outputFile.close()
            return True
    except Exception as e:
        print("Decryption failed:", e)
        return False

# Example usage
# Encryption
# key_value = encrypt(r'C:\Users\ASUS\Downloads\Telegram Desktop\mini-s6 (2)\mini-s6\cropped_image.jpg', 'encrypted.bin')
# if key_value:
#     print("Encryption successful. Key:", key_value)
# else:
#     print("Encryption failed.")

# Decryption
# key_value = eval(input("Enter Key : "))
# if decrypt('encrypted.bin', 'output.jpeg', key_value):
#     print("Decryption successful.")
# else:
#     print("Decryption failed.")
