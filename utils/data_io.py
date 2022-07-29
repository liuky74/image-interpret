import os
import numpy as np
def rle_decode(mask_rle, shape=(512, 512)):
    '''
    mask_rle: run-length as string formated (start length)
    shape: (height,width) of array to return
    Returns numpy array, 1 - mask, 0 - background

    '''
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape, order='F')

def get_file_name_list(root_dir,ext=None):
    file_list=[]
    if not ext is None:
        if not isinstance(ext,list):
            ext = [ext,]
    dirs = [x for x in os.walk(root_dir)]
    for dir in dirs:
        if len(dir[2])>0:
            for file_name in dir[2]:
                file_name_split = file_name.split(os.sep)
                file_name = ".".join(file_name_split[-1].split('.')[:-1])
                file_ext = file_name_split[-1].split('.')[-1]
                if not ext is None:
                    if not file_ext in ext:
                        continue
                file_list.append(file_name)
    return file_list