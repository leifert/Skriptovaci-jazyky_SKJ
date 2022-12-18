from xmlrpc.client import ServerProxy
import numpy as np
from PIL import Image


def load_image(filename):
    try:
        im = Image.open(filename)
        arr = list(im.getdata())
        dct={'size': im.size, 'data': arr}
        return dct
    except FileNotFoundError:
        print("Image not found")
        return None

def save_image(filename, img):
    if img is None: 
        return

    im = Image.new("L", img['size'])
    im.putdata(img['data'])
    im.save(filename)

def main(filepath):
    img = load_image(filepath)
    img_ = filepath.split('.')
    img_name = img_[0]

    server = ServerProxy("http://localhost:10001/")
    server.upload_image(img)
    server.invert_image()

    inverted_img = server.download_image()

    save_image(f"{img_name}_inverted.png", inverted_img)

    server.upload_image(inverted_img)
    server.edge_detect()
    edges_img = server.download_image()
    save_image(f"{img_name}_edges.png", edges_img)



if __name__ == "__main__":
    filepath = "airplane.png"
    main(filepath)
