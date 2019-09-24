import tensorflow as tf
import numpy as np
import cv2
import os 
from matplotlib import pyplot as plt


#Enter the path of the original Images
main_path=r"generated dataset"
#Enter the path where folders will be saved
new_path=r"final"

def new_folder_creater(path):
    train='training'
    test='test'
    j=os.path.join(path,train)
    k=os.path.join(path,test)
    os.makedirs(j)
    os.makedirs(k)
    return j,k

train_path,test_path=new_folder_creater(new_path)
train_start,train_end,test_start,test_end=0,59,60,70
logo_name=os.listdir(main_path)
for i in logo_name:
    #Every logo image path in logo name(adidas)
    main_im_path=os.path.join(main_path,i)
    total=[]
    total=os.listdir(main_im_path)
    
    #classify in train and test
    train=[]
    test=[]
    for k in total:
        z=int(k.split('_')[0])
        if(z>=train_start and z<=train_end):
            train.append(k)
        elif(z>=test_start and z<test_end):
            test.append(k)
        else:
            print("Something is Wrong")
    
    if(len(total)==(len(train)+len(test))):
        print("Everything is okay")
    else:
        print("problem in path Loading")
        
    
    
    train_img_path=[]
    for j in train:
        train_img_path.append(os.path.join(main_im_path,j))
        
        
    test_img_path=[]
    for j in test:
        test_img_path.append(os.path.join(main_im_path,j))
        
    
    #image saving for training dataset
    end=len(train_img_path)
    for b in range(0,end,1):
        img=cv2.imread(train_img_path[b])
        name=train[b]
        filename=train_path+'\\'+name
        cv2.imwrite(filename,img)
                     
             
    #image saving for test dataset
    end=len(test_img_path)
    for b in range(0,end,1):
        img=cv2.imread(test_img_path[b])
        name=test[b]
        filename=test_path+'\\'+name
        cv2.imwrite(filename,img)
    
    #update the range
    train_start= train_start+70
    train_end=train_end+70
    test_start=test_start+70
    test_end= test_end+70
