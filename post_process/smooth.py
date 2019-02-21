import cv2
import os
import numpy as np


def opencv_smooth(img_path_in, img_path_out):
    """
    Smooth images, post process include denoise, dilation and erosion.
    :param img_path_in: binary images' folder.
    :param img_path_out: result.
    :return:
    """
    # 遍历文件夹，获取所有图像
    img_pathes = []
    for root, dirs, files in os.walk(img_path_in):
        for file in files:
            if file.endswith(".png"):
                img_pathes.append(os.path.join(root, file))
    print('%d images loaded, start to smooth...' % len(img_pathes))
    for img_path in img_pathes:
        img = cv2.imread(img_path, 0)
        # denoise
        denoise_img = cv2.fastNlMeansDenoising(img, None, 20)
        # dilation & erosion
        kernel = np.ones((5, 5), np.uint8)
        erosion_1 = cv2.erode(denoise_img, kernel, iterations=3)
        dilation_1 = cv2.dilate(erosion_1, kernel, iterations=3)
        erosion_2 = cv2.erode(dilation_1, kernel, iterations=2)
        result = cv2.dilate(erosion_2, kernel, iterations=2)
        img_name = img_path.split('\\')[-1]
        img_savepath = img_path_out + '\\' + img_name
        cv2.imwrite(img_savepath, result)
    print('Smooth finished.')