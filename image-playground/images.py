import sys
import os 
from PIL import Image

first_dir = sys.argv[1]
second_dir = sys.argv[2]



def check_dir(dir, new_dir):
    current = os.getcwd()
    try:
        os.path.isdir(new_dir)
        print(f'Directory \'{new_dir}\' found')
        convert_image(dir, new_dir)
    except FileNotFoundError:
        print('Directory doesn\'t exist\nCreating new directory...')
        os.mkdir(new_dir)
        print(f'Directory \'{new_dir}\'  was created at \'{current}\' directory.')
        
def convert_image(dir, new_dir):
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(dir, filename))
            
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(new_dir, png_filename)
            img.save(png_path, 'PNG')
            
            os.remove(os.path.join(dir, filename))
            
            print(f'{filename} converted to {png_filename} and saved in {new_dir}')


        
check_dir(first_dir, second_dir)