# PRODIGY_CS_03
# Pixel Manipulation For Image Encryption

This project is a simple Python tool that uses a key to encrypt and decrypt images. It modifies the pixel values of an image based on a pseudo-random sequence generated from the key, allowing the image to be encrypted. The same key can be used to decrypt the image back to its original form.

## Features

- **Encryption**: Encrypts an image by manipulating its RGB pixel values based on a random sequence generated from a user-provided key.
- **Decryption**: Decrypts the image by reversing the encryption process using the same key.
- **Key-based Security**: The key ensures that only someone with the correct key can decrypt the image.

## How It Works

1. **Encryption**:
   - The image is opened, and its pixel values are modified by adding random values (generated using the key) to each RGB channel.
   - The encrypted image is saved as a new file with `_encrypted` appended to its name.

2. **Decryption**:
   - The encrypted image is opened, and the same random values (generated using the key) are subtracted from each RGB channel to restore the original image.
   - The decrypted image is saved as a new file with `_decrypted` appended to its name.

## Prerequisites

- Python 3.x
- [Pillow (PIL)](https://pillow.readthedocs.io/) library for image manipulation

To install Pillow, use the following command:

```bash
pip install pillow
```
# How to Use
1. Clone this repository:
```bash
git clone <repository_url>
```
2. Navigate to the project directory:
```bash
cd PROJECT_DIR
```
3. Place the image you want to encrypt in the same directory.
4. Run the encryption and decryption script:
```bash
python3 PRODIGY_CS_03.py
```
# Example Usage
1. Encryption:
```bash
key = 12345  # Use a secret key for encryption and decryption
encrypt_image("example.jpg", key)
```
This will generate an encrypted image named example_encrypted.png.
2. Decryption:
```bash
decrypt_image("example_encrypted.png", key)
```
This will decrypt the image and generate a file named example_decrypted.png.

# Customization
* You can change the key used for encryption and decryption by modifying the key variable in the script. The same key must be used for both processes.
* The script currently supports PNG and JPEG formats, but it can be extended to support other formats supported by the Pillow library.
