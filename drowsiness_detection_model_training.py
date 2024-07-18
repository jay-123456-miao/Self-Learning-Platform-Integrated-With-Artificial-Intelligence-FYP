import re
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
#
# model
#
# img = 'https://i.guim.co.uk/img/media/085a229c9026cc8e045aeb1155d57aab26062ac0/0_132_5000_3001/master/5000.jpg?width=465&dpr=1&s=none'
#
# results = model(img)
# results.print()
# results.show()
#
# # Save the plot as an image file
# plt.figure(figsize=(8, 6))
# plt.imshow(np.squeeze(results.render()))
# plt.axis('off')
# plt.savefig('yolov5_output.png')
# plt.close()
#
# print('Plot saved as yolov5_output.png')
# import uuid
# import os
# import time
#
# image_path = r"C:\Users\ASUS\PycharmProjects\Final_Year_Project\yolov5\data\val"
# labels = ['awake', 'drowsy']
# number_imgs = 50
#
# cap = cv2.VideoCapture(0)
# # Loop through labels
# for label in labels:
#     print('Collecting images for {}'.format(label))
#     time.sleep(5)
#
#     # Loop through image range
#     for img_num in range(number_imgs):
#         print('Collecting images for {}, image number {}'.format(label, img_num))
#
#         # Webcam feed
#         ret, frame = cap.read()
#
#         # Naming out image path
#         imgname = os.path.join(image_path, label + '.' + str(uuid.uuid1()) + '.jpg')
#
#         # Writes out image to file
#         cv2.imwrite(imgname, frame)
#
#         # Render to the screen
#         cv2.imshow('Image Collection', frame)
#
#         # 2 second delay between captures
#         time.sleep(2)
#
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#
#
# cap.release()
# cv2.destroyAllWindows()

# import matplotlib.pyplot as plt
#
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\ASUS\PycharmProjects\Final_Year_Project\yolov5\yolov5\runs\train\exp\weights\last.pt', force_reload=True)
#
# img = r'C:\Users\ASUS\PycharmProjects\Final_Year_Project\yolov5\data\images\awake.0a99605e-37b2-11ef-b4ba-fc34974d5380.jpg'
#
# results = model(img)
#
# results.print()
#
# # Display the image with the detections
# image = plt.figure(figsize=(8, 6))
# plt.imshow(np.squeeze(results.render()))
# plt.axis('off')
# plt.show()
#
# # Save the plot as an image file
# plt.savefig('yolov5_output.png')
# plt.close()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
