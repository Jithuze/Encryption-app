# Encryption-app
Encryption utility software | College Mini-Project 


# Encryption Application

## Overview
This Encryption Application is designed to provide various functionalities related to data encryption, decryption, image steganography, and file compression. It utilizes a user-friendly interface built with Flet, allowing users to easily navigate through different features.

## Features

### 1. Encryption and Decryption
- **File Encryption**: Users can encrypt files using AES encryption. The application generates a secure key for encryption and saves the encrypted file.
- **File Decryption**: Users can decrypt previously encrypted files by providing the correct key.

### 2. Image Steganography
- **Hide Text in Image**: Users can hide text data within an image using steganography techniques. The application allows users to select an image and input the text to be hidden.
- **Show Text from Image**: Users can extract hidden text from an image that was previously encoded.

### 3. Image Manipulation
- **Hide Image in Image**: Users can hide one image within another, allowing for covert image storage.
- **Show Image from Image**: Users can reveal the hidden image from a carrier image.

### 4. File Compression
- **Compress Files**: Users can compress files using gzip compression to save space.
- **Compress Images**: Users can compress images while maintaining quality, allowing for efficient storage and sharing.

### 5. Image to PDF Conversion
- **Convert Images to PDF**: Users can select multiple images and convert them into a single PDF document.

### 6. Two-Factor Encryption
- **Two-Factor Encryption**: Users can encrypt files with an additional layer of security by generating a key and encoding it within an image.

## Installation
To run the application, ensure you have Python installed along with the required libraries. You can install the necessary libraries using pip:

---


## Usage
1. **Run the Application**: Start the application by executing the main script.
   ```bash
   python encryptApp/main.py
   ```

2. **Navigate the Interface**: Use the application interface to select the desired functionality (e.g., encrypt, decrypt, hide/show text/images).

3. **Follow Prompts**: The application will guide you through the necessary steps for each functionality, including file selection and input data.

## Example Usage
- To encrypt a file, select the "Encrypt" option, choose the file, and specify the output path.
- To hide text in an image, select the "Hide Text" option, choose the image, and enter the text to hide.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
