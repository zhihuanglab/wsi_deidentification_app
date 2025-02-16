from PIL import Image
import sys
import os

def generate_ico_from_png(png_path, ico_path):
    """
    Convert a PNG image to ICO format
    
    Args:
        png_path (str): Path to the source PNG file
        ico_path (str): Path where the ICO file should be saved
    """
    try:
        # Open the PNG image
        img = Image.open(png_path)
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        # Create ICO file
        img.save(ico_path, format='ICO')
        print(f"Successfully created ICO file at: {ico_path}")
        
    except Exception as e:
        print(f"Error converting PNG to ICO: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Use absolute paths directly
    working_dir = os.path.dirname(os.path.abspath(__file__))
    png_path = os.path.join(working_dir, "4x", "Asset 1@4x.png")
    ico_path = os.path.join(working_dir, "icon.ico")
    generate_ico_from_png(png_path, ico_path)
