# Detection and Decoding of Barcode using Image Processing techniques

# Algorithm used for detecting :-
 ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/pr1.jpg)
 
## step 1 : conversion to gray scale image
- colored image contains 3 channel that is three 2d matrices one for red , one for green and another for blue color.
- gray scaling converts 3 channel image into 1 channel image which is one of the important step in the edge detection.

 ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/pr2.jpg)

## step 2 : calculating gradient in both x and y direction
- We use gradients for detecting edges in images, which allows us to find contours and outlines of objects in images.
- Gradient of the image defines the different order of derivative of intensity versus pixel number plot.
- In our project we have used sobel high pass filter which finds approximate first order derivative using sobel operators which are nothing but kernels which various       size and we have taken kernel size of 3 which gives optimum result.
- Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. 
- cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1).
- dx=1 implies derivative in x direction keeping y constant and ksize=-1 implies the kernel size of 3 which is by default and ddpeth is desired depth of output.
- We could also use the Scharr kernel instead of the Sobel kernel which may give us better approximations to the gradient and the function parameters for Scharr gradient   remains same.

## step 3 :  Blurring and Applying Threshold to gradient image
- As in one dimensional signals, images may also can be filtered with various low-pass filters (LPF) and low pass filtering helps in removal of noise and blurring the   image.
- Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content (eg:     noise, edges) from the image.
- In averaging (one of the method of blurring) the average of all the pixels under the kernel area are taken  and replaced with the central element.
- For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value.

## step 4 : Applying Morphological operations 
- Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images.
- It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. 
- Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, Gradient etc also comes into play. 
- Erosion is similar to soil erosion because it erodes away the boundaries of the objects which is essentially removal of white noise in the image.
- Here the white patches other than barcode region are eroded away and boundaries of barcode region also eroded.
- The eroded boundaries can be recovered from the dilation operation which is exactly opposite to erosion.
- The closed operation is dilation followed by erosion.
- The important thing is the object must be white and background must be black and we got this configuration from previous operations.

## step 5 :  Finding the contours and drawing them
- Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool     for shape analysis and object detection and recognition.
- there are three arguments in cv.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it   outputs the contours and hierarchy. Contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of       boundary points of the object.
- We are using retrieval mode as External because it only returns the contours of hierarchy 0 in the hierarchy list and we used Simple as the approximation because to   draw rectangle only 4 points are required and like this we are saving memory.
- To draw the contours, cv2.drawContours( ) function is used.
- If there are many contours in hierarchy 0 then we sort according to the area and take the contour with maximum area because we assume that after filtering the         barcode region will be having more area compared to other contours.
- Pass this as argument to cv2.minAreaRect( ) function which returns the midpoint ,height and width of rectangle and passing this as argument to boxPoints( ) method     gives the four coordinate of rectangle.
- Now give this result as Argument to cv2.drawContours( ) method and we finally get the required result where the red rectangle covers the barcode region of the input   image.


# Results:-
## 1) original image :
  ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/original%20image.png)
  
## 2) gradient in x direction :
  ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/grad%20in%20x%20direction.png)
  
## 3) gradient in y direction :
  ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/gard%20in%20y%20direction.png)
  
## 4) after threshold and morphological operations :
 ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/after%20threshold%20and%20morphological%20operations.png)
 
## 5) final detected image :
 ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/final%20detetced%20image.png)

## 6) decoded results :
 ![App Screenshot](https://github.com/bhim4078652/Detection-and-Decoding-of-Barcode-using-Image-Processing-techniques/blob/main/pr3.jpg)


# Reference(s) :-
- Mr.B.Nagaraju, N.Venkatesh, G.Dhanalakshmi, N.Sai.Chand, D.Haritha. (2022) QR Code Generator and Detector using Python. 
- Adeel U., Yang S., McCann, J. A. (2014). Self-Optimizing Citizen-centric Mobile Urban Sensing Systems. Proceedings of the 11th International Conference on Autonomic   computing (pp.161-167). 
-  Badra M., and Badra R. B. (2016). A Lightweight Security Protocol for NFC-based Mobile Payments. Procedia Computer Science, 83(Ant), 705–711. 
- opencv.org.
- geeks for geeks.













