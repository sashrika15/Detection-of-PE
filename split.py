''' Split the dataset according to annotations given in json file'''

import json
import shutil 
import os 
name = []
test = []
count = 0
# Path to data
path = "/Users/sashrikasurya/Desktop/JPGs"
for file in os.listdir(path):
    if file.endswith(".jpg"):
       name.append(file)
       #src_dir = "your/source/dir"
       #dst_dir = "your/dest/dir"
       #shutil.move(src_dir,dst_dir)
train = []
# Path to json file
p = open("/Users/sashrikasurya/Desktop/P_Mask_RCNN/annotations/instances_val.json")
data = json.load(p)
for i in data:
    for j in data['images']:
        #print(j['file_name'])
        #if j['file_name'].endswith(".jpg"):
        #    count = count+1
        test.append(j['file_name'])
#print(count(name))

for j in test: 
    try:
        src_dir = "/Users/sashrikasurya/Desktop/JPGs/"+str(j)
        print(src_dir)
        dst_dir = "/Users/sashrikasurya/Desktop/val"
        shutil.move(src_dir,dst_dir)
    except:
        print("Doesnt exist")
