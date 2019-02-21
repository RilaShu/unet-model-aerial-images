# -*- coding: UTF-8 -*-
# @author: RilaShu 
# @DateTime: 2018/12/05 11AM

import cv2
import os


def segmentation(folder_in, folder_out):
    # 遍历文件夹，获取所有tif文件
    lsFiles = []
    for root,dirs,files in os.walk(folder_in):
        for file in files:
            if file.endswith(".tif"):
                lsFiles.append(os.path.join(root, file))
    # 使用数字作为名称命名图像/掩膜文件
    image_name = 0
    for img_path in lsFiles:
        image = cv2.imread(img_path)
        row_num = int(image.shape[0]/256)
        col_num = int(image.shape[1]/256)
        print (row_num)
        for i in range(0, row_num):
            for j in range(0, col_num):
                image_name += 1
                if image_name % 1000 == 0:
                    sub_image = image[i*256:(i*256+256), j*256:(j*256+256)]
                    img_savepath = folder_out + '\\' + str(image_name) + '.png'
                    print (img_savepath)
                    cv2.imwrite(img_savepath, sub_image)
                
                                
if __name__ == "__main__":
    segmentation('images', 'image')