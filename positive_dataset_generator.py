import tensorflow as tf
import numpy as np
import cv2
import os 
from matplotlib import pyplot as plt

#Enter the path of the original Images
main_path=r"generated dataset"
#Enter the path where folders will be saved
new_path=r"positive dataset"

def new_folder_creater(brand):
    j=os.path.join(new_path,brand)
    os.makedirs(j)
    return j

logo_name=os.listdir(main_path)
for i in logo_name:
    #Every logo image path in logo name(adidas)
    main_im_path=os.path.join(main_path,i)
    
    
    #getting the list of images
    total=[]
    im_crop=[]
    im_main=[]
    im_mask=[]
    total=os.listdir(main_im_path)
    for x in total:
        u=x.split('_')
        if(u[-1]=='crop.jpg'):
            im_crop.append(x)
        elif(u[-1]=='main.jpg'):
            im_main.append(x)
        elif(u[-1]=='mask.png'):
            im_mask.append(x)
        else:
            print("Error in Labelling")
    if(len(im_crop)==len(im_main) and len(im_main)==len(im_mask)):
        print("Everything is Okay")
    else:
        print("the image path is not equal to txt path in "+i)
        
        
    #getting the path of images
    crop_img_path=[]
    main_img_path=[]
    mask_img_path=[]
    for j in im_crop:
        crop_img_path.append(os.path.join(main_im_path,j))
    for j in im_main:
        main_img_path.append(os.path.join(main_im_path,j))
    for j in im_mask:
        mask_img_path.append(os.path.join(main_im_path,j))
    
    #shuffle the crop path
    np.random.shuffle(crop_img_path)
    end_range=len(main_img_path)
    #all image save path
    save_folder=new_folder_creater(i)
    for b in range(0,end_range,1):
        main_img=cv2.imread(main_img_path[b])
        crop_img=cv2.imread(crop_img_path[b])
        mask_img=cv2.imread(mask_img_path[b])
        #save all the images
        main_name=str(b)+'_'+i+'_'+'main'
        main_filename=save_folder+'\\'+main_name+'.jpg'
        cv2.imwrite(main_filename,main_img)
        mask_name=str(b)+'_'+i+'_'+'mask'
        mask_filename=save_folder+'\\'+mask_name+'.png'
        cv2.imwrite(mask_filename,mask_img)
        crop_name=str(b)+'_'+i+'_'+'pcrop'
        crop_filename=save_folder+'\\'+crop_name+'.jpg'
        cv2.imwrite(crop_filename,crop_img)
