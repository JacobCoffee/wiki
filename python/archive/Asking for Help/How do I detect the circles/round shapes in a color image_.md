# Asking for Help/How do I detect the circles/round shapes in a color image?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Hello everybody!

I just installed the python-opencv package on Ubuntu 10.10 and I was wondering how I can use it to detect the circles/round figures in an RGB image. I am not an expert in images and I do not know what terms like HSV and 8-bit image mean(I know these two now, of course).

I tried this code, which I adapted from a website, and it doesn\'t work:

:::: 
::: 
``` 
   1 import cv
   2         
   3 def main():
   4         
   5         storage = cv.CreateMemStorage(0)
   6         
   7         im = cv.LoadImageM("Proba1.jpg")
   8         size = (640, 480)
   9         hsv_im = cv.CreateImage(size, cv.IPL_DEPTH_8U, 3)
  10         thresholded = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
  11         thresholded2 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
  12          
  13         hsv_min = cv.Scalar(0, 50, 170, 0)
  14         hsv_max = cv.Scalar(10, 180, 256, 0)
  15         hsv_min2 = cv.Scalar(170, 50, 170, 0)
  16         hsv_max2 = cv.Scalar(256, 180, 256, 0)
  17         
  18         cv.CvtColor(im, hsv_im, cv.CV_BGR2HSV)
  19         cv.InRangeS(im, hsv_min, hsv_max, thresholded)
  20         cv.InRangeS(im, hsv_min2, hsv_max2, thresholded2)
  21         cv.cvOr(thresholded, thresholded2, thresholded)
  22         # pre-smoothing improves Hough detector
  23         cv.Smooth(im, im, cv.CV_GAUSSIAN, 9, 9)
  24         
  25         
  26         circles = cv.HoughCircles(im, im, cv.CV_HOUGH_GRADIENT, 2, thresholded.height/4, 100, 40, 20, 200)
  27         
  28         
  29 if __name__ == '__main__':
  30         main()
```
:::
::::

The error I get is: OpenCV Error: Sizes of input arguments do not match () in cvCvtColor, file /build/buildd/opencv-2.1.0/src/cv/cvcolor.cpp, line 2208OpenCV Error: Sizes of input arguments do not match () in cvCvtColor, file /build/buildd/opencv-2.1.0/src/cv/cvcolor.cpp, line 2208

I really do NOT understand the whole code above(not the error, the code) since there is no good documentation about opencv and python available. I also tried installing pyopencv but it didn\'t work.

I would be very glad if someone could show me a code sample that takes a .jpg image, makes it 8-bit(because this is another error it gives me) and detects the circles in it. It would also be nice if you could tell me a good opencv tutorial for python.

Thanks for your time and interest and sorry for my grammar.

Calin

# Asking for Help: \... 

\...

A good place to start is the documentation for OpenCV for python. In particular, the cookbook page( [http://opencv.willowgarage.com/documentation/python/cookbook.html](http://opencv.willowgarage.com/documentation/python/cookbook.html)) will be of help. The documentation for the the module was produced by sphinx and leaves much to be desired.

For you\'re problem, I\'d start by replacing the line

            size = (640, 480)

with

            size = cv.GetSize(im)

That will cause the cv.[CreateImage](./CreateImage.html)() calls to create image objects sized with the same dimensions as your input image, whatever it may be. If you really want to have a 640x480 sized image as a result, you could use the cv.Resize() call.

The cv.[CvtColor](./CvtColor.html)() call changes the color model that\'s used for storing the data from RGB to HSV. This is required in order to properly detect changes in hue, brightness, and saturation levels. Since you\'re looking for circles, you likely need to detect changes in hue(color), or at least look for specific hues.

The cv.[HoughCircles](./HoughCircles.html)() call is what actually finds the circles. Its a rather lengthy computation which results finally in a list of circles. There are some parameters in the call that might need to be adjusted in order for it to do a good job of detection. But alas I did not find documentation for this function on the site I mentioned above.

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](..) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
