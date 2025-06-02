import cv2
import numpy as np
import torch
import faiss
img = np.zeros((64,64,3), np.uint8)
cv2.imwrite("tmp.jpg", img)
img2 = cv2.imread("tmp.jpg")
print("cv2 shape:", img2.shape)