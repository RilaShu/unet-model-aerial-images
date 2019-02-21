import cv2
import os


def opencv_binary(img_path_in, img_path_out):
    '''
    Convert gray predict result to binary images by openvc (Otsu's threshold).
    :param img_path_in: original gray images' folder
    :param img_path_out: binary images' folder
    :return: No return
    '''
    # 遍历文件夹，获取所有图像
    img_pathes = []
    for root, dirs, files in os.walk(img_path_in):
        for file in files:
            if file.endswith(".png"):
                img_pathes.append(os.path.join(root, file))
    print('%d images loaded, start to binary...' % len(img_pathes))
    for img_path in img_pathes:
        img = cv2.imread(img_path, 0)
        # Otsu's thresholding
        ret, binary_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        img_name = img_path.split('\\')[-1]
        img_savepath = img_path_out + '\\' + img_name
        cv2.imwrite(img_savepath, binary_img)
    print('Binary finished.')