from PIL import Image
import random

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Initialize random seed with the key for reproducibility
    random.seed(key)

    # Encrypt the image by manipulating pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Add a random value (based on key) to each RGB channel and mod by 256
            r = (r + random.randint(0, 255)) % 256
            g = (g + random.randint(0, 255)) % 256
            b = (b + random.randint(0, 255)) % 256
            pixels[x, y] = (r, g, b)
    
    # Save the encrypted image
    encrypted_image_path = image_path.split('.')[0] + "_encrypted.png"
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

# Function to decrypt the image
def decrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Initialize random seed with the key to reproduce the same sequence
    random.seed(key)

    # Decrypt the image by reversing pixel value manipulation
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Subtract the same random value (based on key) from each RGB channel and mod by 256
            r = (r - random.randint(0, 255)) % 256
            g = (g - random.randint(0, 255)) % 256
            b = (b - random.randint(0, 255)) % 256
            pixels[x, y] = (r, g, b)
    
    # Save the decrypted image
    decrypted_image_path = image_path.split('_encrypted')[0] + "_decrypted.png"
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

# Example usage
if __name__ == "__main__":
    key = 12345  # This key will be used for both encryption and decryption
    encrypt_image("example.jpg", key)
    decrypt_image("example_encrypted.png", key)
