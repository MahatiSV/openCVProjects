import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("radhekrishna.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#reshape img to 2D array of pixels and 3 color vals (RGB)
pixel_values=image.reshape((-1,3))
print(pixel_values)

pixel_values=np.float32(pixel_values)
print(pixel_values.shape)
#define stopping criteria
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,100,0.2)
#no.of clusters (K) iteration termination "criteria"--tuple of 3 params `(type,max_iter,epsilon)`  ---EPS--specified accuracy epsilon reached max_itr--max iter reached
#flag  specifies KMEANS__PP_CENTERS or RANDOMCENTERS as velow---to specify how initial centers are taken
#o/p params compactness,labels,centers
k=3
_,labels,(centers)=cv2.kmeans(pixel_values,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#convert back to 8 bit values
centers=np.uint8(centers)
#flatten labels array
labels=labels.flatten()
#convert all pixels to color of centroids
segmented_image=centers[labels.flatten()]
#reshape back to org img dimension
segmented_image=segmented_image.reshape(image.shape)
#show img
plt.imshow(segmented_image)
plt.show()
"""img segmentation using k-means clustering
partition img into multiple dif regions to separate each obj and analyze each obj
individually;usually pre-processing
used in self-driving vehicles,health care
k-means--clustering,unsupervised ml --no labelled data available
used to identify dif classes and clusters in given data based on how similar data is
mainly 2 tasks
determine best k value for k center points or centroids by iterative process
assigns each data pt to its closest k-center,based on this a cluster created and so on
s1:select number k to decide no.of clusters
s2:select k random ots
s3:assign each dara to closest centroid
s4:calc variance and place new centroid of each cluster
s5:repeat 3
s6:if any reassign occurs then go to 4 else finish
s7:model ready
"""
