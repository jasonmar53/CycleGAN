from PIL import Image
import os, sys

path1 = os.getcwd() + '/testA/'
path2 = os.getcwd() + '/testB/'
path3 = os.getcwd() + '/trainA/'
path4 = os.getcwd() + '/trainB/'

dirs1 = os.listdir(path1)
dirs2 = os.listdir(path2)
dirs3 = os.listdir(path3)
dirs4 = os.listdir(path4)

def resize(dirs, path):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save(f+'.jpg', 'JPEG', quality=90)
resize(dirs2,path2)
resize(dirs4,path4)
#resize(dirs3,path3)
#resize(dirs4,path4)

