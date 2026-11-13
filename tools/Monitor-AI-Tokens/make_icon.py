import os
import sys
from PIL import Image

def create_ico(png_path, ico_path):
    if not os.path.exists(png_path):
        print(f"Error: {png_path} does not exist")
        return False
    
    img = Image.open(png_path).convert("RGBA")
    
    # Save multi-size ICO
    icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    img.save(ico_path, format="ICO", sizes=icon_sizes)
    print(f"Created ICO: {ico_path}")
    return True

if __name__ == "__main__":
    png = r"C:\Users\migue\Antigravity\Proyectos\Monitor-AI-Tokens\logo.png"
    ico = r"C:\Users\migue\Antigravity\Proyectos\Monitor-AI-Tokens\logo.ico"
    if len(sys.argv) > 1:
        png = sys.argv[1]
    if len(sys.argv) > 2:
        ico = sys.argv[2]
    create_ico(png, ico)
