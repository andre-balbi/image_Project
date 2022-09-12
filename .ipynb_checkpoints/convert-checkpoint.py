# To run this code must be intalled on the local machine the ImageMagick app!
import os
from glob import glob
from wand.image import Image

from PIL import Image, ImageDraw

import warnings
warnings.filterwarnings("ignore")

def convert_img(from_='tif', to_='jpg'):
    try:
        print(f'changing dir from: {os.getcwd()}') # Current dir
        os.chdir("./img") # Changint the dir to img folder
        print(f'to: {os.getcwd()}') # Current dir
    except Exception as e:
        os.chdir("../img") # Changing the dir to img folder case failed in the first trial
        pass
    print()
    imgs = [i for i in glob(f"*.{from_}")] # Getting just the 'from_' files in the folder
    
    for i, img in enumerate(imgs): # Looping for each image om the folder
        from wand.image import Image 
        with Image(filename = img) as Sampleimg:  
            Sampleimg.format = to_ # Setting the format
            file_name = f'{img[:-4]}.{to_}' # Spliting the name from the extension and adding the new extension
            os.chdir("../new_img") # Changing the dir to 'new_img' folder
            Sampleimg.save(filename = file_name) # Saving with t
            os.chdir("../img") # Changint the dir to 'img' folder
            print(f'{img} --> .{to_} - {i+1}')

def insert_legend(from_='tif', to_='jpg', pos1=685, pos2=620):
    
    convert_img(from_=from_, to_=to_) # Converting the images
    
    while True:
        try:
            print(f'changing dir from: {os.getcwd()}') # Current dir
            os.chdir("../new_img") # Changint the dir to img folder
            print(f'to: {os.getcwd()}') # Current dir
        except Exception as e:
            os.chdir("../new_img") # Changint the dir to img folder
            pass
        
        offset = (pos1, pos2) # Position of the label
        imgs = [i for i in glob(f"*{to_}")]  # Getting just the 'to_' files in the folder with the new images
        #print(imgs)
        
        background = Image.open(imgs[1])
        legend = Image.open("../legend/legend.jpg")
        background.paste(legend, offset)
        background.show()
        print('Confirmar (s ou n)')
        var = str(input())
        if var != 's':
            print(f'Pos. Horizontal:{pos1}, Pos. Vertical:{pos2}')
            print('Nova Pos. Horizontal:')
            pos1 = int(input())
            print('Nova Pos. Vertical:')
            pos2 = int(input())
            continue
        elif var == 's':
            for img in imgs:
                #print(f'to: {os.getcwd()}') # Current dir
                background = Image.open(img)
                legend = Image.open("../legend/legend.jpg")
                background.paste(legend, offset)
                background.save(img)
            break

insert_legend(from_='tif', to_='jpg')