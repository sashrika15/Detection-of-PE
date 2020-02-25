import pydicom as dicom
import os
import cv2
import PIL
from PIL import Image
import matplotlib.pyplot as plt
#from scipy.misc import imsave

folder_path = "/Users/sashrikasurya/Desktop/dcmdata"

jpg_folder_path = "/Users/sashrikasurya/Desktop/dcmdata"
images_path = os.listdir(folder_path)
lstFilesDCM = []

for dirName, subdirList, fileList in os.walk(folder_path):
    #print (dirName,'/n', subdirList, fileList)
    for filename in fileList:
        if ".dcm" in filename.lower(): 
            lstFilesDCM.append(os.path.join(dirName,filename))

for i in lstFilesDCM:
    dataset = dicom.dcmread(i)
    pixel_array_numpy = dataset.pixel_array
   
    i = i.replace('.dcm','.jpg')
    
    #cv2.imwrite(os.path.join(jpg_folder_path, i), pixel_array_numpy)
   
    plt.imshow(pixel_array_numpy,cmap='gray')
    
    plt.imsave(os.path.join(jpg_folder_path, i),pixel_array_numpy,cmap='gray')
    #plt.show()
    
