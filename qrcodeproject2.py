# -----------------------------------------------------------------------------
# Code created by: Mohammed Safwanul Islam @safwandotcom®
# Project: Data Science File Conversion 
# Date created: 15th November 2024
# Organization: N/A
# -----------------------------------------------------------------------------
# Description:
#    This script generates a QR code with an optional logo centered in the middle of the QR code. 
#    The user provides the data to encode (such as a URL or text) and optionally a path to a logo image. 
#    The function generates the QR code, embeds the logo (if provided), and saves the result as an image file. 
#    The code uses high error correction to ensure the QR code remains scannable even if a logo is placed over it. 
#    This is a useful tool for creating branded QR codes with logos or custom designs.
# -----------------------------------------------------------------------------
# License:
# This code belongs to @safwandotcom®.
# Code can be freely used for any purpose with proper attribution.
# -----------------------------------------------------------------------------

import qrcode  # Import the qrcode library to create QR codes
from PIL import Image, ImageDraw  # Import Image and ImageDraw from PIL for image manipulation

# Define a function to generate a QR code with a logo
def generate_qr_code_with_logo(data, filename="qrCode.png", box_size=10, border=2, logo_path=None):
    """
    Generates a QR code image with a centered logo (if provided).

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str, optional): The filename for the saved QR code image. Defaults to "qrCode.png".
        box_size (int, optional): The size of each box in the QR code. Defaults to 10.
        border (int, optional): The size of the border around the QR code. Defaults to 2.
        logo_path (str, optional): The path to the logo image file. Defaults to None.
    """
    
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version=1,  # Set the version of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Set the error correction level to high
        box_size=box_size,  # Set the size of each box in the QR code
        border=border  # Set the size of the border around the QR code
    )
    
    # Add the data to be encoded in the QR code
    qr.add_data(data)  
    qr.make(fit=True)  # Optimize the QR code to fit the data

    # Create an image from the QR code and convert it to RGBA for transparency
    img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    
    # Get the size of the QR code image
    width, height = img.size


    # If a logo path is provided
    if logo_path:
        # Open the logo image and convert it to RGBA
        logo = Image.open(logo_path).convert("RGBA")  
        # Resize the logo to fit within the QR code, making it 1/8th of the smallest QR code dimension
        logo_size = min(width, height) // 8  

        # Resize the logo using LANCZOS filter for high-quality downsampling
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        # Calculate the position to center the logo in the QR code
        logo_position = ((width - logo.width) // 2, (height - logo.height) // 2)

        # Create padding around the logo
        padding = 10  # Define the size of the padding
        rectangle_position = [
            logo_position[0] - padding,  # Left position of the rectangle
            logo_position[1] - padding,  # Top position of the rectangle
            logo_position[0] + logo.width + padding,  # Right position of the rectangle
            logo_position[1] + logo.height + padding  # Bottom position of the rectangle
        ]
        
        # Create a drawing context for the QR code image
        draw = ImageDraw.Draw(img)
        # Draw a white rectangle for padding around the logo
        draw.rectangle(rectangle_position, fill="white")

        # Paste the logo onto the QR code image at the calculated position
        img.paste(logo, logo_position, logo)

    # Save the final QR code image to the specified filename
    img.save(filename)

# Main execution block
if __name__ == "__main__":
    # Prompt the user to enter data for the QR code
    data = input("Enter the data to be encoded in the QR code: ")
    # Prompt the user to enter the path to the logo image file (if available)
    logo_path = input("Enter the path to the logo image file (optional): ").strip('"')
    # Generate the QR code with the specified data and logo
    generate_qr_code_with_logo(data, logo_path=logo_path)


#Sample Data which can be put in order to test
#Generated QR Code will be saved in C/Users/HP 
#https://cubie.kidocode.com/
#F:\Office_SEC\logo black.png
