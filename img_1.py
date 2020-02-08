import matplotlib.pyplot as plt
import cv2
import pandas as pd
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import numpy as np

image = cv2.imread('8.jpg')
image1 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(image.shape)
x,y,z = image1.shape
image_2d = image1.reshape(x*y, z)
print(image_2d.shape)
plt.imshow(image1)
plt.show()
r = []
g = []
b = []
for line in image:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

pdf = pd.DataFrame({'red':r,'blue':b,'green':g})
pdf['scaled_red'] = whiten(pdf['red'])
pdf['scaled_blue'] = whiten(pdf['blue'])
pdf['scaled_green'] = whiten(pdf['green'])

cluster_centers, distortion = kmeans(pdf[['scaled_red', 'scaled_green', 'scaled_blue']], 2)
print(cluster_centers)
# cluster = KMeans(n_clusters=3)
# cluster.fit(image_2d)
# print(cluster.cluster_centers_[:])
# print(cluster.labels_)
colors = []
r_std, g_std, b_std = pdf[['red', 'green', 'blue']].std()
for cluste_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluste_center
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
    ))

plt.imshow([colors])
plt.show()
# plt.imshow([colors])
# plt.show()
# print(colors)