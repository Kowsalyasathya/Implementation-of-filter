###Sharpening Filters
# In[1]: Using Laplacian Kernal

import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

kernel3 = np.array([[0,1,0], [1, -4,1],[0,1,0]])
image5 =cv2.filter2D(image2, -1, kernel3)
plt.imshow(image5)
plt.title('Laplacian Kernel')


# In[2]:Using Laplacian Operator


import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

new_image = cv2.Laplacian (image2, cv2.CV_64F)
plt.imshow(new_image)
plt.title('Laplacian Operator')




