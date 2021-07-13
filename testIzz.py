import cv2

img_path = '../cones_dataset/good/images/train/1.png'
mean=(0.485, 0.456, 0.406)
std=(0.229, 0.224, 0.225)
print(img_path)

ori_imgs = cv2.imread('../cones_dataset/good/images/train/1.png') 
print(type(ori_imgs))
print(ori_imgs.shape)
# normalized_imgs = (ori_imgs[::-1] / 255 - mean) / std 