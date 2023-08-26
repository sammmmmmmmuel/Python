import os 
from PIL import Image       # PIP = pip install pillow
# from IPython.display import Image as Img
# from IPython.display import display

path = os.path.dirname(__file__)
path = f"{path}/images"

img_list = os.listdir(path)
img_list = [path + '/' + x for x in img_list]       # look at for x in img_list (1) then path + '/' + x (2) (for x in img_list : path + '/' + x)
images = [Image.open(x) for x in img_list]

file_name = input("Save File name : ")

gif_img = images[0]
gif_img.save(f'{file_name}.gif', save_all=True, append_images=images[1:], loop=0xff, duration = 1000)
