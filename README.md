# Implementation-of-filter
## Aim:
To implement filters for smoothing and sharpening the images in the spatial domain.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step 1:
Import necessary libraries: OpenCV, NumPy, and Matplotlib.Read an image, convert it to RGB format, define an 11x11 averaging kernel, and apply 2D convolution filtering.Display the original and filtered images side by side using Matplotlib.
<br>
### Step 2:
Define a weighted averaging kernel (kernel2) and apply 2D convolution filtering to the RGB image (image2).Display the resulting filtered image (image4) titled 'Weighted Averaging Filtered' using Matplotlib's imshow function.
<br>
### Step 3:
Apply Gaussian blur with a kernel size of 11x11 and standard deviation of 0 to the RGB image (image2).Display the resulting Gaussian-blurred image (gaussian_blur) titled 'Gaussian Blurring Filtered' using Matplotlib's imshow function.
<br>
### Step 4:
Apply median blur with a kernel size of 11x11 to the RGB image (image2).Display the resulting median-blurred image (median) titled 'Median Blurring Filtered' using Matplotlib's imshow function.
<br>
### Step 5 :
Define a Laplacian kernel (kernel3) and perform 2D convolution filtering on the RGB image (image2).Display the resulting filtered image (image5) titled 'Laplacian Kernel' using Matplotlib's imshow function.
<br>
### Step 6 :
Apply the Laplacian operator to the RGB image (image2) using OpenCV's cv2.Laplacian function.Display the resulting image (new_image) titled 'Laplacian Operator' using Matplotlib's imshow function.
<br>
## Program:
### Developed By   : Kowsalya M
### Register Number: 212222230069
</br>

### 1. Smoothing Filters

i) Using Averaging Filter
```
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



```
ii) Using Weighted Averaging Filter
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

kernel2 = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
image4 = cv2.filter2D(image2, -1, kernel2)
plt.imshow(image4)
plt.title('Weighted Averaging Filtered')

```
iii) Using Gaussian Filter
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

gaussian_blur = cv2.GaussianBlur(src=image2, ksize=(11,11), sigmaX=0, sigmaY=0)
plt.imshow(gaussian_blur)
plt.title(' Gaussian Blurring Filtered')

```
iv)Using Median Filter
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

gaussian_blur = cv2.GaussianBlur(src=image2, ksize=(11,11), sigmaX=0, sigmaY=0)
plt.imshow(gaussian_blur)
plt.title(' Gaussian Blurring Filtered')
```

### 2. Sharpening Filters
i) Using Laplacian Linear Kernal
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

kernel3 = np.array([[0,1,0], [1, -4,1],[0,1,0]])
image5 =cv2.filter2D(image2, -1, kernel3)
plt.imshow(image5)
plt.title('Laplacian Kernel')

```
ii) Using Laplacian Operator
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('jackie.jpeg')
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

new_image = cv2.Laplacian (image2, cv2.CV_64F)
plt.imshow(new_image)
plt.title('Laplacian Operator')
```

## OUTPUT:
### 1. Smoothing Filters
</br>

i) Using Averaging Filter
![image](https://github.com/user-attachments/assets/a5d3ff48-dd8d-430d-b2e8-80b4731d169a)

ii)Using Weighted Averaging Filter
![image](https://github.com/user-attachments/assets/c4bb2f74-01b2-4e85-a232-eb9c88774b60)

iii)Using Gaussian Filter:

![image](https://github.com/user-attachments/assets/a511a544-843f-4ac2-af7c-76f3186f2eb6)

iv) Using Median Filter
![image](https://github.com/user-attachments/assets/bec005d2-67c9-4ead-8a77-aa7207174b36)


### 2. Sharpening Filters
</br>

i) Using Laplacian Kernal
![image](https://github.com/user-attachments/assets/765bedf6-65d7-4a45-9399-887d2c53cd40)


ii) Using Laplacian Operator
![image](https://github.com/user-attachments/assets/f006b9bf-50e4-41c1-abbe-58678c8fbe25)


## Result:
Thus the filters are designed for smoothing and sharpening the images in the spatial domain.
