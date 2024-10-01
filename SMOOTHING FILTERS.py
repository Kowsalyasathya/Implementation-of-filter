
###Developed By : Kowsalya M
###Register Number: 212222230069
### Smoothing Filters
# In[1]:Using Averaging Filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

kernel = np.ones((11,11), np. float32)/121
image3 = cv2.filter2D(image2, -1, kernel)

plt.figure(figsize=(9,9))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title('Orignal')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(image3)
plt.title('Filtered')
plt.axis('off')


# In[2]:Using Weighted Averaging Filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

kernel2 = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
image4 = cv2.filter2D(image2, -1, kernel2)
plt.imshow(image4)
plt.title('Weighted Averaging Filtered')



# In[3]:Using Gaussian Filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

gaussian_blur = cv2.GaussianBlur(src=image2, ksize=(11,11), sigmaX=0, sigmaY=0)
plt.imshow(gaussian_blur)
plt.title(' Gaussian Blurring Filtered')

# In[4]:Using Median Filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

gaussian_blur = cv2.GaussianBlur(src=image2, ksize=(11,11), sigmaX=0, sigmaY=0)
plt.imshow(gaussian_blur)
plt.title(' Gaussian Blurring Filtered')






